#!/bin/bash
source .env
docker run -d --name humanode-alert \
                --network host \
                --restart unless-stopped \
                -v ./:/usr/local/humanode ${DOCKER_IMAGE}
