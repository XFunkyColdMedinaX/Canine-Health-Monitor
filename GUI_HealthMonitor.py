from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage

class WorkerThread(QThread):
    # Define a signal to update the label with the current value
    update_label = pyqtSignal(str)
    filepath ="C:\\Users\\josea\\Desktop\\joey\\"
    def __init__(self):
        QThread.__init__(self)

    def openDataFile(self):
        with open(self.filepath + "denny2.txt", "r") as f:
            self.lines = f.readlines()

    def process(self):
        for line in self.lines:
            self.update_label.emit(line)
            self.sleep(1)

    def run(self):
        # Perform a time-consuming task
        self.openDataFile()
        self.process()

class Ui_MainWindow(object):
    yplot = []
    xplotStart = 0
    xplotFinish = 10
    xplotIncrement = 10
    plotZize = 10
    tempHighC = 40; templowC = 37.2; tempRange = 0
    ECGHigh = 160; ECGLow = 70; ECGRange = 0
    #SpO2High = 100; SpO2Low = 97; SpO2Range = 0
    SpO2High = 300; SpO2Low = 220; SpO2Range = 0
    count = 0
    tempC = "0"
    tempF = "0"
    temp = "0"
    tempDeg = ["°C", "°F"]
    fontColor = ["color: green;", "color: red;"]
    SpO2 = '0 SpO2'
    ECG = '0 ECG'
    BMP = 'BMP'; BMPHigh = 160; BMPLow = 70; BMPRange = 0
    sensor_data = ''
    filepath = "C:\\Users\\josea\\Desktop\\joey\\"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 867)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(49, 579, 191, 101))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 119, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 119, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 50, 80, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 320, 62, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 410, 251, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 410, 104, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)

        self.label_4.setGeometry(QtCore.QRect(449, 529, 251, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 530, 184, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 320, 251, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(360, 10, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 841, 221))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Temperature"))
        self.radioButton.setText(_translate("MainWindow", "Farenheit"))
        self.radioButton_2.setText(_translate("MainWindow", "Celsius"))
        self.label_5.setText(_translate("MainWindow", "ECG"))
        self.label_6.setText(_translate("MainWindow", "BPM"))
        self.label_2.setText(_translate("MainWindow", "o"))
        self.label.setText(_translate("MainWindow", "SpO2"))
        self.label_4.setText(_translate("MainWindow", "tmp"))
        self.label_3.setText(_translate("MainWindow", "Temperature"))
        self.label_7.setText(_translate("MainWindow", "o"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        #self.label_8.setPixmap(QtGui.QPixmap('ekg-clipart-gif-transparent-4.gif'))
        self.label_8.setPixmap(QtGui.QPixmap('ecg.jpg'))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.thread = WorkerThread()
        self.thread.update_label.connect(self.main_process)

    def main_process(self, text):
        self.checkData(text)
        self.ECGgraphic(text)
        self.update_GUI(text)

    def ECGgraphic(self, text):
        self.yplot.append(int(self.ECG))
        while(len(self.yplot) >= self.xplotIncrement):
            self.figure = Figure()
            self.canvas = FigureCanvas(self.figure)
            #self.setCentralWidget(self.canvas)
            self.axes = self.figure.add_subplot(111)
            # Generate some data for the ECG graph
            x = np.linspace(self.xplotStart, self.xplotFinish, self.xplotIncrement)
            y = self.yplot
            print('xplotStart= ' + str(self.xplotStart))
            print('xpltfinish = ' + str(self.xplotFinish))
            print('x= ' + str(x))
            print('y= ' + str(y))
            self.axes.plot(x, y)

            buf, size = self.canvas.print_to_buffer()
            qimage = QImage.rgbSwapped(QImage(buf, size[0], size[1], QImage.Format_RGBA8888))
            pixmap = QPixmap(qimage)

            self.label_8.setPixmap(pixmap)
            #self.setCentralWidget(self.label)
            #self.label_8.setPixmap(QtGui.QPixmap(self.axes.plot(x, y)))

            self.yplot = []
            self.xplotStart += self.xplotIncrement
            self.xplotFinish += self.xplotIncrement

    def start_task(self):
        self.thread.start()

        #self.myarduinothread.start()


    def update_GUI(self, text):
        self.label_4.setStyleSheet(self.fontColor[self.tempRange])
        if self.radioButton.isChecked():
            self.label_4.setText(str(self.tempF) + self.tempDeg[1])
        else:
            self.label_4.setText(str(self.tempC) + self.tempDeg[0])

        self.label_7.setStyleSheet(self.fontColor[self.BMPRange])
        self.label_7.setText(str(self.BMP))

        self.label_2.setStyleSheet(self.fontColor[self.SpO2Range])
        self.label_2.setText(str(self.SpO2))
        self.statusbar.showMessage(text)

    def checkData(self, data):
        sensor_data = data.split(",")
        # Check the length of the sensor data
        if len(sensor_data) > 0 and sensor_data[0] != '':
            self.tempC = sensor_data[0][:-2]
            self.tempF = sensor_data[1][:-2]
            if self.isfloat(self.tempC):
                self.tempRange = self.checkinRange(self.tempHighC, self.templowC, float(self.tempC))
            #BMP Check
            self.BMP = sensor_data[2][:-1]
            if self.isfloat(self.BMP):
                self.BMPRange = self.checkinRange(self.BMPHigh, self.BMPLow, float(self.BMP))
            #OpO2
            self.SpO2 = sensor_data[2][:-1]
            if self.isfloat(self.SpO2):
                self.SpO2Range = self.checkinRange(self.SpO2High, self.SpO2Low, float(self.SpO2))
            #ECG
            self.ECG = sensor_data[2][:-1]
            if self.isfloat(self.ECG):
                #self.SpO2Range = self.checkinRange(self.SpO2High, self.SpO2Low, float(self.SpO2))
                pass


    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def checkinRange(self, high, low, read):
        if read < high and read > low:
            return 0
        else:
            return -1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.start_task()
    sys.exit(app.exec_())

    '''

    def create_canvas(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)
        self.axes = self.figure.add_subplot(111)
        # Generate some data for the ECG graph
        x = np.linspace(0, 10, 10)

        print(str(np.linspace(0, 10, 10)))
        y = [20,100,30,90,20,90,30,100,90,10]

        self.axes.plot(x, y)'''
