import sys
from utils.controller import Controller
from PySide2.QtWidgets import QApplication
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    asset_previewer_controller = Controller()
    asset_previewer_controller.init_data()
    asset_previewer_controller.show_ui()
    sys.exit(app.exec_())