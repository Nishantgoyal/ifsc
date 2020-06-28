FROM python:3.8.3-alpine3.12

WORKDIR /usr/src/app
RUN apk add python3-dev build-base linux-headers pcre-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze
RUN apk add vim
RUN addgroup -S www-data && adduser -S www-data -G www-data

# RUN apk add nginx
# RUN mkdir -p /etc/nginx /etc/uwsgi

# COPY conf/nginx.conf /etc/nginx/nginx.conf
# COPY conf/uwsgi.ini /etc/uwsgi/uwsgi.ini

# COPY scripts/run.sh ./
# RUN chmod +x run.sh

COPY scripts/main.py ./
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1

# CMD [ "uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini" ]
# CMD [ "./run.sh" ]
CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "80" ]