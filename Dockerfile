FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apk add update && apk add libpq-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt


CMD ["sh", "entrypoint.sh"]