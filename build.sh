#!/bin/bash

HTTP_PORT=8215
APP_NAME="url-shortener-app"
docker build -t ${APP_NAME}
docker run -p ${HTTP_PORT}:${HTTP_PORT} -e PORT=${HTTP_PORT} ${APP_NAME}

# End;
