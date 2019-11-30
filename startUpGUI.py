from PyQt5 import QtCore, QtGui, QtWidgets
from raceNameGUI import Ui_RaceNamesMainWindow



class Ui_StartupMainWindow(object):
    def setupStartUpUi(self, StartupMainWindow):
        StartupMainWindow.setObjectName("StartupMainWindow")
        StartupMainWindow.resize(502, 198)
        self.centralwidget = QtWidgets.QWidget(StartupMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartNewRacePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartNewRacePushButton.setGeometry(QtCore.QRect(40, 70, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartNewRacePushButton.sizePolicy().hasHeightForWidth())
        self.StartNewRacePushButton.setSizePolicy(sizePolicy)
        self.StartNewRacePushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StartNewRacePushButton.setFont(font)
        self.StartNewRacePushButton.setObjectName("StartNewRacePushButton")
        self.StartNewRacePushButton.clicked.connect(self.startNewRace)
        self.resumeRacePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeRacePushButton.setGeometry(QtCore.QRect(310, 70, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumeRacePushButton.sizePolicy().hasHeightForWidth())
        self.resumeRacePushButton.setSizePolicy(sizePolicy)
        self.resumeRacePushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resumeRacePushButton.setFont(font)
        self.resumeRacePushButton.setObjectName("resumeRacePushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 471, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        StartupMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartupMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        StartupMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartupMainWindow)
        self.statusbar.setObjectName("statusbar")
        StartupMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartupMainWindow)
        QtCore.QMetaObject.connectSlotsByName(StartupMainWindow)

    def retranslateUi(self, StartupMainWindow):
        _translate = QtCore.QCoreApplication.translate
        StartupMainWindow.setWindowTitle(_translate("StartupMainWindow", "Clocker"))
        self.StartNewRacePushButton.setText(_translate("StartupMainWindow", "Start New Race"))
        self.resumeRacePushButton.setText(_translate("StartupMainWindow", "Resume Existing Race"))
        self.label.setText(_translate("StartupMainWindow", "What do you want to do?"))

    def startNewRace(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RaceNamesMainWindow()
        self.ui.setupRaceNamesUi(self.window)
        self.window.show()
        StartupMainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartupMainWindow = QtWidgets.QMainWindow()
    ui = Ui_StartupMainWindow()
    ui.setupStartUpUi(StartupMainWindow)
    StartupMainWindow.show()
    sys.exit(app.exec_())
