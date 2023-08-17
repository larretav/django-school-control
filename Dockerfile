FROM python:3.10.4-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk upgrade \
	&& apk add --no-cache gcc musl-dev mariadb-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["sh", "entrypoint.sh"]