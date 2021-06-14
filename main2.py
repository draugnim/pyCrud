# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\srdjan.vucic\PycharmProjects\pyCRUD\main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebChannel
from PyQt5.Qt import QStyledItemDelegate
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog
from shapely import wkb, wkt
import folium
import io



class Ui_RadioSondes(object):

    def setupUi(self, RadioSondes):
        self.centerCoord = (44.071800, 17.578125)

        RadioSondes.setObjectName("RadioSondes")
        RadioSondes.resize(828, 605)
        RadioSondes.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(RadioSondes)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")


        self.webView = QWebEngineView(self.splitter)
        self.webView.load(QtCore.QUrl('file:/index.html'))

           # setHtml(self.data.getvalue().decode())
        self.webView.setObjectName("webView")


        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.removeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeButton.setFixedSize(QtCore.QSize(20, 20))
        #self.removeButton.setMinimumSize(20, 20)
        self.removeButton.setObjectName("removeButton")
        self.removeButton.setText("Remove")
        self.horizontalLayout.addWidget(self.removeButton, 0, 0)
        self.addButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addButton.setFixedSize(QtCore.QSize(20, 20))
        #self.addButton.setMinimumSize(QtCore.QSize(20, 20))
        self.addButton.setObjectName("addButton")
        self.addButton.setText("Add")
        self.horizontalLayout.addWidget(self.addButton, 0, 1)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 0, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabView = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.verticalLayout_2.addWidget(self.tabView)

        self.tableView_2 = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableView_2.verticalHeader().sectionClicked.connect(self.findMrker)
        self.tableView_2.setItemDelegate(ValidatedItemDelegate())

        self.tableView_3 = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView_3.setObjectName("tableView_3")
        self.tableView_3.verticalHeader().setCascadingSectionResizes(False)

        self.tabView.addTab(self.tableView_2, "APRS Object")
        self.tabView.addTab(self.tableView_3, "Metadata")

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        RadioSondes.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(RadioSondes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 21))
        self.menubar.setObjectName("menubar")

        self.menuConnect = QtWidgets.QMenu(self.menubar)
        self.menuConnect.setObjectName("menuConnect")

        self.menuMap = QtWidgets.QMenu(self.menubar)
        self.menuMap.setObjectName("menuMap")

        RadioSondes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RadioSondes)
        self.statusbar.setObjectName("statusbar")
        RadioSondes.setStatusBar(self.statusbar)

        self.actionNew_DB_Connection = QtWidgets.QAction(RadioSondes)
        self.actionNew_DB_Connection.setObjectName("actionNew_DB_Connection")
        self.menuConnect.addAction(self.actionNew_DB_Connection)
        self.menubar.addAction(self.menuConnect.menuAction())

        self.toggleCluster = QtWidgets.QAction(RadioSondes)
        self.toggleCluster.setObjectName("toggleCluster")
        self.menuMap.addAction(self.toggleCluster)
        self.menubar.addAction(self.menuMap.menuAction())
        self.toggleCluster.triggered.connect(self.toggleMarkerCluster)

        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 0)

        self.retranslateUi(RadioSondes)
        QtCore.QMetaObject.connectSlotsByName(RadioSondes)

    def retranslateUi(self, RadioSondes):
        _translate = QtCore.QCoreApplication.translate
        RadioSondes.setWindowTitle(_translate("RadioSondes", "Radio Sondes Tracker"))
        self.menuConnect.setTitle(_translate("RadioSondes", "Connect"))
        self.menuMap.setTitle(_translate("RadioSondes", "Map"))
        self.actionNew_DB_Connection.setText(_translate("RadioSondes", "New DB Connection"))
        self.toggleCluster.setText(_translate("RadioSondes", "Marker Cluster Toggle"))

    def initMap(self, model):
        markerLst = []
        for n in range(0, model.rowCount()):
            name = model.record(n).value("name")
            wkbGeom = model.record(n).value("geometry")
            point = wkb.loads(wkbGeom, hex=True)
            markerGeometry = [point.xy[1][0], point.xy[0][0]]
            marker = {'name': name,
                      'index': n,
                      'geometry': markerGeometry}
            markerLst.append(marker)
        page = self.webView.page()
        page.runJavaScript('testJs({})'.format(markerLst))

    def toggleMarkerCluster(self):
        page = self.webView.page()
        page.runJavaScript('toggleCluster()')

    def findMrker(self, index):
        page = self.webView.page()
        page.runJavaScript('findMarker({})'.format(index))



