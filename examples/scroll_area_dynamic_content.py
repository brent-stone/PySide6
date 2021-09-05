from PySide6.QtWidgets import *

app = QApplication([])

scroll = QScrollArea()
scroll.setWidgetResizable(True)  # CRITICAL

inner = QFrame(scroll)
inner.setLayout(QVBoxLayout())

scroll.setWidget(inner)  # CRITICAL


def on_remove_widget(button):
    button.deleteLater()


def populate():
    for i in range(40):
        b = QPushButton(inner)
        b.setText(str(i))
        b.clicked.connect(b.deleteLater)
        inner.layout().addWidget(b)

b = QPushButton(inner)
b.setText("Populate")
b.clicked.connect(populate)
inner.layout().addWidget(b)

scroll.show()
app.exec()
