from view.main_view import MainView

class Controller():
    def __init__(self) -> None:
        self.view = MainView()

    def show_ui(self) -> None:
        self.view.setup_ui()
        self.view.show()

    def init_data(self) -> None:
        pass