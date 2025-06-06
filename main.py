import sys
from main_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import re

class NameToBinaryApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_binary_time)
        self.timer.start(1000)

        self.setStyleSheet("""QMainWindow {border-image: url('binnum.jpeg') 0 0 0 0 stretch stretch;}""")

        self.ui.lang_combo.clear()
        self.ui.lang_combo.addItems(["English", "ქართული"])
        self.ui.lang_combo.setCurrentIndex(0)

        self.ui.push_btn.clicked.connect(self.convert_name)
        self.ui.name_input.textChanged.connect(self.validate_input)
        self.ui.lang_combo.currentTextChanged.connect(self.validate_input)

    def validate_input(self):
        name = self.ui.name_input.text()
        language = self.ui.lang_combo.currentText()
        latin_pattern = r'^[A-Za-z ]*$'
        georgian_pattern = r'^[ა-ჰ ]*$'

        if language == "English":
            if re.fullmatch(latin_pattern, name):
                self.ui.warning.setText("")
            else:
                self.ui.warning.setText("Only Latin letters (A-Z, a-z) and spaces allowed.")

        elif language == "ქართული":
            if re.fullmatch(georgian_pattern, name):
                self.ui.warning.setText("")
            else:
                self.ui.warning.setText("დასაშვებია მხოლოდ ქართული ასობგერები და გამოტოვებები საჭიროებისამებრ.")

    def convert_name(self):
        name = self.ui.name_input.text()
        language = self.ui.lang_combo.currentText()
        latin_input = r'^[A-Za-z ]+$'
        georgian_input = r'^[ა-ჰ ]+$'

        if language == "English":
            if re.fullmatch(latin_input, name):
                binary = ' '.join(format(ord(something), '08b') for something in name if something != ' ')
                self.ui.result.setText(f"Your name in binary is: {binary}")
                self.ui.warning.setText("")
            else:
                self.ui.result.setText("")
                self.ui.warning.setText("Please input only Latin letters and spaces if necessary.")

        elif language == "ქართული":
            if re.fullmatch(georgian_input, name):
                binary = ' '.join(format(ord(something), '08b') for something in name if something != ' ')
                self.ui.result.setText(f"თვლის ორობით სისტემაში თქვენი სახელია: {binary}")
                self.ui.warning.setText("")
            else:
                self.ui.result.setText("")
                self.ui.warning.setText("გთხოვთ შეიყვანოთ მხოლოდ ქართული ასობგერები და საჭიროებისამებრ გამოტოვებები.")

    def update_binary_time(self):
        current_time = QtCore.QTime.currentTime()
        hours = format(current_time.hour(), '08b')
        minutes = format(current_time.minute(), '08b')
        seconds = format(current_time.second(), '08b')
        
        binary_time = f"{hours} : {minutes} : {seconds}"
        self.ui.binary_time.setText(binary_time)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NameToBinaryApp()
    window.show()
    sys.exit(app.exec_())