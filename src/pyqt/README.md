# QT Designer and .ui files

These generated Python files are never edited but instead imported into windows.py and manipulated there. The convertFiles.bat file is really handy for changing the .ui files to .py. 

QT designer is strange in that you must fix the import resource_rc of each generated .py file so that it now reads 

> **import pyqt.resource_rc**

Finally, the generated files are ugly in the way they are created but there's not much that you can do about it unfortunately.