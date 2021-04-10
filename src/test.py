import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import threading

import dash
import dash_core_components as dcc
import dash_html_components as html

class CustomMainWindow(QMainWindow):  # MainWindow is a subclass of QMainWindow
    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Window Title")

        label = QLabel("Label")
        label.setAlignment(Qt.AlignCenter)
#        
        layout = QVBoxLayout()
        
        web = QWebEngineView()
        web.load(QUrl("http://127.0.0.1:8050"))

        layout.addWidget(web)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)        


def run_dash(data, layout):
    app = dash.Dash()

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': data,
                'layout': layout
            })
        ])
    app.run_server(debug=False)

if __name__ == '__main__':
    data = [
        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    ]

    layout = {
        'title': 'Dash Data Visualization'
    }

    threading.Thread(target=run_dash, args=(data, layout), daemon=True).start()

    app = QApplication(sys.argv)

    CMWindow = CustomMainWindow()  # Instead of using QMainWindow, we now use our custom window subclassed from QMainWindow
    CMWindow.show()
    app.exec_()