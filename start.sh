#!/bin/bash

app="ifsc_site"
docker build -t ${app} .
echo "Stopping..."
docker stop ${app}
echo "Starting..."
docker run --rm -d -p 8080:80 --name=${app} ${app}
# docker run -d -p 8080:80 --name=${app} -v $PWD:/app ${app}

# Testing command
# docker run --rm -it -p 8080:80 --name=ifsc_site ifsc_site sh