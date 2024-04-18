#!/bin/bash

user_name=$(id -un)
user_id=$(id -u)
group_id=$(id -g)
docker_group=$(getent group docker | cut -d: -f 3)
source .env

docker build -f Dockerfile . \
            --build-arg user_name=$user_name \
            --build-arg user_id=$user_id \
            --build-arg group_id=$group_id \
            --build-arg docker_group=$docker_group  \
            -t ${DOCKER_IMAGE}
