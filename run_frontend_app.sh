#!/bin/bash

app="frontend"
docker build -t ${app} front_end
docker run --rm --network=ifsc_app -p 8080:8080 -it --name=${app} -v `pwd`/front_end:/usr/src/app ${app}
