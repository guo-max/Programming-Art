import PyQt5
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QColorDialog,QApplication, QWidget,QMainWindow, QHBoxLayout, QVBoxLayout, QDialog
from PyQt5.QtCore import QLine,QPoint,QCoreApplication
from PyQt5.QtGui import QColor
import numpy as np
import time




class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainWindow.ui",self)
        self.setWindowTitle("Programming Art")
        self.setGeometry(0,0,1200,800)

        #repeat 
        self.repeat = self.repeat_times.value()

        # select color 
        self.color = QColor(255,0,0)
        self.color_button.setStyleSheet('* { background-color: '+ self.color.name() + ' }')
        self.sample.setStyleSheet('* { background-color: '+ self.color.name() + ' }')
        self.color_button.clicked.connect(self.color_picker)

        # length, width, angle selection
        self.on_slide()
        self.on_dial()
        self.width_slider.valueChanged.connect(self.on_slide)
        self.length_slider.valueChanged.connect(self.on_slide)
        self.angle_dial.valueChanged.connect(self.on_dial)


        # 
        self.canvas = QtGui.QPixmap(450, 450)
        self.Art.setPixmap(self.canvas)
        self.startButton.clicked.connect(self.draw_art)

        self.textAngle.textChanged.connect(self.on_angle_text)

        #close function
        self.exitButton.clicked.connect(self.close)

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
        self.textAngle.setText(str(self.myAngle))

    def on_angle_text(self):
        try:
            self.myAngle=int(self.textAngle.toPlainText())
            # self.angle_dial.setValue(self.myAngle)
        except:
            print("number only")
        
    def draw_art(self):
        self.Art.pixmap().fill()
        self.repeat = self.repeat_times.value()

        self.start_x=100.0
        self.start_y=100.0
        self.theta = 0.0
        for i in range (0,self.repeat):
            painter = QtGui.QPainter(self.Art.pixmap())
            pen = QtGui.QPen()
            pen.setWidth(self.myWidth)
            pen.setColor(self.color)
            painter.setPen(pen)

            painter.drawLine(self.get_start_point(),self.get_stop_point())

            painter.end()
            self.Art.update()
            QCoreApplication.processEvents()
            time.sleep(0.07)

    def get_stop_point(self):
        self.stop_x=self.start_x+self.myLength*np.cos(self.theta)
        self.stop_y=self.start_y+self.myLength*np.sin(self.theta)
        self.theta=self.theta+self.myAngle/180.0*np.pi
        self.start_x=self.stop_x
        self.start_y=self.stop_y
        return QPoint(int(self.stop_x),int(self.stop_y))
    
    def get_start_point(self):
        return QPoint(int(self.start_x),int(self.start_y))



        

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

