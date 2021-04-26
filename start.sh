#!/bin/bash

echo OFF
echo Starting Python Virtual Environment
cd src
source /.env/bin/activate
echo Starting Docker Container
docker run -d --name splash -it -p 8050:8050 --rm scrapinghub/splash
python emotQT.py