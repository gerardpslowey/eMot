@ECHO OFF
ECHO Converting .ui files to .py..
pyuic5 -x about_form.ui -o ../about_window.py
pyuic5 -x main_window.ui -o ../main_window.py
pyuic5 -x browser_dialog.ui -o ../browser_dialog.py
pyuic5 -x preferences_window.ui -o ../preferences_window.py
pyuic5 -x metrics.ui -o ../metrics_window.py
ECHO DONE!
pause
