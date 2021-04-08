from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None):
        # self.setParent(parent) optional
        fig = Figure(figsize=(5, 5))
        super(MplCanvas, self).__init__(fig)