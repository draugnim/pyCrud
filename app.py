import sys, os
import PyQt5
from datetime import datetime
from shapely import wkb, wkt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QErrorMessage, QHeaderView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import Qt, QtCore, QtWebChannel
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from login_dialog import Ui_Dialog
from main2 import Ui_RadioSondes
from addObj import Ui_addObj
import qdarkstyle

os.environ['QT_DEBUG_PLUGINS'] = "1"

class MainWindow(QMainWindow, Ui_RadioSondes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ================= Web Channel ===================
        self.channel = QtWebChannel.QWebChannel()
        self.handler = self
        self.channel.registerObject('handler', self.handler)
        self.webView.page().setWebChannel(self.channel)

        # ================= Listeners ===================
        self.actionNew_DB_Connection.triggered.connect(self.exLogin)
        self.removeButton.clicked.connect(self.removeRows)
        self.addButton.clicked.connect(self.addRows)
        # ============================================
        self.db = QSqlDatabase.addDatabase("QPSQL", "db")
        self.dbDriver = "QPSQL"
        self.dbHostName = None
        self.dbPort = None
        self.dbDatabaseName = None
        self.dbUserName = None
        self.dbPassword = None
        self.conn = None

        self.objModel = QSqlTableModel(self, self.db)
        self.metaModel = None


    @QtCore.pyqtSlot(str)
    def markerClicked(self, markerIndex):
        self.tableView_2.selectRow(int(markerIndex))

    # ================= Events ===================
    def removeRows(self):
        print(self.tableView_2.selectionModel().selectedRows())

    def addRows(self):
        curIndex = self.tabView.currentIndex()
        dbOpen = self.db.isOpen()
        print(dbOpen)
        print(curIndex)
        if not dbOpen:
            print("jeste")
            err_dialog = QErrorMessage(parent=self)
            err_dialog.setWindowModality(Qt.WindowModal)
            err_dialog.showMessage('Not connected to database!')
        else:
            if (curIndex == 0):
                self.addObjWin = addObjDialog()

                self.addObjWin.comboBox.setModel(self.metaModel)
                self.addObjWin.comboBox.setModelColumn(self.metaModel.fieldIndex("tag"))

                if self.addObjWin.exec_() == QDialog.Accepted:
                    if (self.addObjWin.lineEdit.text() and self.addObjWin.lineEdit_10.text() and self.addObjWin.lineEdit_11.text() and self.addObjWin.lineEdit_12.text()):
                        geomStr = "POINT Z (" + self.addObjWin.lineEdit_10.text() + " " + self.addObjWin.lineEdit_11.text() + " " + self.addObjWin.lineEdit_12.text() + ")"
                        geom = wkt.loads(geomStr)
                        geomWkb = wkb.dumps(geom, hex=True, srid=4326)
                        insertValues = [self.addObjWin.lineEdit.text(), self.addObjWin.dateTimeEdit.text(),
                                        self.addObjWin.lineEdit_3.text(), self.addObjWin.lineEdit_4.text(),
                                        self.addObjWin.lineEdit_5.text(), self.addObjWin.lineEdit_6.text(),
                                        self.addObjWin.lineEdit_7.text(), self.addObjWin.lineEdit_8.text(),
                                        self.addObjWin.lineEdit_9.text(), geomWkb, '1']
                        print(geom)
                        self.insertDb(insertValues)
                    else:
                        print("nema")

    def insertDb(self, values):
        r = self.createRecord(values)
        for i in range(0,11):
            print("Vrijednost: " + r.value(i))
        try:
            inserted = self.objModel.insertRecord(-1, r)
            print(inserted)
            print(self.objModel.lastError().text())
        except(Exception) as error:
            print("Doslo je do greske prilikom dodavanja objekta u bazu: " + error)

    def createRecord(self, paramList):
        r = self.objModel.record()
        for x in range(0, 11):
            print('index: ' + str(x))
            try:
                r.setValue(x, paramList[x])
            except(Exception) as error:
                print(error)
            print('Parametar: ' + paramList[x])
        return r

    def exLogin(self):
        self.window = LoginDialog()
        self.window.host_line.insert("127.0.0.1")
        self.window.port_line.insert("5432")
        self.window.db_line.insert("aprs_py")
        self.window.user_line.insert("postgres")
        self.window.pass_line.insert("root")
        self.window.exec_()

    def setConn(self, conName):
        # Set up the model
        self.objModel.setTable("aprsobj")
        self.objModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.objModel.setHeaderData(0, Qt.Horizontal, "Name")
        self.objModel.setHeaderData(1, Qt.Horizontal, "Time")
        self.objModel.setHeaderData(2, Qt.Horizontal, "Coursse")
        self.objModel.setHeaderData(3, Qt.Horizontal, "Speed")
        self.objModel.setHeaderData(4, Qt.Horizontal, "Symbol")
        self.objModel.setHeaderData(5, Qt.Horizontal, "Source call")
        self.objModel.setHeaderData(6, Qt.Horizontal, "Dest call")
        self.objModel.setHeaderData(7, Qt.Horizontal, "Comment")
        self.objModel.setHeaderData(8, Qt.Horizontal, "Path")
        self.objModel.setHeaderData(9, Qt.Horizontal, "Geometry")
        self.objModel.setHeaderData(10, Qt.Horizontal, "Metadata")
        self.objModel.select()

        self.metaModel = QSqlTableModel(self, self.db)
        self.metaModel.setTable("metadata")
        self.metaModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.metaModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.metaModel.setHeaderData(1, Qt.Horizontal, "Time")
        self.metaModel.setHeaderData(2, Qt.Horizontal, "Tag")
        self.metaModel.select()

        ## Set up the views
        self.tableView_2.setModel(self.objModel)
        self.tableView_3.setModel(self.metaModel)

        for i in range(11):
            self.tableView_2.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        for i in range(3):
            self.tableView_3.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        self.initMap(self.objModel)


class addObjDialog(QDialog, Ui_addObj):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        btn = self.connectButton
        btn.clicked.connect(self.con2Db)

    def con2Db(self):
        hostName = self.host_line.text()
        port = self.port_line.text()
        dbName = self.db_line.text()
        userName = self.user_line.text()
        password = self.pass_line.text()

        if "" not in (hostName, port, dbName, userName, password):
            ex.dbHostName = hostName
            ex.dbPort = int(port)
            ex.dbDatabaseName = dbName
            ex.dbUserName = userName
            ex.dbPassword = password

            ex.db.setHostName(ex.dbHostName)
            ex.db.setPort(ex.dbPort)
            ex.db.setDatabaseName(ex.dbDatabaseName)
            ex.db.setUserName(ex.dbUserName)
            ex.db.setPassword(ex.dbPassword)

            dbOpen = ex.db.open()

            if dbOpen:
                ex.setConn("db")
                self.accept()
            else:
                print("Error while connecting to PostgreSQL", ex.db.lastError())
                # err_msg = QMessageBox.critical(parent=self.window())
                err_dialog = QErrorMessage(parent=self.window())
                err_dialog.setWindowModality(Qt.WindowModal)
                err_dialog.showMessage('Unable to connecto to database!')
        else:
            err_dialog = QErrorMessage(parent=self.window())
            err_dialog.setWindowModality(Qt.WindowModal)
            err_dialog.showMessage('Missing input!')


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value

            # Default (anything not captured above: e.g. int)
            return value

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class CallHandler(QtCore.QObject):
    @QtCore.pyqtSlot(str)
    def testChannel(self, markerName):
        print("stigo poziv 2")
        print("Marker : " + markerName)
        self.mainWin = MainWindow()

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())