class ValidatedItemDelegate(QStyledItemDelegate):
    def createEditor(self, widget, option, index):
        if not index.isValid():
            return 0
        if index.column() == 0: #only on the cells in the first column
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('[\w]{1,10}'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 2:
            editor = QtWidgets.QSpinBox(widget)
            editor.setMaximum(360)
            editor.setMinimum(1)
            return editor
        if index.column() == 3:
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('[1-9][0-9]{0,2}'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 4:
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('.{2}'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 5:
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('^(?=.{1,8}$)((\w)+-?(\w)+(-?(\w))*)+$'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 6:
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('^(?=.{1,8}$)((\w)+-?(\w)+(-?(\w))*)+$'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 7:
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('.{0,150}'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 8:
            editor = QtWidgets.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('^(?=.{1,8}$)((\w)+-?(\w)+(-?(\w))*)+$'), editor)
            editor.setValidator(validator)
            return editor
        if index.column() == 9:
            self.form = QtWidgets.QWidget()
            self.formLayout = QtWidgets.QFormLayout(self.form)
            self.formLayout.setVerticalSpacing(12)
            self.formLayout.setObjectName("formLayout")
            ###__________ Latitude__________###
            self.latLabel = QtWidgets.QLabel(self.form)
            self.latLabel.setObjectName("latLabel")
            self.latLabel.setText("Latitude")
            self.latLabel.adjustSize()
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.latLabel)
            self.latEdit = QtWidgets.QLineEdit(self.form)
            # lineEdit.textChanged.connect(validateFields)
            self.latEdit.setObjectName("latEdit")
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.latEdit)
            ###__________ Longitude__________###
            self.lngLabel = QtWidgets.QLabel(self.form)
            self.lngLabel.setObjectName("lngLabel")
            self.lngLabel.setText("Longitude")
            self.lngLabel.adjustSize()
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lngLabel)
            self.lngEdit = QtWidgets.QLineEdit(self.form)
            # lineEdit.textChanged.connect(validateFields)
            self.lngEdit.setObjectName("lngEdit")
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lngEdit)
            ###__________ Elevation__________###
            self.elevationLabel = QtWidgets.QLabel(self.form)
            self.elevationLabel.setObjectName("elevationLabel")
            self.elevationLabel.setText("Elevation")
            self.elevationLabel.adjustSize()
            self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.elevationLabel)
            self.elevationEdit = QtWidgets.QLineEdit(self.form)
            # lineEdit.textChanged.connect(validateFields)
            self.elevationEdit.setObjectName("elevationEdit")
            self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.elevationEdit)

            self.buttonBox = QtWidgets.QDialogButtonBox(self.form)
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")
            self.formLayout.addWidget(self.buttonBox)

            self.form.resize(200, 300)

            self.prevData = index.data()
            self.index = index
            self.widget = widget

            self.model = self.widget.parent().parent().parent().parent().parent().parent().parent().objModel

            data = self.model.data(self.index)
            geomWkb = wkb.loads(bytes.fromhex(data))
            self.latEdit.setText(str(geomWkb.x))
            self.lngEdit.setText(str(geomWkb.y))
            self.elevationEdit.setText(str(geomWkb.z))

            self.buttonBox.accepted.connect(self.generateGeom)
            self.buttonBox.rejected.connect(self.cancelGeomEdit)
            return self.form
        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)

    def generateGeom(self):
        print(self.latEdit.text())
        print(self.lngEdit.text())
        print(self.elevationEdit.text())

        geomStr = "POINT Z (" + self.latEdit.text() + " " + self.lngEdit.text() + " " + self.elevationEdit.text() + ")"
        geom = wkt.loads(geomStr)
        geomWkb = wkb.dumps(geom, hex=True, srid=4326)

        self.model.setData(self.index, geomWkb)

        print("lalala")

    def cancelGeomEdit(self):
        self.form.destroy(destroyWindow=True)