# QT Designer and .ui files

Generated Python files from .ui are never edited but instead imported into super classes and manipulated there. The convertFiles.bat file is really handy for changing the .ui files to .py.

QT designer is strange in that you must fix the import resource_rc of each generated .py file so that it now reads

> **import pyqt.resource_rc**


## Converting metrics_windows

The metrics_windows uses a QWidget promoted to a QChartview so a view imports need to be changed.

```python
import sys

import pyqt.resource_rc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView
# flake8: noqa
```

## Converting other files

```python
import sys

import pyqt.resource_rc

from PyQt5 import QtCore, QtGui, QtWidgets

# flake8: noqa
```
