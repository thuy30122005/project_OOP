from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QDialog
import sys

from management1 import Manager, LoginDialog

app = QApplication(sys. argv)

login_dialog = LoginDialog()
login_dialog.exec()  # Thay đổi từ app.exec_()
if login_dialog.logged_in:
    main_window = Manager()
    main_window.show()
    app.exec()
