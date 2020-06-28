#!/bin/bash

app="ifsc_site"
docker build -t ${app} .
echo "Stopping..."
docker stop ${app}
echo "Starting..."

# Background
# docker run --rm -d -p 8080:80 --name=${app} ${app}
docker run --rm -d -p 8080:80 --name=${app} -v $PWD/app:/usr/src/app/app ${app}

# Testing command
# docker run --rm -it -p 8080:80 --name=${app} ${app} sh
# docker run --rm -it -p 8080:80 --name=${app} -v $PWD/app:/usr/src/app/app ${app} sh
