@ECHO OFF
ECHO Converting .ui files to .py..
pyuic5 -x about_window.ui -o about_window.py
pyuic5 -x print_window.ui -o print_window.py
pyuic5 -x main_window.ui -o main_window.py
pyuic5 -x browser_dialog.ui -o browser_dialog.py

ECHO converting .qrc to .py....
pyrcc5 resource.qrc -o resource_rc.py

ECHO DONE!
pause