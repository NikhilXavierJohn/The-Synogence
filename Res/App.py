from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from pytube import YouTube
import os
import subprocess
import time
import speech_recognition as sr


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        MainWindow.setStyleSheet("background-image: url(:/Background/Ui_Background.png);\n"
"\n"
"\n"
"\n"
"")
        self.command=""
        self.title=""
        self.fileName=""
        self.newTitle=""
        self.yt=None
        self.transcribe=None
        self.stream=None
        self.audiofile=None
        self.msg=QMessageBox()
        self.splitcommand="sox /home/nikhil/Nefarians/UI/Res/audio/out.wav /home/nikhil/Nefarians/UI/Res/split/split.wav silence 1 0.5 1% 1 1.5 1% : newfile : restart"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.videoname=""
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QFrame(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(60, 20, 181, 181))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("image: url(:/Logo/synogence logo_text.png);\n"
"background-image: url(:/Logo/synogence logo_text.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setObjectName("logo")
        self.urltext = QtWidgets.QLabel(self.centralwidget)
        self.urltext.setGeometry(QtCore.QRect(560, 210, 261, 71))
        self.urltext.setStyleSheet("background-image: url(:/Logo/synogence logo_text.png);\n"
"font: italic 40pt \"Visionary Stairs\" ;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.urltext.setTextFormat(QtCore.Qt.PlainText)
        self.urltext.setAlignment(QtCore.Qt.AlignCenter)
        self.urltext.setObjectName("urltext")
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(382, 320, 551, 26))
        self.url.setStyleSheet("border:1px solid black;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"color:white;\n"
"font: 15pt \"FreeMono\";")
        self.url.setText("")
        self.url.setObjectName("url")
        self.downloadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadbutton.setGeometry(QtCore.QRect(960, 320, 91, 26))
        self.downloadbutton.setStyleSheet("border-radius:10px;\n"
"font: 11pt \"Visionary Stairs\";\n"
"color: rgb(255, 255, 255);")
        self.downloadbutton.setObjectName("downloadbutton")
        self.downloadbutton.clicked.connect(self.downloadnow)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 410, 551, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("\n"
"QProgressBar:horizontal {\n"
"border: 3px ;\n"
"background: rgb(105,105,105,70%);\n"
"padding: 1px;\n"
"text-align:center;\n"
"border-radius: 10px;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightgray, stop: 1 white);\n"
"}\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.downloadtext = QtWidgets.QLabel(self.centralwidget)
        self.downloadtext.setGeometry(QtCore.QRect(580, 470, 211, 61))
        self.downloadtext.setStyleSheet("font: 40pt \"Visionary Stairs\";\n"
"text-align:center;\n"
"color:white;\n"
"background-image: url(:/Logo/synogence logo_text.png);")
        self.downloadtext.setObjectName("downloadtext")
        self.link = QtWidgets.QLineEdit(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(380, 560, 551, 26))
        self.link.setStyleSheet("border:1px solid black;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"color:white;\n"
"font: 15pt \"FreeMono\";")
        self.link.setText("")
        self.link.setObjectName("link")
        self.browsebutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsebutton.setGeometry(QtCore.QRect(960, 560, 95, 26))
        self.browsebutton.setStyleSheet("border-radius:10px;\n"
"font: 11pt \"Visionary Stairs\";\n"
"color: rgb(255, 255, 255);")
        self.browsebutton.setObjectName("browsebutton")
        self.browsebutton.clicked.connect(self.openfiledialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.urltext.setText(_translate("MainWindow", "URL"))
        self.downloadbutton.setText(_translate("MainWindow", "DOWNLOAD"))
        self.downloadtext.setText(_translate("MainWindow", "Browse"))
        self.browsebutton.setText(_translate("MainWindow", "Browse"))

    def progress_Check(self,stream = None, chunk = None, file_handle = None, remaining = None):
        percent = (100*(file_size-remaining))/file_size
        self.progressBar.setProperty("value", percent)

    def downloadnow(self):
        self.yt = YouTube(str(self.url.text()))
        self.title=self.yt.title
        self.yt.register_on_progress_callback(self.return_progress)
        self.stream=self.yt.streams.filter(subtype='mp4').first()
        # self.videoname= self.stream.default_filename
        #print(self.videoname)
        self.stream.download("/home/nikhil/Nefarians/UI/Res/videos",filename="video")
        self.progressBar.setValue(0)
        self.newTitle="video.mp4"
        #os.rename("/home/nikhil/Nefarians/UI/Res/videos/"+self.title+".mp4","/home/nikhil/Nefarians/UI/Res/videos/"+self.newTitle)
        self.command="ffmpeg -i /home/nikhil/Nefarians/UI/Res/videos/video.mp4 -ab 160k -ac 2 -ar 44100 -vn /home/nikhil/Nefarians/UI/Res/audio/out.wav"
        # self.url.setText("")
        self.converter()
        # print("file has been successfully downloaded")
    
    def return_progress(self, stream, chunk, file_handle, bytes_remaining):
        percentage = (1 - bytes_remaining / self.stream.filesize)*100
        self.progressBar.setValue(percentage)
        if(percentage==100):
            
            self.msg.setWindowTitle("Synogence")
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Downloaded "+self.title)
            self.msg.exec_()

    def splitter(self):
        subprocess.call(self.splitcommand,shell=True)
        self.msg.setText("Removed Silences")
        self.msg.exec_()
        files=os.listdir("/home/nikhil/Nefarians/UI/Res/split/")
        for i in files:
            self.splitcommand="ffmpeg -i /home/nikhil/Nefarians/UI/Res/split/"+i+ " -f segment -segment_time 30 -c copy /home/nikhil/Nefarians/UI/Res/split/out%03d.wav"
            subprocess.call(self.splitcommand,shell=True)
        self.msg.setText("Audio Split Every 30 Seconds")
        self.msg.exec_()
        for f in files:
            if(f.startswith("split")):
                print("removing: /home/nikhil/Nefarians/UI/Res/split/"+f)
                os.remove("/home/nikhil/Nefarians/UI/Res/split/"+f)
        self.msg.setText("Starting Transcription")
        self.msg.exec_()
        self.transcriber()

    def transcriber(self):
        import transcribefast
        self.msg.setText("Transcription Done")
        self.msg.exec_()
        self.msg.setText("Summarising And Categorizing Transcript")
        self.msg.exec_()
        import Summcategorise
        self.msg.setText("Output Generated ")
        self.msg.exec_()
        import prediction
        self.msg.setText("Click Ok to Display Output")
        self.msg.exec_()
        subprocess.call("python3 -W ignore Outputwindow.py",shell=True)


    def converter(self):
        subprocess.call(self.command, shell=True)
        self.msg.setText("Converted To WAV!")
        self.msg.exec_()
        self.splitter()
        


    def openfiledialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            self.link.setText(self.fileName)
            if(self.fileName.endswith(".wav")):
                if(os.path.isfile("/home/nikhil/Nefarians/UI/Res/audio/out.wav")):
                    subprocess.call("sudo rm /home/nikhil/Nefarians/UI/Res/audio/out.wav",shell=True)
                os.rename(self.fileName,"/home/nikhil/Nefarians/UI/Res/audio/out.wav")
                time.sleep(2)
            elif(self.fileName.endswith(".mp4")):
                if(os.path.isfile("/home/nikhil/Nefarians/UI/Res/videos/video.mp4")):
                    subprocess.call("sudo rm /home/nikhil/Nefarians/UI/Res/videos/video.mp4",shell=True)
                os.rename(self.fileName,"/home/nikhil/Nefarians/UI/Res/videos/video.mp4")
                time.sleep(2)
                self.converter()
            else:
                self.msg.setText("Invalid or Unsupported file type")
                self.msg.exec_()

import Background

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())