#!/bin/bash

docker network rm ifsc_app
docker network create --subnet=192.168.0.0/24 ifsc_app

docker run --rm --network=ifsc_app --ip 192.168.0.2 --name mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=example mongo:4.2.8