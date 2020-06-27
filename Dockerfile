FROM python:3.8.3-alpine3.12

WORKDIR /usr/src/app
RUN apk add python3-dev build-base linux-headers pcre-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze
RUN apk add vim
RUN addgroup -S www-data && adduser -S www-data -G www-data

RUN apk add nginx
RUN mkdir -p /etc/nginx
COPY nginx.conf /etc/nginx/nginx.conf

COPY main.py ./
COPY run.sh ./
RUN chmod +x run.sh
COPY uwsgi.ini ./
COPY app ./app
ENV FLASK_APP=main.py

CMD [ "./run.sh" ]