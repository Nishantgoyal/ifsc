FROM python:3.8.3-slim

WORKDIR /usr/src/app
# RUN apk add python3-dev build-base linux-headers pcre-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
EXPOSE 8080
CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "8080" ]