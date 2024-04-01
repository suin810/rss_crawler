import sys
import datetime

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox,
                             QProgressBar, QFileDialog)
from PyQt5.QtCore import QThread, pyqtSignal, Qt

from src.constants import DATETIME_TODAY

class Crawler(QThread):
    progress_changed = pyqtSignal(int)
    finished = pyqtSignal()

    def run(self):
        pass

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.path_IDs = QPushButton('select ID path')
        self.path_res = QPushButton('select res path')
        self.duration_edit = QLineEdit()
        self.start_button = QPushButton("Start")
        self.end_button = QPushButton("End")
        self.progress_bar = QProgressBar()
        # first boot, end button and progress bar need to be invisable
        self.end_button.setVisible(False)
        self.progress_bar.setVisible(False)

        # Create labels
        path1_label = QLabel("ID 엑셀파일 경로:")
        path2_label = QLabel("결과파일 경로:")
        duration_label = QLabel("주기 (분 단위, 숫자):")
        self.progress_label = QLabel("작동중입니다...")
        self.progress_label.setVisible(False)

        # Layout
        layout = QVBoxLayout()
        path_layout = QHBoxLayout()
        path_layout.addWidget(path1_label)
        path_layout.addWidget(self.path_IDs)
        path_layout.addWidget(path2_label)
        path_layout.addWidget(self.path_res)
        layout.addLayout(path_layout)

        duration_layout = QHBoxLayout()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(self.duration_edit)
        layout.addLayout(duration_layout)

        # progress_layout -> initially invisable
        progress_layout = QHBoxLayout()
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)
        layout.addLayout(progress_layout)

        layout.addWidget(self.start_button)
        layout.addWidget(self.end_button)

        self.setLayout(layout)

        # Connect button click signals to slots
        self.start_button.clicked.connect(self.start_process)
        self.end_button.clicked.connect(self.end_process)
        self.path_IDs.clicked.connect(self.set_origin_path)
        self.path_res.clicked.connect(self.set_res_path)

        # Set window title and size
        self.setWindowTitle("Process Controller")
        self.setGeometry(100, 100, 500, 200)

    def open_file_explorer(self, title, filter):
        file_path, _ = QFileDialog.getOpenFileName(self, title, '', filter)
        return file_path

    def set_origin_path(self):
        file_path = self.open_file_explorer('Select Origin Path', 'Excel Files (*.xlsx)')
        if file_path:
            self.origin_path = file_path
            print("Origin Path:", self.origin_path)

    def set_res_path(self):
        file_path = self.open_file_explorer('Select Result Path', 'Excel Files (*.xlsx)')
        if file_path:
            self.res_path = file_path
            print("Result Path:", self.res_path)

    def start_process(self):
        # allocate given arguments into variables
        duration = int(self.duration_edit.text())

        # set visible status to each buttons
        self.start_button.setVisible(False)
        self.end_button.setVisible(True)
        self.progress_label.setVisible(True)
        self.progress_bar.setVisible(True)
        # Add your logic to start the process here
        QMessageBox.information(self, "작업이 시작되었습니다", f"Path 1: {self.origin_path}, "
                                                         f"Path 2: {self.res_path}, Duration: {duration} minutes")

    def end_process(self):
        # Add your logic to end the process here
        QMessageBox.information(self, "Process Ended", "Process ended")


def run_apps():
    app = QApplication(sys.argv)
    window = MyWidget()
    window.setWindowTitle(f"{DATETIME_TODAY.strftime('%Y-%m-%d')} 일자 블로그 최신글 수집기")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_apps()
