# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.setEnabled(True)
        LoginForm.resize(400, 600)
        LoginForm.setMinimumSize(QtCore.QSize(400, 600))
        LoginForm.setMaximumSize(QtCore.QSize(400, 600))
        LoginForm.setAutoFillBackground(False)
        LoginForm.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.762, y2:0.715909, stop:0 rgba(32, 35, 147, 255), stop:1 rgba(15, 154, 90, 255));\n"
"QPushButton#connectButton {\n"
"border-color: rgb(15, 154, 90, 255);\n"
"};\n"
"")
        self.widget = QtWidgets.QWidget(LoginForm)
        self.widget.setGeometry(QtCore.QRect(1, 4, 401, 601))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setMinimumSize(QtCore.QSize(350, 300))
        self.logo.setMaximumSize(QtCore.QSize(350, 300))
        self.logo.setStyleSheet("background-color:rgba(255, 255, 255, 0)")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../aprs/icon1.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)
        self.host_line = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.host_line.sizePolicy().hasHeightForWidth())
        self.host_line.setSizePolicy(sizePolicy)
        self.host_line.setMinimumSize(QtCore.QSize(350, 35))
        self.host_line.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.host_line.setFont(font)
        self.host_line.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.host_line.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-radius:17px;\n"
"border: 2px solid black;\n"
"")
        self.host_line.setAlignment(QtCore.Qt.AlignCenter)
        self.host_line.setObjectName("host_line")
        self.verticalLayout.addWidget(self.host_line, 0, QtCore.Qt.AlignHCenter)
        self.port_line = QtWidgets.QLineEdit(self.widget)
        self.port_line.setMinimumSize(QtCore.QSize(350, 35))
        self.port_line.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.port_line.setFont(font)
        self.port_line.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-radius:17px;\n"
"border: 2px solid black;\n"
"")
        self.port_line.setAlignment(QtCore.Qt.AlignCenter)
        self.port_line.setObjectName("port_line")
        self.verticalLayout.addWidget(self.port_line, 0, QtCore.Qt.AlignHCenter)
        self.db_line = QtWidgets.QLineEdit(self.widget)
        self.db_line.setMinimumSize(QtCore.QSize(350, 35))
        self.db_line.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.db_line.setFont(font)
        self.db_line.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-radius:17px;\n"
"border: 2px solid black;\n"
"")
        self.db_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.db_line.setAlignment(QtCore.Qt.AlignCenter)
        self.db_line.setObjectName("db_line")
        self.verticalLayout.addWidget(self.db_line, 0, QtCore.Qt.AlignHCenter)
        self.user_line = QtWidgets.QLineEdit(self.widget)
        self.user_line.setMinimumSize(QtCore.QSize(350, 35))
        self.user_line.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.user_line.setFont(font)
        self.user_line.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-radius:17px;\n"
"border: 2px solid black;\n"
"")
        self.user_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.user_line.setAlignment(QtCore.Qt.AlignCenter)
        self.user_line.setObjectName("user_line")
        self.verticalLayout.addWidget(self.user_line, 0, QtCore.Qt.AlignHCenter)
        self.pass_line = QtWidgets.QLineEdit(self.widget)
        self.pass_line.setMinimumSize(QtCore.QSize(350, 35))
        self.pass_line.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.pass_line.setFont(font)
        self.pass_line.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-radius:17px;\n"
"border: 2px solid black;\n"
"")
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_line.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_line.setObjectName("pass_line")
        self.verticalLayout.addWidget(self.pass_line, 0, QtCore.Qt.AlignHCenter)
        self.connectButton = QtWidgets.QPushButton(self.widget)
        self.connectButton.setMinimumSize(QtCore.QSize(150, 50))
        self.connectButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setStyleSheet("QPushButton#connectButton:hover {\n"
" background-color: rgba(15, 154, 90, 255); \n"
" border: 3px solid;\n"
" border-color: rgb(20, 58, 98);\n"
"}\n"
"QPushButton#connectButton:pressed {\n"
" background-color: rgb(20, 58, 98);\n"
" }\n"
"QPushButton#connectButton {\n"
"background-color:rgb(20, 58, 98);\n"
"border-radius:25px;\n"
"}")
        self.connectButton.setAutoDefault(False)
        self.connectButton.setDefault(False)
        self.connectButton.setFlat(False)
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout.addWidget(self.connectButton, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.host_line.setPlaceholderText(_translate("LoginForm", "127.0.0.1"))
        self.port_line.setPlaceholderText(_translate("LoginForm", "5432"))
        self.db_line.setPlaceholderText(_translate("LoginForm", "aprs_py"))
        self.user_line.setPlaceholderText(_translate("LoginForm", "postgres"))
        self.pass_line.setPlaceholderText(_translate("LoginForm", "root"))
        self.connectButton.setText(_translate("LoginForm", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())