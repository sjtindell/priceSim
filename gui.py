import sys
import time
from PyQt4 import QtCore, QtGui
import pyqtgraph
import sim


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('price_sim_app')
        self.setGeometry(200, 200, 400, 600)

        self.layout = QtGui.QVBoxLayout(self)

        self.run_btn = QtGui.QPushButton('run sim')
        self.connect(self.run_btn, QtCore.SIGNAL("released()"), self.run)

        self.plot = pyqtgraph.PlotWidget()

        self.data_widget = QtGui.QTextEdit()

        self.layout.addWidget(self.run_btn)
        self.layout.addWidget(self.plot)
        self.layout.addWidget(self.data_widget)

        self.asset = None

        # threading
        # self.work_thread = None
        self.thread_pool = []

    def plot_batch(self):
        self.asset.update_price()
        self.plot.plot(self.asset.price_history)

    def run(self):

        self.asset = sim.Asset()
        self.asset.set_attributes()

        self.data_widget.clear()

        self.data_widget.append('symbol: {}'.format(self.asset.symbol))
        self.data_widget.append('start price: {}'.format(self.asset.price))
        self.data_widget.append('volatility: {}'.format(self.asset.volatility))

        self.plot.clear()

        # connect to signal from different thread
        # self.work_thread = WorkThread()
        self.thread_pool.append(Worker())
        self.connect(self.thread_pool[-1], QtCore.SIGNAL("update (QString)"), self.plot_batch)
        self.thread_pool[-1].start()


class Worker(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        for _ in range(500):
            time.sleep(0.1)  # artificial time delay
            self.emit(QtCore.SIGNAL('update(QString)'), "update")

        self.terminate()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())