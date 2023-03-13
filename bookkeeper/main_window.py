import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from bookkeeper.view.bookkeepr_widgets import MainWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Bookkeeper")

        # Initialize the expense management widget
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
