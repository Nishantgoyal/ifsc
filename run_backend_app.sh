#!/bin/bash

app="backend"
docker build -t ${app} back_end
docker run --rm --network=ifsc_app -it --name=${app} -v `pwd`/back_end:/usr/src/app ${app}