FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED=1
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apk update && apk upgrade \
    && apk add --no-cache \
    git \
    gcc \
    musl-dev \
    libxslt-dev \
    libxml2-dev \
    libffi-dev \
    && apk add --virtual build-deps python3-dev \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip


RUN pip install --no-cache-dir -r requirements.txt


CMD ["sh", "entrypoint.sh"]