# /usr/bin/env python3
# -*- coding: utf-8 -*-

# Program      : ToolsBox.py
# Description  : Some tools in one program (network, informations, security, ...)
# Authors      : Eleni, Wilson, Mickaël, Paul
# Creation     : 2018/11/27 
# Update       : 2018/12/01
# Dependences  : - python3 : apt install python3
#                - PyQt4 : apt install python3-pyqt4
#                - scapy : pip3 install scapy
#                - netifaces : pip3 install netifaces

#############
## MODULES ##
#############
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from scapy.all import *
from netifaces import AF_INET
from urllib.request import urlopen
from math import sqrt
import sys, os, uuid, hashlib, time, ipaddress, netifaces, socket, struct, binascii


################
## DESIGN GUI ##
################
## MAIN FORM
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

## MAIN WINDOW
class Ui_winMain(QtGui.QWidget):
    def __init__(self):

        ## MAIN WINDOW PARAMETERS
        QtGui.QWidget.__init__(self)
        winMain = self
        winMain.setObjectName(_fromUtf8("winMain"))
        winMain.resize(913, 727)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        winMain.setFont(font)

        ## COLORS PARAMETERS
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 37))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        winMain.setPalette(palette)

        ## OBJECTS PARAMETERS
        self.centralwidget = QtGui.QWidget(winMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gbxTools = QtGui.QGroupBox(self.centralwidget)
        self.gbxTools.setGeometry(QtCore.QRect(10, 50, 301, 611))
        self.gbxTools.setObjectName(_fromUtf8("gbxTools"))
        self.gbxParam = QtGui.QGroupBox(self.centralwidget)
        self.gbxParam.setEnabled(False)
        self.gbxParam.setGeometry(QtCore.QRect(320, 50, 581, 221))
        self.gbxParam.setObjectName(_fromUtf8("gbxParam"))
        self.lblParam1 = QtGui.QLabel(self.gbxParam)
        self.lblParam1.setVisible(False)
        self.lblParam1.setGeometry(QtCore.QRect(10, 30, 281, 16))
        self.lblParam1.setObjectName(_fromUtf8("lblParam1"))
        self.tbxParam1 = QtGui.QLineEdit(self.gbxParam)
        self.tbxParam1.setVisible(False)
        self.tbxParam1.setGeometry(QtCore.QRect(300, 30, 271, 20))
        self.tbxParam1.setObjectName(_fromUtf8("tbxParam1"))
        self.lblParam2 = QtGui.QLabel(self.gbxParam)
        self.lblParam2.setVisible(False)
        self.lblParam2.setGeometry(QtCore.QRect(10, 60, 281, 16))
        self.lblParam2.setObjectName(_fromUtf8("lblParam2"))
        self.tbxParam2 = QtGui.QLineEdit(self.gbxParam)
        self.tbxParam2.setVisible(False)
        self.tbxParam2.setGeometry(QtCore.QRect(300, 60, 271, 20))
        self.tbxParam2.setObjectName(_fromUtf8("tbxParam2"))
        self.lblParam3 = QtGui.QLabel(self.gbxParam)
        self.lblParam3.setVisible(False)
        self.lblParam3.setGeometry(QtCore.QRect(10, 90, 281, 16))
        self.lblParam3.setObjectName(_fromUtf8("lblParam3"))
        self.tbxParam3 = QtGui.QLineEdit(self.gbxParam)
        self.tbxParam3.setVisible(False)
        self.tbxParam3.setGeometry(QtCore.QRect(300, 90, 271, 20))
        self.tbxParam3.setObjectName(_fromUtf8("tbxParam3"))
        self.lblParam4 = QtGui.QLabel(self.gbxParam)
        self.lblParam4.setVisible(False)
        self.lblParam4.setGeometry(QtCore.QRect(10, 120, 281, 16))
        self.lblParam4.setObjectName(_fromUtf8("lblParam4"))
        self.tbxParam4 = QtGui.QLineEdit(self.gbxParam)
        self.tbxParam4.setVisible(False)
        self.tbxParam4.setGeometry(QtCore.QRect(300, 120, 271, 20))
        self.tbxParam4.setObjectName(_fromUtf8("tbxParam4"))
        self.lblParam5 = QtGui.QLabel(self.gbxParam)
        self.lblParam5.setVisible(False)
        self.lblParam5.setGeometry(QtCore.QRect(10, 150, 281, 16))
        self.lblParam5.setObjectName(_fromUtf8("lblParam5"))
        self.tbxParam5 = QtGui.QLineEdit(self.gbxParam)
        self.tbxParam5.setVisible(False)
        self.tbxParam5.setGeometry(QtCore.QRect(300, 150, 271, 20))
        self.tbxParam5.setObjectName(_fromUtf8("tbxParam5"))
        self.cbxParam = QtGui.QComboBox(self.gbxParam)
        self.cbxParam.setVisible(False)
        self.cbxParam.setGeometry(QtCore.QRect(300, 180, 271, 22))
        self.cbxParam.setObjectName(_fromUtf8("cbxParam"))
        self.cbxParam2 = QtGui.QComboBox(self.gbxParam)
        self.cbxParam2.setVisible(False)
        self.cbxParam2.setGeometry(QtCore.QRect(300, 180, 271, 22))
        self.cbxParam2.setObjectName(_fromUtf8("cbxParam"))
        self.lblParam6 = QtGui.QLabel(self.gbxParam)
        self.lblParam6.setVisible(False)
        self.lblParam6.setGeometry(QtCore.QRect(10, 180, 281, 16))
        self.lblParam6.setObjectName(_fromUtf8("lblParam6"))
        self.gbxOutput = QtGui.QGroupBox(self.centralwidget)
        self.gbxOutput.setGeometry(QtCore.QRect(320, 280, 581, 381))
        self.gbxOutput.setObjectName(_fromUtf8("gbxOutput"))
        self.txtOutput = QtGui.QPlainTextEdit(self.gbxOutput)
        self.txtOutput.setGeometry(QtCore.QRect(10, 20, 561, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtOutput.setFont(font)
        self.txtOutput.setReadOnly(True)
        self.txtOutput.setObjectName(_fromUtf8("txtOutput"))
        self.lblTitle = QtGui.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(40, 10, 821, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.btnHelp = QtGui.QPushButton(self.centralwidget)
        self.btnHelp.setGeometry(QtCore.QRect(880, 10, 21, 23))
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.btnLaunch = QtGui.QPushButton(self.centralwidget)
        self.btnLaunch.setGeometry(QtCore.QRect(10, 670, 441, 31))
        self.btnLaunch.setObjectName(_fromUtf8("btnLaunch"))
        self.btnLaunch.setEnabled(False)
        self.btnClose = QtGui.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(460, 670, 441, 31))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.btnIfconfig = QtGui.QPushButton(self.gbxTools)
        self.btnIfconfig.setGeometry(QtCore.QRect(10, 30, 281, 21))
        self.btnIfconfig.setObjectName(_fromUtf8("btnIfconfig"))
        self.btnPublicIp = QtGui.QPushButton(self.gbxTools)
        self.btnPublicIp.setGeometry(QtCore.QRect(10, 60, 281, 21))
        self.btnPublicIp.setObjectName(_fromUtf8("btnPublicIp"))
        self.btnPing = QtGui.QPushButton(self.gbxTools)
        self.btnPing.setGeometry(QtCore.QRect(10, 90, 281, 21))
        self.btnPing.setObjectName(_fromUtf8("btnPing"))
        self.btnWhois = QtGui.QPushButton(self.gbxTools)
        self.btnWhois.setGeometry(QtCore.QRect(10, 120, 281, 21))
        self.btnWhois.setObjectName(_fromUtf8("btnWhois"))
        self.btnScanIpRange = QtGui.QPushButton(self.gbxTools)
        self.btnScanIpRange.setGeometry(QtCore.QRect(10, 150, 281, 21))
        self.btnScanIpRange.setObjectName(_fromUtf8("btnScanIpRange"))
        self.btnScanPorts = QtGui.QPushButton(self.gbxTools)
        self.btnScanPorts.setGeometry(QtCore.QRect(10, 180, 281, 21))
        self.btnScanPorts.setObjectName(_fromUtf8("btnScanPorts"))
        self.btsnScanArp = QtGui.QPushButton(self.gbxTools)
        self.btsnScanArp.setGeometry(QtCore.QRect(10, 210, 281, 21))
        self.btsnScanArp.setObjectName(_fromUtf8("btsnScanArp"))
        self.btnChangeIp = QtGui.QPushButton(self.gbxTools)
        self.btnChangeIp.setGeometry(QtCore.QRect(10, 240, 281, 21))
        self.btnChangeIp.setObjectName(_fromUtf8("btnChangeIp"))
        self.btnSniffer = QtGui.QPushButton(self.gbxTools)
        self.btnSniffer.setGeometry(QtCore.QRect(10, 270, 281, 21))
        self.btnSniffer.setObjectName(_fromUtf8("btnSniffer"))
        self.btnMacChanger = QtGui.QPushButton(self.gbxTools)
        self.btnMacChanger.setGeometry(QtCore.QRect(10, 300, 281, 21))
        self.btnMacChanger.setObjectName(_fromUtf8("btnMacChanger"))
        self.btnAnonSurf = QtGui.QPushButton(self.gbxTools)
        self.btnAnonSurf.setGeometry(QtCore.QRect(10, 330, 281, 21))
        self.btnAnonSurf.setObjectName(_fromUtf8("btnAnonSurf"))
        self.btnDosAttack = QtGui.QPushButton(self.gbxTools)
        self.btnDosAttack.setGeometry(QtCore.QRect(10, 360, 281, 21))
        self.btnDosAttack.setObjectName(_fromUtf8("btnDosAttack"))
        self.btnGenerateHash = QtGui.QPushButton(self.gbxTools)
        self.btnGenerateHash.setGeometry(QtCore.QRect(10, 390, 281, 21))
        self.btnGenerateHash.setObjectName(_fromUtf8("btnGenerateHash"))
        self.btnSolveEquation = QtGui.QPushButton(self.gbxTools)
        self.btnSolveEquation.setGeometry(QtCore.QRect(10, 420, 281, 21))
        self.btnSolveEquation.setObjectName(_fromUtf8("btnSolveEquation"))
        self.statusbar = QtGui.QStatusBar(winMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.tbxAction = QtGui.QLineEdit(self.centralwidget)
        self.tbxAction.setVisible(False)
        self.retranslateUi(winMain)
        QtCore.QMetaObject.connectSlotsByName(winMain)

        ## OBJECT TEXTS
        winMain.setWindowTitle(_translate("winMain", "MainWindow", None))
        self.gbxTools.setTitle(_translate("winMain", "Tools", None))
        self.gbxParam.setTitle(_translate("winMain", "Parameters", None))
        self.lblParam1.setText(_translate("winMain", "Parameter 1", None))
        self.lblParam2.setText(_translate("winMain", "Parameter 2", None))
        self.lblParam3.setText(_translate("winMain", "Parameter 3", None))
        self.lblParam4.setText(_translate("winMain", "Parameter 4", None))
        self.lblParam5.setText(_translate("winMain", "Parameter 5", None))
        self.lblParam6.setText(_translate("winMain", "Parameter 6", None))
        self.gbxOutput.setTitle(_translate("winMain", "Output", None))
        self.lblTitle.setText(_translate("winMain", "ToolsBox", None))
        self.btnHelp.setText(_translate("winMain", "?", None))
        self.btnLaunch.setText(_translate("winMain", "LAUNCH TOOL", None))
        self.btnClose.setText(_translate("winMain", "CLOSE", None))
        self.btnIfconfig.setText(_translate("winMain", "SHOW IP CONFIGURATION", None))
        self.btnPublicIp.setText(_translate("winMain", "SHOW PUBLIC IP", None))
        self.btnPing.setText(_translate("winMain", "PING HOST", None))
        self.btnChangeIp.setText(_translate("winMain", "CHANGE IP CONFIGURATION", None))
        self.btnMacChanger.setText(_translate("winMain", "CHANGE MAC ADDRESS", None))
        self.btnScanIpRange.setText(_translate("winMain", "SCAN IP RANGE", None))
        self.btnScanPorts.setText(_translate("winMain", "SCAN PORT HOST", None))
        self.btnWhois.setText(_translate("winMain", "WHOIS", None))
        self.btnGenerateHash.setText(_translate("winMain", "GENERATE A HASH", None))
        self.btnSolveEquation.setText(_translate("winMain", "SOLVE SECOND DEGREE EQUATION", None))
        self.btsnScanArp.setText(_translate("winMain", "ARP SCAN", None))
        self.btnSniffer.setText(_translate("winMain", "SNIFFER", None))
        self.btnDosAttack.setText(_translate("winMain", "DOS ATTACK", None))
        self.btnAnonSurf.setText(_translate("winMain", "ANONSURF", None))

    def retranslateUi(self, winMain):
        #########################
        ## PARAMETERS PRINTING ##
        #########################
        def disable_params():
            self.gbxParam.setEnabled(False)
            self.lblParam1.setVisible(False)
            self.tbxParam1.setVisible(False)
            self.lblParam2.setVisible(False)
            self.tbxParam2.setVisible(False)
            self.lblParam3.setVisible(False)
            self.tbxParam3.setVisible(False)
            self.lblParam4.setVisible(False)
            self.tbxParam4.setVisible(False)
            self.lblParam5.setVisible(False)
            self.tbxParam5.setVisible(False)
            self.lblParam6.setVisible(False)
            self.cbxParam.setVisible(False)
            self.cbxParam2.setVisible(False)
            self.cbxParam.setGeometry(QtCore.QRect(300, 180, 271, 22))
            self.cbxParam2.setGeometry(QtCore.QRect(300, 180, 271, 22))
            self.lblParam1.setText("Parameter 1")
            self.lblParam2.setText("Parameter 2")
            self.lblParam3.setText("Parameter 3")
            self.lblParam4.setText("Parameter 4")
            self.lblParam5.setText("Parameter 5")
            self.lblParam6.setText("Parameter 6")
            self.tbxParam1.setText("")
            self.tbxParam2.setText("")
            self.tbxParam3.setText("")
            self.tbxParam4.setText("")
            self.tbxParam5.setText("")
            self.cbxParam.clear()
            self.cbxParam2.clear()
            self.btnLaunch.setEnabled(False)
            self.tbxAction.clear()

        ###############################
        ## WHEN COBOBOX PARAM CHANGE ##
        ###############################
        def cbx_changed(tool):
            tool = self.tbxAction.text()
            text = self.cbxParam.currentText()
            text2 = self.cbxParam2.currentText()
            ## DISPLAYS MORE CHOICE FOR HASH TOOL
            if tool == "hash":
                if text == "SHAKE_128" or text == "SHAKE_256":
                    self.lblParam3.setVisible(True)
                    self.tbxParam3.setVisible(True)
                    self.lblParam3.setText("Length of hash :")
                    self.tbxParam3.setText("15")
                else:
                    self.lblParam3.setVisible(False)
                    self.tbxParam3.setVisible(False)
                    self.lblParam3.setText("Parameter 3 :")
                    self.tbxParam3.setText("")

            ## DISPLAYS MORE CHOICE FOR IP CHANGER TOOL
            elif tool == "changeIp":
                if text2 == "STATIC":
                    self.lblParam3.setVisible(True)
                    self.tbxParam3.setVisible(True)
                    self.lblParam4.setVisible(True)
                    self.tbxParam4.setVisible(True)
                    self.lblParam5.setVisible(True)
                    self.tbxParam5.setVisible(True)
                    self.lblParam3.setText("IP Address :")
                    self.tbxParam3.setText("xxx.xxx.xxx.xxx")
                    self.lblParam4.setText("Mask (not CIDR) :")
                    self.tbxParam4.setText("xxx.xxx.xxx.xxx")
                    self.lblParam5.setText("GATEWAY :")
                    self.tbxParam5.setText("xxx.xxx.xxx.xxx")
                else:
                    self.lblParam3.setVisible(False)
                    self.tbxParam3.setVisible(False)
                    self.lblParam4.setVisible(False)
                    self.tbxParam4.setVisible(False)
                    self.lblParam5.setVisible(False)
                    self.tbxParam5.setVisible(False)
                    self.lblParam3.setText("Parameter 3 :")
                    self.tbxParam3.setText("")
                    self.lblParam4.setText("Parameter 4 :")
                    self.tbxParam4.setText("")
                    self.lblParam5.setText("Parameter 5 :")
                    self.tbxParam5.setText("")


        ###########
        ## TOOLS ##
        ###########
        ## IFCONFIG - ACTION (NO TOOL)
        def ifconfig_action():
            disable_params()
            self.txtOutput.clear()
            output = os.popen('ifconfig').read()
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## SHOW PUBLIC IP - ACTION (NO TOOL)
        def publicIp_action():
            disable_params()
            
            # URL to get public ip
            url = "http://ip.42.pl/raw"
            
            # Contact URL and get content
            public_ip = urlopen(url).read().decode()

            # Output
            output = "Public IP is : " + public_ip + "\n(Given by " + url + ")"
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## PING - TOOL
        def ping_tool():
            disable_params()
            self.tbxAction.clear()
            self.tbxAction.setText("ping")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Host to ping :")

        ## PING - ACTION
        def ping_action():
            self.txtOutput.clear()
            host = self.tbxParam1.text()

            # Testing connexion
            try:
                reply = sr(IP(dst=host)/ICMP(),timeout=2)

                # Check answer
                if reply is None:
                    output = host + " is offline."
                else:
                    output = host + " is online."

            # If no connection
            except:
                output = "Host unreachable"

            # Output
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## CHANGE IP - TOOL
        def changeIp_tool():
            disable_params()
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.cbxParam.setVisible(True)
            self.lblParam2.setVisible(True)
            self.cbxParam2.setVisible(True)
            self.cbxParam.setGeometry(QtCore.QRect(300, 30, 271, 22))
            self.cbxParam2.setGeometry(QtCore.QRect(300, 60, 271, 22))
            self.lblParam1.setText("Network interface to change :")
            self.lblParam2.setText("Type of connection :")
            self.tbxAction.setText("changeIp")
            net_list = os.listdir("/sys/class/net")
            for net in net_list:
                if net != "lo":
                    self.cbxParam.addItem(_fromUtf8(net))
            self.cbxParam2.addItem(_fromUtf8("DHCP"))
            self.cbxParam2.addItem(_fromUtf8("STATIC"))
            self.btnLaunch.setEnabled(True)

        ## CHANGE IP - ACTION
        def changeIp_action():
            self.txtOutput.clear()
            card = self.cbxParam.currentText()
            con_type = self.cbxParam2.currentText()
            self.txtOutput.insertPlainText("Configuring " + card + " with a " + con_type + " connection...")
            
            # Backups currently /etc/network/interfaces file 
            os.system("mv /etc/network/interfaces /etc/network/interfaces.bak")
            
            # Creates a new one
            net_file = open('/etc/network/interfaces','w+')
            net_file.write("#For more information, see interfaces(5) \n#source /etc/network/interfaces.d/* \n \n")
            net_file.write("#The loopack network interface \nauto lo\niface lo inet loopback \n \n")
            
            # DHCP config
            if con_type == "DHCP":
                net_file.write("auto " + card + "\n" + "iface "+ card + " inet dhcp" + "\n" + "\n")
            
            # Static config
            else:
                ip_addr = self.tbxParam3.text()
                netmask = self.tbxParam4.text()
                gateway = self.tbxParam5.text()
                net_file.write("auto " + card + "\n" + "iface " + card + " inet static" + "\n" + "address " + ip_addr + "\n" + "netmask " + netmask + "\n" + "gateway " + gateway + "\n" + "\n")
            
            # Closing interface file
            net_file.close()

            # Output
            self.txtOutput.insertPlainText("\n\n/etc/network/interface file has changed...")
            output = os.popen("cat /etc/network/interfaces").read()
            self.txtOutput.insertPlainText("\n\n" + output)
            self.txtOutput.insertPlainText("Network is restarting...")
            os.system("/etc/init.d/networking restart") 
            self.txtOutput.insertPlainText("\n\nDone.")

        ## CHANGE MAC ADDRESSE - TOOL
        def macchanger_tool():
            disable_params()
            self.tbxAction.setText("macchanger")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.cbxParam.setVisible(True)
            self.cbxParam.setGeometry(QtCore.QRect(300, 30, 271, 22))
            self.lblParam1.setText("Network interface to change :")
            self.btnLaunch.setEnabled(True)
            net_list = os.listdir("/sys/class/net")
            for net in net_list:
                if net != "lo":
                    self.cbxParam.addItem(_fromUtf8(net))


        ## CHANGE MAC ADDRESSE - ACTION
        def macchanger_action():
            # Generate random number
            def randomMAC():
                return [0x00, 0x50, 0x56,
                    random.randint(0x00, 0x7f),
                    random.randint(0x00, 0xff),
                    random.randint(0x00, 0xff)]

            # Format with MAC address pattern
            def formatMAC(mac):
                return ':'.join(map(lambda x: "%02x" % x, mac))

            # Change MAC address
            card = self.cbxParam.currentText()
            mac_addr = randomMAC()
            mac_format = formatMAC(mac_addr)
            os.system("ifdown " + card)
            os.system("ifconfig " + card + " hw ether " + mac_format)
            os.system("ifup " + card)

            # Output
            output = "Your MAC address has changed in : " + mac_format
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## SCAN IP RANGE - TOOL
        def scaniprange_tool():
            disable_params()
            self.tbxAction.setText("scaniprange")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.lblParam1.setText("IP Range to scan :")
            self.tbxParam1.setText("xxx.xxx.xxx.xxx-xxx")
            self.btnLaunch.setEnabled(True)

        ## SCAN IP RANGE - ACTION
        def scaniprange_action():
            self.txtOutput.clear()
            self.txtOutput.insertPlainText("IP range is being scanning ...\n\n")
            output = ""
            rang = self.tbxParam1.text()

            # Testing connection
            try:
                rep,nrep=sr(IP(dst=rang)/ICMP(),timeout=1)
                for hit in rep:
                    if hit[1].type == 0 :
                        output += "Host " + hit[1].src + " is online.\n"

            # If no output
            except:
                output = "Host unreachable."

            # End of the output
            if output == "":
                output = "No host found."
            else:
                output += "\nScan is over."

            # Output
            self.txtOutput.insertPlainText(output)

        ## SCANPORT - TOOL
        def scanports_tool():
            disable_params()
            self.tbxAction.setText("scanports")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.lblParam2.setVisible(True)
            self.tbxParam2.setVisible(True)
            self.lblParam3.setVisible(True)
            self.tbxParam3.setVisible(True)
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Host to scan :")
            self.lblParam2.setText("First port to scan :")
            self.tbxParam2.setText("1")
            self.lblParam3.setText("Last port to scan :")
            self.tbxParam3.setText("1024")

        ## SCANTPORT - ACTION
        def scanports_action():
            host = self.tbxParam1.text()
            fport = "" 
            lport = ""
            output = ""

            # Testing if float iput
            try:
                fport = float(self.tbxParam2.text())
                lport = float(self.tbxParam3.text())
            except:
                output = "Only number are possible for ports parameters."
            
            # If float, launch scan
            if output == "":
                rep,nrep=sr(IP(dst=host)/TCP(dport=(fport,lport)),timeout=2)
                for send,recv in rep:
                    if recv[1].flags == 18 :
                        output += "Port " + str(recv[1].sport) + " is open on " + host + "\n"
                if output == "":
                    output = "No port is opened."
                else: 
                    output += "\nPort scan is over."

            # Output
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## SCAN ARP - TOOL
        def scanarp_tool():
            disable_params()
            self.tbxAction.setText("scanarp")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.cbxParam.setVisible(True)
            self.cbxParam.setGeometry(QtCore.QRect(300, 30, 271, 22))
            self.lblParam1.setText("Network interface :")
            self.btnLaunch.setEnabled(True)
            net_list = os.listdir("/sys/class/net")
            for net in net_list:
                if net != "lo":
                    self.cbxParam.addItem(_fromUtf8(net))

        ## SCAN ARP - ACTION
        def scanarp_action():
            output = ""
            self.txtOutput.clear()
            self.txtOutput.insertPlainText("ARP scan is processing, it will take some time : please wait ...\n\n")
            card = self.cbxParam.currentText()

            # Get the local network
            ip = netifaces.ifaddresses(str(card))[AF_INET][0]['addr']
            mask = netifaces.ifaddresses(str(card))[AF_INET][0]['netmask']
            cidr = ipaddress.ip_interface(str(ip) + '/' + str(mask))

            # Check response for each host in the local network
            for host in ipaddress.IPv4Network(str(cidr.network)):
                arpRequete = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(host), hwdst="ff:ff:ff:ff:ff:ff")
                arpReponse = srp1(arpRequete, timeout=1, verbose=0)
                if arpReponse :
                    output += "P: " + str(arpReponse.psrc) + "\t MAC: " + str(arpReponse.hwsrc)

            # If no output
            if output == "":
                output = "Scan doesn't return anything."

            # Output
            self.txtOutput.insertPlainText(output)

        ## SNIFFER - TOOL
        def sniffer_tool():
            disable_params()
            self.tbxAction.clear()
            self.tbxAction.setText("sniffer")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Packet limit number :")

        ## SNIFFER - ACTION
        def sniffer_action():
            self.txtOutput.clear()
            self.txtOutput.insertPlainText("Sniffing is processing, please wait ...\n\n")

            def AnalyseETH(entete):
                ent_eth = struct.unpack("!6s6s2s", entete)
                source = binascii.hexlify(ent_eth[0]).decode()
                dest = binascii.hexlify(ent_eth[1]).decode()
                self.txtOutput.insertPlainText("\nEthernet")
                self.txtOutput.insertPlainText("-Source :\t " + str(source))
                self.txtOutput.insertPlainText("-Dest :\t\t " + str(dest))
                if ent_eth[2] == b'\x08\x00':
                    return True

            def AnalyseIP(entete):
                ip_hdr = struct.unpack("!9s1s2s4s4s", entete)
                source = socket.inet_ntoa(ip_hdr[3])
                dest = socket.inet_ntoa(ip_hdr[4])
                self.txtOutput.insertPlainText("\nIP")
                self.txtOutput.insertPlainText("-Source :\t " + str(source))
                self.txtOutput.insertPlainText("-Dest :  \t" + str(dest))
                if binascii.hexlify(ip_hdr[1]).decode() == '06':
                    return True
            
                elif binascii.hexlify(ip_hdr[1]).decode() == '11':
                    return False
            
            def AnalyseTCP(entete):
                tcp_hdr = struct.unpack("!HH16s", entete)
                src_port,dst_port,lereste = tcp_hdr
                self.txtOutput.insertPlainText("\nTCP")
                self.txtOutput.insertPlainText("-Port Source :\t" + str(src_port))
                self.txtOutput.insertPlainText("-Port Dest :\t"+ str(dst_port))
                if (src_port == 80) or (dst_port == 80):
                    return True

            def AnalyseUDP(entete):
                udp_hdr = struct.unpack("!HH16s", entete)
                src_port,dst_port,lereste = udp_hdr
                self.txtOutput.insertPlainText("\nUDP")
                self.txtOutput.insertPlainText("-Port Source :\t" + str(src_port))
                self.txtOutput.insertPlainText("-Port Dest :\t" + str(dst_port))

            def AnalyseHTTP(data):
                self.txtOutput.insertPlainText(data)

            rawSock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
            end = self.tbxParam1.text()
            count = 0
            while str(count) != end:
                count = count + 1
                pkt = rawSock.recvfrom(2048)
                self.txtOutput.insertPlainText("\n------------------------------------------\n")
                self.txtOutput.insertPlainText("Received packets:")
                enteteL2,enteteL3,enteteL4,HTTP=pkt[0][0:14],pkt[0][14:34],pkt[0][34:54],pkt[0][54:]
                if AnalyseETH(enteteL2):
                    if AnalyseIP(enteteL3):
                        if AnalyseTCP(enteteL4):
                            AnalyseHTTP(HTTP)
                        else :
                            AnalyseUDP(enteteL3)
                        self.txtOutput.insertPlainText("\nFinish!\n\n")
            self.txtOutput.insertPlainText("\n------------------------------------------\n")

        ## WHOIS - TOOL
        def whois_tool():
            disable_params()
            self.tbxAction.clear()
            self.tbxAction.setText("whois")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Host to search for :")

        ## WHOIS - ACTION
        def whois_action():
            # Host to search
            host = self.tbxParam1.text()

            # Connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("whois.arin.net", 43))   
            s.send((host + "\r\n").encode())
            response = b""

            # Get data
            while True:
                data = s.recv(4096)
                response += data
                if not data:
                    break
            # Close connection
            s.close()

            # Output
            output = response.decode()
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## DOS ATTACK - TOOL
        def dos_tool():
            disable_params()
            self.tbxAction.clear()
            self.tbxAction.setText("dos")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.lblParam2.setVisible(True)
            self.tbxParam2.setVisible(True)
            self.lblParam3.setVisible(True)
            self.tbxParam3.setVisible(True)
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Target Host :")
            self.lblParam2.setText("Target Port :")
            self.lblParam3.setText("Packet limit number :")

        ## DOS ATTACK - ACTION
        def dos_action():
            self.txtOutput.clear()
            host = self.tbxParam1.text()
            port = self.tbxParam2.text()
            limit = self.tbxParam3.text()
            count = 0
            while str(count) != limit:
                count = count + 1
                trame=IP(dst=host)/TCP(flags='S', dport=502)
                send(trame)
                self.txtOutput.insertPlainText("Trame number " + str(count) + " sent. \n")

        ## ANONSURF - TOOL
        def anonsurf_tool():
            disable_params()

            # Check if anonsurf is installed
            self.txtOutput.insertPlainText("Checking anonsurf installation ...\n\n")

            # If anonsurf is not installed, launch installation
            if os.system("anonsurf status 2> /dev/null") != 0:
                self.txtOutput.insertPlainText("Anonsurf installation, please wait ...\n")
                os.system("mkdir /root/anonsurf")
                os.system("cd /root/anonsurf && wget https://github.com/Und3rf10w/kali-anonsurf/archive/master.zip")
                os.system("cd /root/anonsurf && unzip master.zip")
                os.system("cd /root/anonsurf/kali-anonsurf-master/ && ./installer.sh")
                time.sleep(1)
                os.system("rm -r /root/anonsurf")
                os.system("rm libjetty8-java_8.1.16-4_all.deb")

            # Show parameters
            self.tbxAction.setText("anonsurf")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.cbxParam.setVisible(True)
            self.cbxParam.setGeometry(QtCore.QRect(300, 30, 271, 22))
            self.lblParam1.setText("Change status :")
            self.btnLaunch.setEnabled(True)
            self.cbxParam.addItem(_fromUtf8("START"))
            self.cbxParam.addItem(_fromUtf8("STOP"))
            self.cbxParam.addItem(_fromUtf8("RESET"))
            self.txtOutput.clear()

        ## ANONSURF - ACTION
        def anonsurf_action():
            
            # URL to get public IP
            url = "http://ip.42.pl/raw"

            # Action
            self.txtOutput.clear()
            act = self.cbxParam.currentText()
            if act == "START":
                os.system("anonsurf start")
                url = "http://ip.42.pl/raw"
                public_ip = urlopen(url).read().decode()
                output = "Anonsurf Started.\n\nPublic IP is : " + public_ip + "\n(Given by " + url + ")"
            elif act == "STOP":
                os.system("anonsurf stop")
                public_ip = urlopen(url).read().decode()
                output = "Anonsurf Stopped.\n\nPublic IP is : " + public_ip + "\n(Given by " + url + ")"
            elif act == "RESET":
                os.system("anonsurf change")
                url = "http://ip.42.pl/raw"
                public_ip = urlopen(url).read().decode()
                output = "Anonsurf changed IP.\n\nPublic IP is : " + public_ip + "\n(Given by " + url + ")"

            # Output
            self.txtOutput.insertPlainText(output)

        ## GENERATE HASH - TOOL
        def hash_tool():
            disable_params()
            self.tbxAction.setText("hash")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.lblParam2.setVisible(True)
            self.cbxParam.setVisible(True)
            self.cbxParam.setGeometry(QtCore.QRect(300, 60, 271, 22))
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Word to hsah :")
            self.lblParam2.setText("Select the hash method :")
            self.cbxParam.addItem(_fromUtf8("MD5"))
            self.cbxParam.addItem(_fromUtf8("SHA1"))
            self.cbxParam.addItem(_fromUtf8("SHA224"))
            self.cbxParam.addItem(_fromUtf8("SHA256"))
            self.cbxParam.addItem(_fromUtf8("SHA384"))
            self.cbxParam.addItem(_fromUtf8("SHA512"))
            self.cbxParam.addItem(_fromUtf8("SHAKE_128"))
            self.cbxParam.addItem(_fromUtf8("SHAKE_256"))
            self.cbxParam.addItem(_fromUtf8("BLAKE2B"))
            self.cbxParam.addItem(_fromUtf8("BLAKE2S"))
            self.cbxParam.addItem(_fromUtf8("SHA3_224"))
            self.cbxParam.addItem(_fromUtf8("SHA3_256"))
            self.cbxParam.addItem(_fromUtf8("SHA3_384"))
            self.cbxParam.addItem(_fromUtf8("SHA3_512"))

        ## GENERATE HASH - ACTION
        def hash_action():
            # Word to hash
            word = self.tbxParam1.text()

            # Method to use
            method = self.cbxParam.currentText()

            # Action according to method
            if self.lblParam2.isVisible() == True:
                length = self.tbxParam3.text()
            salt = uuid.uuid4().hex
            if method == "MD5":
                result = hashlib.md5(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA1":
                result = hashlib.sha1(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA224":
                result = hashlib.sha224(word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA256":
                result = hashlib.sha256(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA384":
                result = hashlib.sha384(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA512":
                result = hashlib.sha512(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHAKE_128":
                result = hashlib.shake_128(salt.encode() + word.encode())
                result = result.hexdigest(int(length)) + ":" + salt
            elif method == "SHAKE_256":
                result = hashlib.shake_256(salt.encode() + word.encode())
                result = result.hexdigest(int(length)) + ":" + salt
            elif method == "BLAKE2B":
                result = hashlib.blake2b(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "BLAKE2S":
                result = hashlib.blake2s(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA3_224":
                result = hashlib.sha3_224(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA3_256":
                result = hashlib.sha3_256(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA3_384":
                result = hashlib.sha3_384(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt
            elif method == "SHA3_512":
                result = hashlib.sha3_512(salt.encode() + word.encode())
                result = result.hexdigest() + ":" + salt

            # Output
            output = "Generated hash in " + method + " : " + result
            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ## EQUATION - TOOL
        def equation_tool():
            disable_params()
            self.tbxAction.setText("equation")
            self.gbxParam.setEnabled(True)
            self.lblParam1.setVisible(True)
            self.tbxParam1.setVisible(True)
            self.lblParam2.setVisible(True)
            self.tbxParam2.setVisible(True)
            self.lblParam3.setVisible(True)
            self.tbxParam3.setVisible(True)
            self.btnLaunch.setEnabled(True)
            self.lblParam1.setText("Value for A :")
            self.lblParam2.setText("Value for B :")
            self.lblParam3.setText("Value for C :")


        ## EQUATION - ACTION
        def equation_action():
            # Parameters values
            output = ""
            try:
                A = float(self.tbxParam1.text())
                B = float(self.tbxParam2.text())
                C = float(self.tbxParam3.text())
            except:
                output = "Numbers need to be enter. Try again."

            # If parameters are float
            if output == "":
                # Computing delta
                D = B*B-4*A*C

                # Delta < 0 - 0 solution
                if D < 0:
                    output = "No solution because D < 0."

                # Delta = 0 - 1 solution
                elif D == 0:
                    X0=-B/2*A
                    output = "Only one solution because D = 0 :\n\nX0 = " + str(X0)

                # Delta > 0 - 2 solutions
                elif D > 0:
                    X1=-B-sqrt(D)/2*A
                    X2=-B+sqrt(D)/2*A
                    output = "Two solutions because D > 0 :\n\nX1 = " + str(X1) + "\nX2 = " + str(X2) +"\n"

            self.txtOutput.clear()
            self.txtOutput.insertPlainText(output)

        ############
        ## BUTTON ##
        ############
        ## CLOSE BUTTON
        def btnClose_Action():
            app.quit()

        ## LAUNCH BUTTON
        def btnLaunch_Action(tool):
            if tool == "ping":
                ping_action()
            elif tool == "hash":
                hash_action()
            elif tool == "macchanger":
                macchanger_action()
            elif tool == "changeIp":
                changeIp_action()
            elif tool == "equation":
                equation_action()
            elif tool == "scanports":
                scanports_action()
            elif tool == "scaniprange":
                scaniprange_action()
            elif tool == "whois":
                whois_action()
            elif tool == "scanarp":
                scanarp_action()
            elif tool == "sniffer":
                sniffer_action()
            elif tool == "dos":
                dos_action()
            elif tool == "anonsurf":
                anonsurf_action()

        ## HELP BUTTON
        def btnHelp_Action():
            msgBox = QtGui.QMessageBox(self)
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setText("ToolsBox Informations")
            font = QFont()
            font.setFamily("Consolas")
            font.setPointSize(10)
            msgBox.setFont(font)
            msgText = "Program      : ToolsBox.py\n"
            msgText += "Description  : Some tools in one program\n"
            msgText += "               (network, configs, security, ...)\n"
            msgText += "Authors      : Eleni, Wilson, Mickaël, Paul\n"
            msgText += "Creation     : 2018/11/27\n"
            msgText += "Update       : 2018/12/01\n"
            msgText += "Dependences  : - python3 : apt install python3\n"
            msgText += "               - PyQt4 : apt install python3-pyqt4\n"
            msgText += "               - scapy : pip3 install scapy\n"
            msgText += "               - netifaces : pip3 install netifaces\n"
            msgBox.setInformativeText(msgText)
            msgBox.addButton(QtGui.QMessageBox.Ok)
            msgBox.setDefaultButton(QtGui.QMessageBox.Ok) 
            msgBox.exec_()
        
        ## ACTIONS
        self.cbxParam.currentIndexChanged.connect(cbx_changed)
        self.cbxParam2.currentIndexChanged.connect(cbx_changed)
        self.btnClose.clicked.connect(btnClose_Action)
        self.btnLaunch.clicked.connect(lambda: btnLaunch_Action(self.tbxAction.text()))
        self.btnHelp.clicked.connect(btnHelp_Action)
        self.btnIfconfig.clicked.connect(ifconfig_action)
        self.btnPublicIp.clicked.connect(publicIp_action)
        self.btnPing.clicked.connect(ping_tool)
        self.btnChangeIp.clicked.connect(changeIp_tool)
        self.btnMacChanger.clicked.connect(macchanger_tool)
        self.btnScanIpRange.clicked.connect(scaniprange_tool)
        self.btnScanPorts.clicked.connect(scanports_tool)
        self.btnWhois.clicked.connect(whois_tool)
        self.btnGenerateHash.clicked.connect(hash_tool)
        self.btnSolveEquation.clicked.connect(equation_tool)
        self.btsnScanArp.clicked.connect(scanarp_tool)
        self.btnSniffer.clicked.connect(sniffer_tool)
        self.btnDosAttack.clicked.connect(dos_tool)
        self.btnAnonSurf.clicked.connect(anonsurf_tool)

## PROGRAM
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    form = Ui_winMain()
    form.show()
    app.exec_()

