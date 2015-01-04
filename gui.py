import sys
import time
from PyQt4 import QtCore, QtGui
import pyqtgraph
import sim


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('price_sim_app')
        self.setGeometry(200, 200, 1000, 800)

        self.layout = QtGui.QVBoxLayout(self)

        self.run_btn = QtGui.QPushButton('run sim')
        self.connect(self.run_btn, QtCore.SIGNAL("released()"), self.start)

        self.plot = pyqtgraph.PlotWidget()

        self.layout.addWidget(self.run_btn)
        self.layout.addWidget(self.plot)

        # threading
        # self.work_thread = None
        self.thread_pool = []

        self.market = sim.Market()
        self.market.generate_assets(1)
        self.market.update_assets()
        self.asset = self.market.asset_list[0]

    def plot_batch(self):
        self.asset.update_price()
        self.plot.plot(self.asset.price_history)

    def start(self):

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
        for _ in range(5):
            time.sleep(0.3)  # artificial time delay
            self.emit(QtCore.SIGNAL('update(QString)'), "completed job ")

        self.terminate()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())