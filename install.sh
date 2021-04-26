#!/bin/bash

echo ON
echo "Installing Python Dependencies"
cd src
which python || echo Python not installed
python -m venv env
source /.env/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Getting scrapinghub docker image
which docker || echo Docker not installed
docker pull scrapinghub/splash

echo System installed!
read -p "Press any key to resume ..."