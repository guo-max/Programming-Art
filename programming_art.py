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
        # self.setCentralWidget(self.Art)

        self.startButton.clicked.connect(self.draw_art)

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
        print(self.myAngle)
        
    def draw_art(self):
        self.Art.pixmap().fill()
        self.repeat = self.repeat_times.value()
     
        start_point = QPoint(100,100)
        theta = 0
        for i in range (0,self.repeat):
            painter = QtGui.QPainter(self.Art.pixmap())
            pen = QtGui.QPen()
            pen.setWidth(self.myWidth)
            pen.setColor(self.color)
            painter.setPen(pen)
            x = start_point.x() + int(self.myLength*np.cos(theta))
            y = start_point.y() + int(self.myLength*np.sin(theta))
            stop_point=QPoint(x,y)
            painter.drawLine(start_point,stop_point)
            start_point = stop_point
            theta=theta+self.myAngle/180*np.pi
            painter.end()
            self.Art.update()
            QCoreApplication.processEvents()
            time.sleep(0.07)



        

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

