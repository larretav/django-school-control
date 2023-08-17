FROM python:3.9.17-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk upgrade \
    && apk add --no-cache \
    git \
    gcc \
    musl-dev \
    libpq-dev \
    build-essential
    libxslt-dev \
    libxml2-dev \
    libffi-dev \
    && apk add --virtual build-deps python3-dev \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

COPY  ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["sh", "entrypoint.sh"]