import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget

from ui.save_log_ui import SaveLogUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ui = SaveLogUi()
    qr = Ui.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    Ui.move(qr.topLeft())
    Ui.show()
    sys.exit(app.exec_())
