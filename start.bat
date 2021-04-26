echo OFF
echo Starting Python Virtual Environment
cd src
call env\Scripts\activate.bat

echo Starting Docker Container
docker stop splash && (
    echo Setting up new container
) || (
    echo Setting up container
)

docker run -d --name splash -i -p 8050:8050 --rm scrapinghub/splash && (
    echo Running new docker
) || (
    echo Running docker
)

python emotQT.py
pause
rem -d (-detach) = Run container in background and print container ID
rem -i (-interactive) = Keep STDIN open even if not attached
rem -p (-publish) = Publish a container's port(s) to the host
rem -rm = Automatically remove the container when it exits