from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from driver.list_mnos_log_files import ListMnosLogFiles
from driver.model import Label
from driver.save_log import SaveLog


Default_MnOS_Log_Path = Path(r"C:\Users\Samuel\Desktop\Mnos")


class SaveLogUi(QMainWindow):

    def __init__(self):
        super(SaveLogUi, self).__init__()
        self.setupUi(self)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(819, 449)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.testTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.testTypecomboBox.setGeometry(QtCore.QRect(30, 20, 181, 25))
        self.testTypecomboBox.setObjectName("testTypecomboBox")

        for i in range(len(Label.get_all_type())):
            self.testTypecomboBox.addItem("")

        self.testTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.testTypeLabel.setGeometry(QtCore.QRect(250, 20, 91, 23))
        self.testTypeLabel.setObjectName("testTypeLabel")

        self.logNamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.logNamelineEdit.setGeometry(QtCore.QRect(30, 60, 181, 41))
        self.logNamelineEdit.setObjectName("logNamelineEdit")

        self.defaultDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.defaultDirButton.setGeometry(QtCore.QRect(421, 20, 80, 31))
        self.defaultDirButton.setObjectName("defaultDirButton")
        self.flashDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.flashDirButton.setGeometry(QtCore.QRect(421, 60, 80, 31))
        self.flashDirButton.setObjectName("flashDirButton")
        self.chooseDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseDirButton.setGeometry(QtCore.QRect(507, 20, 98, 31))
        self.chooseDirButton.setObjectName("chooseDirButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(507, 60, 101, 31))
        self.saveButton.setObjectName("saveButton")
        self.logListtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logListtextEdit.setGeometry(QtCore.QRect(30, 130, 361, 261))
        self.logListtextEdit.setObjectName("logListtextEdit")
        self.infotextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.infotextEdit.setGeometry(QtCore.QRect(410, 130, 371, 261))
        self.infotextEdit.setObjectName("infotextEdit")
        self.logNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.logNameLabel.setGeometry(QtCore.QRect(250, 70, 91, 23))
        self.logNameLabel.setObjectName("logNameLabel")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.controlUi(mainWindow)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "日志保存工具"))
        self.testTypeLabel.setText(_translate("mainWindow", "测试标签类型"))
        self.defaultDirButton.setText(_translate("mainWindow", "默认路径"))
        self.flashDirButton.setText(_translate("mainWindow", "刷新路径"))
        self.chooseDirButton.setText(_translate("mainWindow", "选择存储路径"))
        self.saveButton.setText(_translate("mainWindow", "一键保存"))
        self.logNameLabel.setText(_translate("mainWindow", "日志保存名称"))
        self.get_test_items()

    def controlUi(self, mainWindow):
        self.saveButton.clicked.connect(self.saveButton_onclick)
        self.defaultDirButton.clicked.connect(self.defaultDirButton_onclick)
        self.chooseDirButton.clicked.connect(self.chooseDirButton_onclick)
        self.flashDirButton.clicked.connect(self.flashDirButton_onclick)
        self.testTypecomboBox.currentIndexChanged.connect(self.testTypecomboBox_choosed)

    def get_test_items(self):
        _translate = QtCore.QCoreApplication.translate
        items = Label.get_all_type()
        for i in range(len(items)):
            self.testTypecomboBox.setItemText(i, _translate("mainWindow", items[i].value))

    def testTypecomboBox_choosed(self):
        testTpye = self.testTypecomboBox.currentText()
        items = Label.get_all_type()
        for item in items:
            if testTpye.strip() in item.value:
                print(item.name)

    def saveButton_onclick(self):
        testTpye = self.testTypecomboBox.currentText()
        log_name = self.logNamelineEdit.text()
        if len(log_name)==0:
            log_name = "None"
        items = Label.get_all_type()
        testTpye_name = None
        for item in items:
            if testTpye.strip() in item.value:
                testTpye_name = item.name

        a = ListMnosLogFiles(Default_MnOS_Log_Path, _date="2023-09-05")
        target_files = [a.path / i for i in a.get_all_log_files()]

        SaveLog.run(target_files, testTpye_name, log_name, a.path)



    def defaultDirButton_onclick(self):
        print('defaultDirButton clicked')
        self.logListtextEdit.setText('/var/log/MnOS')

    def chooseDirButton_onclick(self):
        print('chooseDirButton clicked')
        dirName = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "All Files(*);;Log Files(*.log)")
        self.logListtextEdit.setText(dirName[0])

    def flashDirButton_onclick(self):
        print('flashDirButton clicked')
