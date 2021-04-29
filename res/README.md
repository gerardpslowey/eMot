# Scripts

The install scripts in this directory will create a Python venv, download the requirements and pull the scrapinghub/splash docker image.

The start scripts will activate the Python venv, and run the docker image.

The install and start script depends on your operating system.

1. Mac OS = macInstall.sh and macStart.sh
2. Linux OS = linuxInstall.sh and linuxStart.sh
3. Windows OS = windowsInstall.sh and windowsStart.sh

## Installation issues

If you can't download the project on Mac OS and pyqt5 specifically, your OS version could be too old. You can refer to the following link otherwise for troubleshooting:

#### [Installing PYQT on Mac OS X](https://pythonschool.net/pyqt/installing-pyqt-on-mac-os-x/)

# Pre-commit-conf
This file is used for installing the dependencies into the virtual env so that any git commits are
checked by the various applications. Git hooks can be seen in the .git folder in the root of your repository. In the hooks folder, you can activate it by removing the .sample from the suffix.

On VSCode, you can view .git files with:
```
"files.exclude": {
        "**/.git": false
    },
```


To use the pre-commit, first install it with pip:
```
pip install pre-commit
```

Then activate the virtual environment and install the dependencies:
```
pip install -r pre-commit-conf.txt
```

This will run every time you go to commit and might change a few things. They don't all need to be adhered to but a lot of beneficial info can be returned. You can run it manually in the project by using:
```
pre-commit run --all-files
```
