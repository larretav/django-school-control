import requests
from decouple import config
from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import status, generics
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, UserAccountStudentRegisterSerializer, UserAccountTeacherRegisterSerializer

AUTH_URL = config('AUTH_URL')

class UserAccountStudentRegisterView(generics.CreateAPIView):
	serializer_class = UserAccountStudentRegisterSerializer
	permission_classes = (AllowAny,)

	def post(self, request, *args, **kwargs):
		try:
			serializer = self.get_serializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			user, student = serializer.save()
			if user and student:
				return Response(status=status.HTTP_201_CREATED)
			else:
				return Response({'status':'Error', 'message':'Error al crear el estudiante'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response({'status':'Error', 'message':'Error al crear el estudiante'}, status=status.HTTP_400_BAD_REQUEST)

class UserAccountTeacherRegisterView(generics.CreateAPIView):
	serializer_class = UserAccountTeacherRegisterSerializer
	permission_classes = (IsAuthenticated, IsAdminUser,)

	def post(self, request, *args, **kwargs):
		try:
			serializer = self.get_serializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			user, teacher = serializer.save()
			if user and teacher:
				return Response(status=status.HTTP_201_CREATED)
			else:
				return Response({'status':'Error', 'message':'Error al crear el maestro'}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({'status':'Error', 'message':'Error al crear el maestro'}, status=status.HTTP_400_BAD_REQUEST)
		
@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):

    try:
        user = User.objects.get(username = request.data['username'], is_active = True)
        if user:
            r = requests.post(
			f'{AUTH_URL}/o/token/',
				data={
					'grant_type': 'password',
					'username': request.data['username'],
					'password': request.data['password'],
					'client_id': config('CLIENT_ID'),
					'client_secret': config('CLIENT_SECRET'),
				},
			)

            user.last_login = datetime.now()
            user.save()

            return Response(r.json()) # retorna el token
        else:
            return Response({'message':'Usuario inactivo'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'status':'Error', 'message':'Error al iniciar sesión'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):

	r = requests.post(
	f'{AUTH_URL}/o/token/',
		data={
			'grant_type': 'refresh_token',
			'refresh_token': request.data['refresh_token'],
			'client_id': config('CLIENT_ID'),
			'client_secret': config('CLIENT_SECRET'),
		},
	)
	return Response(r.json())

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def revoke_token(request):
    
	r = requests.post(
		f'{AUTH_URL}/o/revoke_token/',
		data={
			'token': request.data['token'],
			'client_id': config('CLIENT_ID'),
			'client_secret': config('CLIENT_SECRET'),
		},
	)
	if r.status_code == requests.codes.ok:
		return Response({'message': 'token revoked'}, r.status_code)
	return Response(r.json(), r.status_code)

class UserProfile(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_password(request):
	'''
	Method to update user password.
	{"actual_password": "password", "passwd1": "password1" , "passwd2": "password1"}
	'''
	data = request.data
	user = get_object_or_404(User, pk=request.auth.user_id)

	actual_password = str(data.get('actual_password', ''))
	passwd1 = str(data.get('passwd1', ''))
	passwd2 = str(data.get('passwd2', ''))

	if not user.check_password(data.get('actual_password', None)):
		return Response({'status':'Error', 'message':'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

	if (passwd1 != passwd2) and (passwd1 != '') and (passwd2 != ''):
		return Response({'status':'Error', 'message':'Las contraseñas no coinciden'}, status=status.HTTP_400_BAD_REQUEST)
	elif (passwd1 == ''):
		return Response({'status':'Error', 'message':'Campo passwd1 vacio'}, status=status.HTTP_400_BAD_REQUEST)
	elif (passwd2 == ''):
		return Response({'status':'Error', 'message':'Campo passwd2 vacio'}, status=status.HTTP_400_BAD_REQUEST)
	elif passwd1 == actual_password:
		return Response({'status':'Error', 'message':'La nueva contraseña es igual a la anterior'}, status=status.HTTP_400_BAD_REQUEST)


	user.set_password(passwd1)
	user.save()
	return Response({'status':'OK', 'message':'Contraseña modificada correctamente'}, status=status.HTTP_200_OK)