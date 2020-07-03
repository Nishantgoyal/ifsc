#!/bin/bash

docker run --rm --net=host --name mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=example mongo:4.2.8