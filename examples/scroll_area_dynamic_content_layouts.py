from PySide6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.setWindowTitle("My GUI")
        self.resize(300, 400)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)  # CRITICAL

        self.inner = QFrame(self.scroll)
        self.inner.setLayout(QVBoxLayout())

        self.scroll.setWidget(self.inner)  # CRITICAL

        self.scroll_layout_dict = {}

        b = QPushButton(self.inner)
        b.setText("Populate")
        b.clicked.connect(self.populate)
        self.inner.layout().addWidget(b)

        # When creating MainWindow() from scratch like this,
        # it's necessary to tell PySide6 which widget is
        # the 'central' one for the MainWindow().
        self.setCentralWidget(self.scroll)

        self.show()

    def populate(self):
        for i in range(10):
            b = QPushButton(self.inner)
            b.setText(str(i))
            b.clicked.connect(self.del_button)

            checkbox = QCheckBox(f"Check {i}!", self.inner)

            new_layout = QHBoxLayout(self.inner)
            new_layout.addWidget(b)
            new_layout.addWidget(checkbox)

            n = self.inner.layout().count()
            self.inner.layout().insertLayout(n, new_layout)
            self.scroll_layout_dict[b] = new_layout

    def del_button(self):
        button: QPushButton = self.sender()
        layout: QVBoxLayout = self.scroll_layout_dict[button]
        while layout.count() > 0:
            layout.takeAt(0).widget().deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
