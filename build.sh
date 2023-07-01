#!/bin/bash

HTTP_PORT=8215
APP_NAME="my-url-shortener-app"

echo "docker container rm --force \"${APP_NAME}\""
echo "docker build -t ${APP_NAME} ."
echo "docker run -d --name ${APP_NAME} --sysctl net.ipv4.ip_unprivileged_port_start=0 --publish ${HTTP_PORT}:${HTTP_PORT} ${APP_NAME}"

docker container rm --force "${APP_NAME}"
docker build -t ${APP_NAME} .
docker run -d --name ${APP_NAME} --sysctl net.ipv4.ip_unprivileged_port_start=0 --publish ${HTTP_PORT}:${HTTP_PORT} ${APP_NAME}

# End;
