from PySide6 import QtWidgets, QtCore, QtGui


class ArrangementWidget(QtWidgets.QWidget):
    def __init__(self, text=None, image_path=None):
        super().__init__()

        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.text_label)

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.image_label)

        if text is not None:
            self.set_text(text)

        if image_path is not None:
            self.set_image(image_path)

    def set_text(self, text):
        self.text_label.setText(text)


    def set_image(self, image_path):
        pixmap = QtGui.QPixmap(image_path)
        self.image_label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ArrangementWidget("秀・15玉", "images/strawberry1.png")

    widget.show()

    app.exec()
