echo OFF
echo Starting Python Virtual Environment
cd src
call env\Scripts\activate.bat
echo Starting Docker Container
docker run -d --name splash -it -p 8050:8050 --rm scrapinghub/splash
python emotQT.py