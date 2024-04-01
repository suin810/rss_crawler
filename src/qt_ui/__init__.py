import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.path1_edit = QLineEdit()
        self.path2_edit = QLineEdit()
        self.duration_edit = QLineEdit()
        self.start_button = QPushButton("Start")
        self.end_button = QPushButton("End")

        # Create labels
        path1_label = QLabel("ID 엑셀파일 경로:")
        path2_label = QLabel("결과파일 경로:")
        duration_label = QLabel("주기 (분 단위, 숫자):")

        # Layout
        layout = QVBoxLayout()
        path_layout = QHBoxLayout()
        path_layout.addWidget(path1_label)
        path_layout.addWidget(self.path1_edit)
        path_layout.addWidget(path2_label)
        path_layout.addWidget(self.path2_edit)
        layout.addLayout(path_layout)

        duration_layout = QHBoxLayout()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(self.duration_edit)
        layout.addLayout(duration_layout)

        layout.addWidget(self.start_button)
        layout.addWidget(self.end_button)

        self.setLayout(layout)

        # Connect button click signals to slots
        self.start_button.clicked.connect(self.start_process)
        self.end_button.clicked.connect(self.end_process)

        # Set window title and size
        self.setWindowTitle("Process Controller")
        self.setGeometry(100, 100, 400, 200)

    def start_process(self):
        path1 = self.path1_edit.text()
        path2 = self.path2_edit.text()
        duration = self.duration_edit.text()
        # Add your logic to start the process here
        QMessageBox.information(self, "Process Started", f"Process started with Path 1: {path1}, "
                                                         f"Path 2: {path2}, Duration: {duration} minutes")

    def end_process(self):
        # Add your logic to end the process here
        QMessageBox.information(self, "Process Ended", "Process ended")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
