# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/demo.ui'
#
# Created: Tue Jul 16 16:35:43 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1297, 705)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.landsharkButton = QtGui.QPushButton(self.centralWidget)
        self.landsharkButton.setGeometry(QtCore.QRect(20, 20, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.landsharkButton.setFont(font)
        self.landsharkButton.setStyleSheet(_fromUtf8("QPushButton:checked {background: rgba(60, 179, 113, 255);}"))
        self.landsharkButton.setCheckable(True)
        self.landsharkButton.setObjectName(_fromUtf8("landsharkButton"))
        self.rcButton = QtGui.QPushButton(self.centralWidget)
        self.rcButton.setEnabled(False)
        self.rcButton.setGeometry(QtCore.QRect(20, 250, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.rcButton.setFont(font)
        self.rcButton.setStyleSheet(_fromUtf8("QPushButton:checked {background: rgba(60, 179, 113, 255);}"))
        self.rcButton.setCheckable(True)
        self.rcButton.setObjectName(_fromUtf8("rcButton"))
        self.attackButton = QtGui.QPushButton(self.centralWidget)
        self.attackButton.setEnabled(False)
        self.attackButton.setGeometry(QtCore.QRect(20, 340, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.attackButton.setFont(font)
        self.attackButton.setStyleSheet(_fromUtf8("QPushButton:checked {background: red;}"))
        self.attackButton.setCheckable(True)
        self.attackButton.setObjectName(_fromUtf8("attackButton"))
        self.console = QtGui.QPlainTextEdit(self.centralWidget)
        self.console.setGeometry(QtCore.QRect(20, 530, 1261, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(13)
        self.console.setFont(font)
        self.console.setPlainText(_fromUtf8(""))
        self.console.setObjectName(_fromUtf8("console"))
        self.ccButton = QtGui.QPushButton(self.centralWidget)
        self.ccButton.setEnabled(False)
        self.ccButton.setGeometry(QtCore.QRect(20, 120, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ccButton.setFont(font)
        self.ccButton.setStyleSheet(_fromUtf8("QPushButton:checked {background: rgba(60, 179, 113, 255);}"))
        self.ccButton.setCheckable(True)
        self.ccButton.setObjectName(_fromUtf8("ccButton"))
        self.attack1RadioButton = QtGui.QRadioButton(self.centralWidget)
        self.attack1RadioButton.setEnabled(False)
        self.attack1RadioButton.setGeometry(QtCore.QRect(30, 440, 121, 20))
        self.attack1RadioButton.setChecked(True)
        self.attack1RadioButton.setObjectName(_fromUtf8("attack1RadioButton"))
        self.attack2RadioButton = QtGui.QRadioButton(self.centralWidget)
        self.attack2RadioButton.setEnabled(False)
        self.attack2RadioButton.setGeometry(QtCore.QRect(30, 470, 121, 20))
        self.attack2RadioButton.setObjectName(_fromUtf8("attack2RadioButton"))
        self.attack3RadioButton = QtGui.QRadioButton(self.centralWidget)
        self.attack3RadioButton.setEnabled(False)
        self.attack3RadioButton.setGeometry(QtCore.QRect(30, 500, 121, 20))
        self.attack3RadioButton.setObjectName(_fromUtf8("attack3RadioButton"))
        self.saveButton = QtGui.QPushButton(self.centralWidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(20, 210, 241, 41))
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton:checked {background: rgba(60, 179, 113, 255);}"))
        self.saveButton.setCheckable(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 10, 1001, 511))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.control_tab = QtGui.QWidget()
        self.control_tab.setObjectName(_fromUtf8("control_tab"))
        self.actualSpeedLCD = QtGui.QLCDNumber(self.control_tab)
        self.actualSpeedLCD.setEnabled(False)
        self.actualSpeedLCD.setGeometry(QtCore.QRect(20, 290, 171, 71))
        self.actualSpeedLCD.setObjectName(_fromUtf8("actualSpeedLCD"))
        self.trimLabel = QtGui.QLabel(self.control_tab)
        self.trimLabel.setEnabled(False)
        self.trimLabel.setGeometry(QtCore.QRect(80, 190, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trimLabel.setFont(font)
        self.trimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trimLabel.setObjectName(_fromUtf8("trimLabel"))
        self.outputPlotLabel = QtGui.QLabel(self.control_tab)
        self.outputPlotLabel.setEnabled(False)
        self.outputPlotLabel.setGeometry(QtCore.QRect(210, 240, 51, 16))
        self.outputPlotLabel.setObjectName(_fromUtf8("outputPlotLabel"))
        self.outputPlot = QtGui.QWidget(self.control_tab)
        self.outputPlot.setEnabled(False)
        self.outputPlot.setGeometry(QtCore.QRect(210, 270, 331, 201))
        self.outputPlot.setStyleSheet(_fromUtf8("background-color: white;"))
        self.outputPlot.setObjectName(_fromUtf8("outputPlot"))
        self.frame_5 = QtGui.QFrame(self.control_tab)
        self.frame_5.setGeometry(QtCore.QRect(310, 0, 21, 21))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: red;"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.setTrimLeftButton = QtGui.QPushButton(self.control_tab)
        self.setTrimLeftButton.setEnabled(False)
        self.setTrimLeftButton.setGeometry(QtCore.QRect(20, 190, 61, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/arrow_left_12x12.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setTrimLeftButton.setIcon(icon)
        self.setTrimLeftButton.setObjectName(_fromUtf8("setTrimLeftButton"))
        self.label_3 = QtGui.QLabel(self.control_tab)
        self.label_3.setGeometry(QtCore.QRect(490, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.kiLabel = QtGui.QLabel(self.control_tab)
        self.kiLabel.setEnabled(False)
        self.kiLabel.setGeometry(QtCore.QRect(10, 140, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kiLabel.setFont(font)
        self.kiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kiLabel.setObjectName(_fromUtf8("kiLabel"))
        self.actualSpeedLabel = QtGui.QLabel(self.control_tab)
        self.actualSpeedLabel.setEnabled(False)
        self.actualSpeedLabel.setGeometry(QtCore.QRect(20, 270, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actualSpeedLabel.setFont(font)
        self.actualSpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actualSpeedLabel.setObjectName(_fromUtf8("actualSpeedLabel"))
        self.estimatedSpeedLCD = QtGui.QLCDNumber(self.control_tab)
        self.estimatedSpeedLCD.setEnabled(False)
        self.estimatedSpeedLCD.setGeometry(QtCore.QRect(20, 400, 171, 71))
        self.estimatedSpeedLCD.setObjectName(_fromUtf8("estimatedSpeedLCD"))
        self.setKIButton = QtGui.QPushButton(self.control_tab)
        self.setKIButton.setEnabled(False)
        self.setKIButton.setGeometry(QtCore.QRect(140, 140, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setKIButton.setFont(font)
        self.setKIButton.setObjectName(_fromUtf8("setKIButton"))
        self.saveRightPlotButton = QtGui.QPushButton(self.control_tab)
        self.saveRightPlotButton.setEnabled(False)
        self.saveRightPlotButton.setGeometry(QtCore.QRect(630, 0, 31, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/folder_image.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveRightPlotButton.setIcon(icon1)
        self.saveRightPlotButton.setObjectName(_fromUtf8("saveRightPlotButton"))
        self.label_5 = QtGui.QLabel(self.control_tab)
        self.label_5.setGeometry(QtCore.QRect(340, 0, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.control_tab)
        self.label.setGeometry(QtCore.QRect(350, 240, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.control_tab)
        self.label_6.setGeometry(QtCore.QRect(830, 0, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame_6 = QtGui.QFrame(self.control_tab)
        self.frame_6.setGeometry(QtCore.QRect(800, 0, 21, 21))
        self.frame_6.setStyleSheet(_fromUtf8("background-color: cyan;"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.rightPlotLabel = QtGui.QLabel(self.control_tab)
        self.rightPlotLabel.setEnabled(False)
        self.rightPlotLabel.setGeometry(QtCore.QRect(550, 0, 71, 16))
        self.rightPlotLabel.setObjectName(_fromUtf8("rightPlotLabel"))
        self.desiredSpeedEdit = QtGui.QLineEdit(self.control_tab)
        self.desiredSpeedEdit.setEnabled(False)
        self.desiredSpeedEdit.setGeometry(QtCore.QRect(20, 40, 91, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.desiredSpeedEdit.setFont(font)
        self.desiredSpeedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.desiredSpeedEdit.setObjectName(_fromUtf8("desiredSpeedEdit"))
        self.desiredSpeedLabel = QtGui.QLabel(self.control_tab)
        self.desiredSpeedLabel.setEnabled(False)
        self.desiredSpeedLabel.setGeometry(QtCore.QRect(20, 9, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.desiredSpeedLabel.setFont(font)
        self.desiredSpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.desiredSpeedLabel.setObjectName(_fromUtf8("desiredSpeedLabel"))
        self.saveOutputPlotButton = QtGui.QPushButton(self.control_tab)
        self.saveOutputPlotButton.setEnabled(False)
        self.saveOutputPlotButton.setGeometry(QtCore.QRect(270, 240, 31, 21))
        self.saveOutputPlotButton.setIcon(icon1)
        self.saveOutputPlotButton.setObjectName(_fromUtf8("saveOutputPlotButton"))
        self.saveInputPlotButton = QtGui.QPushButton(self.control_tab)
        self.saveInputPlotButton.setEnabled(False)
        self.saveInputPlotButton.setGeometry(QtCore.QRect(260, 0, 31, 21))
        self.saveInputPlotButton.setIcon(icon1)
        self.saveInputPlotButton.setObjectName(_fromUtf8("saveInputPlotButton"))
        self.setSpeedButton = QtGui.QPushButton(self.control_tab)
        self.setSpeedButton.setEnabled(False)
        self.setSpeedButton.setGeometry(QtCore.QRect(120, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setSpeedButton.setFont(font)
        self.setSpeedButton.setObjectName(_fromUtf8("setSpeedButton"))
        self.line_2 = QtGui.QFrame(self.control_tab)
        self.line_2.setGeometry(QtCore.QRect(190, 0, 20, 471))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.kpEdit = QtGui.QLineEdit(self.control_tab)
        self.kpEdit.setEnabled(False)
        self.kpEdit.setGeometry(QtCore.QRect(70, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.kpEdit.setFont(font)
        self.kpEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.kpEdit.setObjectName(_fromUtf8("kpEdit"))
        self.label_7 = QtGui.QLabel(self.control_tab)
        self.label_7.setGeometry(QtCore.QRect(710, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.trimValueLabel = QtGui.QLabel(self.control_tab)
        self.trimValueLabel.setEnabled(False)
        self.trimValueLabel.setGeometry(QtCore.QRect(80, 210, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.trimValueLabel.setFont(font)
        self.trimValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trimValueLabel.setObjectName(_fromUtf8("trimValueLabel"))
        self.kiEdit = QtGui.QLineEdit(self.control_tab)
        self.kiEdit.setEnabled(False)
        self.kiEdit.setGeometry(QtCore.QRect(70, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.kiEdit.setFont(font)
        self.kiEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.kiEdit.setObjectName(_fromUtf8("kiEdit"))
        self.estimatedSpeedLabel = QtGui.QLabel(self.control_tab)
        self.estimatedSpeedLabel.setEnabled(False)
        self.estimatedSpeedLabel.setGeometry(QtCore.QRect(20, 380, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.estimatedSpeedLabel.setFont(font)
        self.estimatedSpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.estimatedSpeedLabel.setObjectName(_fromUtf8("estimatedSpeedLabel"))
        self.rightPlot = QtGui.QWidget(self.control_tab)
        self.rightPlot.setEnabled(False)
        self.rightPlot.setGeometry(QtCore.QRect(550, 30, 421, 441))
        self.rightPlot.setStyleSheet(_fromUtf8("background-color: white;"))
        self.rightPlot.setObjectName(_fromUtf8("rightPlot"))
        self.inputPlotLabel = QtGui.QLabel(self.control_tab)
        self.inputPlotLabel.setEnabled(False)
        self.inputPlotLabel.setGeometry(QtCore.QRect(210, 0, 41, 16))
        self.inputPlotLabel.setObjectName(_fromUtf8("inputPlotLabel"))
        self.frame_7 = QtGui.QFrame(self.control_tab)
        self.frame_7.setGeometry(QtCore.QRect(680, 0, 21, 21))
        self.frame_7.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.label_4 = QtGui.QLabel(self.control_tab)
        self.label_4.setGeometry(QtCore.QRect(440, 0, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inputPlot = QtGui.QWidget(self.control_tab)
        self.inputPlot.setEnabled(False)
        self.inputPlot.setGeometry(QtCore.QRect(210, 30, 331, 201))
        self.inputPlot.setStyleSheet(_fromUtf8("background-color: white;"))
        self.inputPlot.setObjectName(_fromUtf8("inputPlot"))
        self.setKPButton = QtGui.QPushButton(self.control_tab)
        self.setKPButton.setEnabled(False)
        self.setKPButton.setGeometry(QtCore.QRect(140, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setKPButton.setFont(font)
        self.setKPButton.setObjectName(_fromUtf8("setKPButton"))
        self.label_2 = QtGui.QLabel(self.control_tab)
        self.label_2.setGeometry(QtCore.QRect(420, 240, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_4 = QtGui.QFrame(self.control_tab)
        self.frame_4.setGeometry(QtCore.QRect(410, 0, 21, 21))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: cyan;"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.setTrimRightButton = QtGui.QPushButton(self.control_tab)
        self.setTrimRightButton.setEnabled(False)
        self.setTrimRightButton.setGeometry(QtCore.QRect(130, 190, 61, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/arrow_right_12x12.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setTrimRightButton.setIcon(icon2)
        self.setTrimRightButton.setObjectName(_fromUtf8("setTrimRightButton"))
        self.kpLabel = QtGui.QLabel(self.control_tab)
        self.kpLabel.setEnabled(False)
        self.kpLabel.setGeometry(QtCore.QRect(10, 110, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kpLabel.setFont(font)
        self.kpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kpLabel.setObjectName(_fromUtf8("kpLabel"))
        self.frame_2 = QtGui.QFrame(self.control_tab)
        self.frame_2.setGeometry(QtCore.QRect(390, 240, 21, 21))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: green;"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.frame = QtGui.QFrame(self.control_tab)
        self.frame.setGeometry(QtCore.QRect(320, 240, 21, 21))
        self.frame.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_3 = QtGui.QFrame(self.control_tab)
        self.frame_3.setGeometry(QtCore.QRect(460, 240, 21, 21))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: magenta;"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.tabWidget.addTab(self.control_tab, _fromUtf8(""))
        self.nav_tab = QtGui.QWidget()
        self.nav_tab.setObjectName(_fromUtf8("nav_tab"))
        self.mapView = QtGui.QGraphicsView(self.nav_tab)
        self.mapView.setEnabled(False)
        self.mapView.setGeometry(QtCore.QRect(225, 11, 761, 461))
        self.mapView.setObjectName(_fromUtf8("mapView"))
        self.waypointListView = QtGui.QListView(self.nav_tab)
        self.waypointListView.setEnabled(False)
        self.waypointListView.setGeometry(QtCore.QRect(10, 31, 201, 441))
        self.waypointListView.setObjectName(_fromUtf8("waypointListView"))
        self.waypointLabel = QtGui.QLabel(self.nav_tab)
        self.waypointLabel.setEnabled(False)
        self.waypointLabel.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.waypointLabel.setObjectName(_fromUtf8("waypointLabel"))
        self.tabWidget.addTab(self.nav_tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1297, 22))
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.landsharkButton, self.ccButton)
        MainWindow.setTabOrder(self.ccButton, self.rcButton)
        MainWindow.setTabOrder(self.rcButton, self.attackButton)
        MainWindow.setTabOrder(self.attackButton, self.console)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HACMS Demo", None))
        self.landsharkButton.setText(_translate("MainWindow", "Landshark", None))
        self.rcButton.setText(_translate("MainWindow", "Resilient Controller", None))
        self.attackButton.setText(_translate("MainWindow", "Attack", None))
        self.ccButton.setText(_translate("MainWindow", "Cruise Control", None))
        self.attack1RadioButton.setText(_translate("MainWindow", "Attack Mode 1", None))
        self.attack2RadioButton.setText(_translate("MainWindow", "Attack Mode 2", None))
        self.attack3RadioButton.setText(_translate("MainWindow", "Attack Mode 3", None))
        self.saveButton.setText(_translate("MainWindow", "Save Data", None))
        self.trimLabel.setText(_translate("MainWindow", "Trim", None))
        self.outputPlotLabel.setText(_translate("MainWindow", "Output", None))
        self.label_3.setText(_translate("MainWindow", "GPS", None))
        self.kiLabel.setText(_translate("MainWindow", "KI", None))
        self.actualSpeedLabel.setText(_translate("MainWindow", "Actual Speed", None))
        self.setKIButton.setText(_translate("MainWindow", "Set", None))
        self.label_5.setText(_translate("MainWindow", "CMD", None))
        self.label.setText(_translate("MainWindow", "LE", None))
        self.label_6.setText(_translate("MainWindow", "REF", None))
        self.rightPlotLabel.setText(_translate("MainWindow", "Odometry", None))
        self.desiredSpeedEdit.setText(_translate("MainWindow", "0.8", None))
        self.desiredSpeedLabel.setText(_translate("MainWindow", "Set Speed", None))
        self.setSpeedButton.setText(_translate("MainWindow", "Set", None))
        self.kpEdit.setText(_translate("MainWindow", "0.05", None))
        self.label_7.setText(_translate("MainWindow", "SPEED", None))
        self.trimValueLabel.setText(_translate("MainWindow", "0.0", None))
        self.kiEdit.setText(_translate("MainWindow", "0.2", None))
        self.estimatedSpeedLabel.setText(_translate("MainWindow", "Estimated Speed", None))
        self.inputPlotLabel.setText(_translate("MainWindow", "Input", None))
        self.label_4.setText(_translate("MainWindow", "REF", None))
        self.setKPButton.setText(_translate("MainWindow", "Set", None))
        self.label_2.setText(_translate("MainWindow", "RE", None))
        self.kpLabel.setText(_translate("MainWindow", "KP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control_tab), _translate("MainWindow", "Control", None))
        self.waypointLabel.setText(_translate("MainWindow", "Waypoints", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nav_tab), _translate("MainWindow", "Navigation", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

import images_rc
