from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(768, 588)
        Form.setMinimumSize(QtCore.QSize(768, 588))
        Form.setMaximumSize(QtCore.QSize(768, 588))
        Form.setStyleSheet("background-image: url(:/Background/Ui_Background.png);")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(260, 10, 221, 181))
        self.graphicsView.setStyleSheet("background-image: url(:/Logo/synogence logo_text.png);\n"
"border-image: url(:/Logo/synogence logo_text.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.TranscribedText = QtWidgets.QTextBrowser(Form)
        self.TranscribedText.setGeometry(QtCore.QRect(40, 190, 681, 192))
        self.TranscribedText.setStyleSheet("font: 11pt \"FreeMono\";\n"
"color: rgb(255, 255, 255);")
        self.TranscribedText.setObjectName("TranscribedText")
        self.Transcribedlabel = QtWidgets.QLabel(Form)
        self.Transcribedlabel.setGeometry(QtCore.QRect(190, 160, 381, 20))
        self.Transcribedlabel.setStyleSheet("font: 30pt \"Visionary Stairs\";\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/Logo/synogence logo_text.png);")
        self.Transcribedlabel.setObjectName("Transcribedlabel")
        self.headinglabel = QtWidgets.QLabel(Form)
        self.headinglabel.setGeometry(QtCore.QRect(160, 390, 441, 20))
        self.headinglabel.setStyleSheet("font: 30pt \"Visionary Stairs\";\n"
"color: rgb(255, 255, 255);")
        self.headinglabel.setObjectName("headinglabel")
        self.Headline = QtWidgets.QTextBrowser(Form)
        self.Headline.setGeometry(QtCore.QRect(40, 420, 681, 111))
        self.Headline.setStyleSheet("font: italic 11pt \"FreeMono\";\n"
"color: rgb(255, 255, 255);")
        self.Headline.setObjectName("Headline")
        self.category = QtWidgets.QTextBrowser(Form)
        self.category.setGeometry(QtCore.QRect(250, 550, 256, 31))
        self.category.setStyleSheet("font: italic 11pt \"FreeMono\";\n"
"color: rgb(255, 255, 255);")
        self.category.setObjectName("category")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 550, 201, 31))
        self.label.setStyleSheet("font: 30pt \"Visionary Stairs\";\n"
"background-image: url(:/Logo/synogence logo_text.png);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.fake = QtWidgets.QTextBrowser(Form)
        self.fake.setGeometry(QtCore.QRect(520, 550, 191, 31))
        self.fake.setStyleSheet("font: 11pt \"FreeMono\";\n"
"color: rgb(255, 255, 255);")
        self.fake.setObjectName("fake")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Transcribedlabel.setText(_translate("Form", "Transcribed text"))
        self.headinglabel.setText(_translate("Form", "Summarised Headline"))
        self.label.setText(_translate("Form", "Category"))
        Category=open("fakenews.txt","r")
        Tfiles=open("transcript.txt","r")
        Sfiles=open("summary.txt","r")
        fakes=open("predictionfile.txt","r")
        fakees=fakes.readlines()
        tText=Tfiles.readlines()
        sText=Sfiles.readlines()
        cat=Category.readlines()
        self.category.setText(str(cat[0]))
        self.TranscribedText.setText(str(tText))
        self.Headline.setText(str(sText))
        self.fake.setText(str(fakees[0]))
        Category.close()
        Tfiles.close()
        Sfiles.close()
        fakes.close()
import Background

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())