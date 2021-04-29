#!/bin/bash

echo ON
echo "Installing Python Dependencies"
cd ../src
which python3 || echo Python not installed
sudo apt-get install python3-venv
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo Getting scrapinghub docker image
which docker || echo Docker not installed
sudo docker pull scrapinghub/splash
sudo apt-get install --reinstall libxcb-xinerama0

echo System installed!
read -p "Press any key to resume ..."
