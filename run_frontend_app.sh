#!/bin/bash

app="frontend"
docker build -t ${app} front_end
docker run --rm -it -p 8080:80 --name=${app} -v `pwd`/front_end:/usr/src/app ${app}
