#!/bin/bash

echo OFF
echo Starting Python Virtual Environment
cd ..
source env/bin/activate

echo Starting Docker Container
sudo docker stop splash && (
    echo Setting up new container
) || (
    echo Setting up container
)

sudo docker run -d --name splash -i -p 8050:8050 --rm scrapinghub/splash && (
    echo Running new docker
) || (
    echo Running docker
)
python3 emotQT.py

# -d (-detach) = Run container in background and print container ID
# -i (-interactive) = Keep STDIN open even if not attached
# -p (-publish) = Publish a container's port(s) to the host
# -rm = Automatically remove the container when it exits
