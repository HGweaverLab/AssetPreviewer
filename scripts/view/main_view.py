from PySide2 import QtWidgets

class MainView(QtWidgets.QMainWindow):
    def __init__(self, _parent :QtWidgets.QWidget=None) -> None:
        super(MainView, self).__init__(_parent)
        self.setup_ui()

    def setup_ui(self) -> None:
        """Design ui"""

        self.main_wg = QtWidgets.QWidget()
        self.setCentralWidget(self.main_wg)