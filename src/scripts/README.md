# Python script to Executables

The exe files are created by placing start.py and installer.py in the root directory
and running the following command:

```
pyinstaller --onefile PROGRAMNAME.py -windowed
```

The exe file will be palced in a folder called dist.
The exe will then check the system platform and call either the batch or bash scripts.