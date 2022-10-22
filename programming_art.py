import PyQt5
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QColorDialog,QApplication, QWidget,QMainWindow, QHBoxLayout, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor




class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainWindow.ui",self)
        self.setWindowTitle("Programming Art")
        self.setGeometry(0,0,800,800)
        # self.frame.setGeometry(0,0,400,400)
        # self.label_repeat.setGeometry(30,20,160,40)
        # self.repeat_times.setGeometry(250,20,75,40)

        # select color 
        self.color = QColor(255,0,0)
        self.color_button.setStyleSheet('* { background-color: '+ self.color.name() + ' }')
        self.sample.setStyleSheet('* { background-color: '+ self.color.name() + ' }')
        self.color_button.clicked.connect(self.color_picker)
        self.on_slide()
        self.on_dial()
        self.width_slider.valueChanged.connect(self.on_slide)
        self.length_slider.valueChanged.connect(self.on_slide)
        self.angle_dial.valueChanged.connect(self.on_dial)


        # 
    def color_picker(self):
        self.color = QColorDialog.getColor()
        self.color_button.setStyleSheet('* { background-color: '+ self.color.name() + ' }')
        self.sample.setStyleSheet('* { background-color: '+ self.color.name() + ' }')

    def on_slide(self):
        self.myWidth = self.width_slider.value()
        self.myLength=self.length_slider.value()
        self.sample.setGeometry(30,440,self.myLength,self.myWidth)
    
    def on_dial(self):
        self.myAngle=self.angle_dial.value()
        

if __name__ == '__main__':
    app=QApplication(sys.argv)

    app.setStyleSheet('''
        QWidget{
            font-size : 30px
        }

    ''')

    myApp = MyApp()

    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("system Exit")

