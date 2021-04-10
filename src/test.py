import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import threading

import dash
import dash_core_components as dcc
import dash_html_components as html


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Window Title")

        label = QtWidgets.QLabel("Label")
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QtWidgets.QVBoxLayout()

        web = QtWebEngineWidgets.QWebEngineView()
        web.load(QtCore.QUrl("http://127.0.0.1:8080"))

        layout.addWidget(web)

        widget = QtWidgets.QWidget()
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
        ])  # noqa
    app.run_server(debug=False)


if __name__ == '__main__':
    data = [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}]

    layout = {
        'title': 'Dash Data Visualization'
    }

    threading.Thread(target=run_dash, args=(data, layout), daemon=True).start()

    app = QtWidgets.QApplication(sys.argv)

    # Instead of using QMainWindow, we now use our custom window subclassed from QMainWindow
    CMWindow = CustomMainWindow()
    CMWindow.show()
    app.exec_()
