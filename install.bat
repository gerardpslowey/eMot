echo ON

echo Installing Python Dependencies
cd src
where python || echo Python not installed
python -m venv env
call env\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Getting scrapinghub docker image
where docker || echo Docker not installed
docker pull scrapinghub/splash

echo System installed!
pause
