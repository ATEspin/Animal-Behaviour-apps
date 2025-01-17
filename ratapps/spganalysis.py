import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets, QtGui
import numpy as np
import cv2
import math
import os


VERSION = (0, 2, 0)

class ControlWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.cap = None
        self.filename=None
        self.line1_x=300
        self.line2_x=600
        self.magnification=1
        
        self.resize(400, 800)
        
        self.videoSize = QtWidgets.QComboBox(self)
        self.videoSize.addItem("1X")
        self.videoSize.addItem("1.5X")
        self.videoSize.addItem("2X")
        self.videoSize.addItem("3X")
        self.videoSize.addItem("4X")
        self.videoSize.setCurrentIndex(0)
        self.videoSize.setEnabled(True)
        self.videoSize.activated.connect(self.magnific)
        self.videoSize.setGeometry(QtCore.QRect(675, 30, 50, 20))

        self.LablePath = QtWidgets.QLineEdit(self)
        self.LablePath.setEnabled(False)
        self.LablePath.setGeometry(QtCore.QRect(90, 10, 641, 20))
        self.LablePath.setFrame(False)
        
        self.LableCamera = QtWidgets.QLineEdit(self)
        self.LableCamera.setEnabled(False)
        self.LableCamera.setGeometry(QtCore.QRect(675, 10, 50, 20))
        self.LableCamera.setFrame(False)
        self.LableCamera.setText("Camera:")
        
        self.Camera = QtWidgets.QComboBox(self)
        self.Camera.addItem("Left")
        self.Camera.addItem("Right")
        self.Camera.setEnabled(True)
        self.Camera.setGeometry(QtCore.QRect(675, 30, 50, 20))
        
        self.LableRatL = QtWidgets.QLineEdit(self)
        self.LableRatL.setEnabled(False)
        self.LableRatL.setGeometry(QtCore.QRect(735, 10, 50, 20))
        self.LableRatL.setFrame(False)
        self.LableRatL.setText("Rat L:")
        
        self.LableRat1 = QtWidgets.QLineEdit(self)
        self.LableRat1.setEnabled(True)
        self.LableRat1.setText("0")
        self.LableRat1.setGeometry(QtCore.QRect(735, 30, 40, 20))
        self.LableRat1.setFrame(True)
        
        self.LableRatM = QtWidgets.QLineEdit(self)
        self.LableRatM.setEnabled(False)
        self.LableRatM.setGeometry(QtCore.QRect(785, 10, 50, 20))
        self.LableRatM.setFrame(False)
        self.LableRatM.setText("Rat M:")
        
        self.LableRat2 = QtWidgets.QLineEdit(self)
        self.LableRat2.setEnabled(True)
        self.LableRat2.setText("0")
        self.LableRat2.setGeometry(QtCore.QRect(785, 30, 40, 20))
        self.LableRat2.setFrame(True)
        
        self.LableRatR = QtWidgets.QLineEdit(self)
        self.LableRatR.setEnabled(False)
        self.LableRatR.setGeometry(QtCore.QRect(835, 10, 50, 20))
        self.LableRatR.setFrame(False)
        self.LableRatR.setText("Rat R:")
        
        self.LableRat3 = QtWidgets.QLineEdit(self)
        self.LableRat3.setEnabled(True)
        self.LableRat3.setText("0")
        self.LableRat3.setGeometry(QtCore.QRect(835, 30, 40, 20))
        self.LableRat3.setFrame(True)
        
        self.Table = QtWidgets.QTableWidget(self)
        self.Table.setGeometry(QtCore.QRect(675, 60,235, 560))
        self.Table.setColumnCount(5)
        self.Table.resizeRowsToContents()
#        self.Table.keyPressEvent=self.keyPressEvent
        self.Table.itemClicked.connect(self.tableClick)
#        self.Table.mousePressEvent=self.tableClick
        self.Table.setHorizontalHeaderLabels(["Frame","Time(ms)", "Rat "+self.LableRat1.text(),"Rat "+self.LableRat2.text(),"Rat "+self.LableRat3.text()])
        self.Table.resizeColumnsToContents()
        self.Table.verticalHeader().setVisible(False)
        
        self.TableSumary = QtWidgets.QTableWidget(self)
        self.TableSumary.setGeometry(QtCore.QRect(300, 530,340,110))
        self.TableSumary.setEnabled(False)
        self.TableSumary.setColumnCount(8)
        self.TableSumary.setRowCount(3)
        self.TableSumary.resizeRowsToContents()
        self.TableSumary.setVerticalHeaderLabels(["Rat "+self.LableRat1.text(),"Rat "+self.LableRat2.text(),"Rat "+self.LableRat3.text()])
        self.TableSumary.setHorizontalHeaderLabels(["X0", "T", "K", "D", "S", "I", "Attempts", "Trials"])
        self.TableSumary.resizeColumnsToContents()        
        self.TableSumary.resizeRowsToContents()
        
        for i in range (0, 3):
            for j in range (0,8):
                newitem = QtWidgets.QTableWidgetItem("0")
                self.TableSumary.setItem(i, j, newitem)        
        
        self.open_button = QtWidgets.QPushButton(self)
        self.open_button.setText("Open Video")
        self.open_button.clicked.connect(self.getfile)
        self.open_button.setGeometry(QtCore.QRect(9, 9, 75, 23))
        
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText("Save data")
        self.save_button.clicked.connect(self.handleSave)
        self.save_button.setGeometry(QtCore.QRect(575, 9, 75, 23))
        
        self.play_button = QtWidgets.QPushButton(self)
        self.play_button.setText("Play")
        self.play_button.clicked.connect(self.playBtn)
        self.play_button.setGeometry(QtCore.QRect(9, 530, 75, 23))
        
        self.nplay_button = QtWidgets.QRadioButton(self)
        self.nplay_button.setText("Normal")
        self.nplay_button.setGeometry(QtCore.QRect(90, 530, 75, 23))
        
        self.fplay_button = QtWidgets.QRadioButton(self)
        self.fplay_button.setText("Fast")
        self.fplay_button.setChecked(True)
        self.fplay_button.setGeometry(QtCore.QRect(150, 530, 75, 23))
        
       
        self.LableRat1.textChanged.connect(self.tableHeader)
        self.LableRat2.textChanged.connect(self.tableHeader)
        self.LableRat3.textChanged.connect(self.tableHeader)
               
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        
        layout.addWidget(self.open_button,0,0)
        layout.addWidget(self.videoSize,0,5)
        layout.addWidget(self.LablePath,0,1)
        layout.addWidget(self.save_button,10,5)
        layout.addWidget(self.play_button,10,0)
        layout.addWidget(self.nplay_button,10,1)
        layout.addWidget(self.fplay_button,10,2)
        layout.addWidget(self.LableCamera, 10,3)
        layout.addWidget(self.Camera,10,4)
        layout.addWidget(self.LableRatL,1,0)
        layout.addWidget(self.LableRat1,1,1)
        layout.addWidget(self.LableRatM,1,2)
        layout.addWidget(self.LableRat2,1,3)
        layout.addWidget(self.LableRatR,1,4)
        layout.addWidget(self.LableRat3,1,5)
        layout.addWidget(self.TableSumary,2,0,2,6)
        layout.addWidget(self.Table,4,0,6,6)
        
        self.setWindowTitle('Control Panel')
        self.show()
        
    def startCapture(self):
        if not self.cap:
            if self.filename:
                self.cap = cv2.VideoCapture(str(self.filename))

                if not self.cap.isOpened(): 
                    print("could not open: %s" % self.filename)
#                    self.getfile()
                    return

                self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
                self.fps=self.cap.get(cv2.CAP_PROP_FPS)
                self.fps2=self.fps
#                self.LableFrames.setText("0/"+str(self.length))
                self.Table.setRowCount(self.length)
                
                self.videoFrame=videoWindow(window=self)
                
                for i in range(0, self.length):
                    newitem = QtWidgets.QTableWidgetItem(str(i))
                    self.Table.setItem(i, 0, newitem)
                    
                    newitem = QtWidgets.QTableWidgetItem(str(self.fps*i))
                    self.Table.setItem(i, 1, newitem)
                    
                    for j in range(2, 5):
                       newitem = QtWidgets.QTableWidgetItem("-")
                       self.Table.setItem(i, j, newitem)
                       0
                for i in range(0, 3):
                    for j in range(0,8):
                        newitem = QtWidgets.QTableWidgetItem("0")
                        self.TableSumary.setItem(i, j, newitem) 
                
                
#        ret, frame = self.cap.read()
#        self.videoFrame.video_frame.setGeometry(QtCore.QRect(10, 40, frame.shape[1], frame.shape[0]))
#        self.video_screen.setGeometry(QtCore.QRect(10, 40, frame.shape[1], frame.shape[0]))
#        self.LableFrames.setGeometry(QtCore.QRect(self.video_screen.x()+self.video_screen.width()-100,self.video_screen.y()+self.video_screen.height()-30 , 81, 20))
#        self.LableFrames.setVisible(True)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.nextFrameSlot()

    def endCapture(self):
        #self.stop()
        self.cap.release()
        self.cap = None
        
    def getfile(self):
        if self.cap:
            self.endCapture()
            
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
                        'c:\\',"Video files (*.avi *.mp4 *.MOD)")[0]
        if os.path.exists(filename):
            self.filename = os.path.abspath(filename)
        else:
            return
            
        self.startCapture()
        self.LablePath.setText(self.filename)

    def refresh(self):
        self.nextFrameSlot()
        if (self.play_button.text()=="Stop"):
            self.start()
            
    def magnific(self):
        if self.videoSize.currentText()=='1X':self.magnification=1
        if self.videoSize.currentText()=='1.5X':self.magnification=1.5
        if self.videoSize.currentText()=='2X':self.magnification=2
        if self.videoSize.currentText()=='3X':self.magnification=3
        if self.videoSize.currentText()=='4X':self.magnification=4
        self.nextFrameSlot()
        self.backwards(1)
        
        
    def nextFrameSlot(self):
        nframe = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

        if nframe >= self.length - 1:
            self.stop()
            return

        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame,None,fx=self.magnification, fy=self.magnification, interpolation = cv2.INTER_NEAREST)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.videoFrame.video_frame.setPixmap(pix)
        self.videoFrame.video_screen.resize(frame.shape[1], frame.shape[0])
        self.videoFrame.video_screen.setGeometry(QtCore.QRect(10, 40, frame.shape[1], frame.shape[0]))
        #print("frame: "+str(nframe))
        self.Table.selectRow(nframe)
  
        
    def backwards(self, countBack):
        nframe = self.Table.currentRow() - countBack
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,nframe)
        self.nextFrameSlot() 
                
   
    def playBtn(self):
        if self.fplay_button.isChecked():
            self.fps2=300
        else:
            self.fps2=self.fps
            
        if (self.play_button.text()=="Play"):
            self.start()
        else:
            self.stop()

    def stop(self):
        self.play_button.setText("Play")
        self.timer.stop()

    def start(self):
        self.play_button.setText("Stop")
        self.timer.start(int(1000/ self.fps2))
    
    def openright(self):
        popMenu = QtWidgets.QMenu()
        
        if (self.play_button.text()=="Stop"):
            self.gtn()
            
        popMenu.addAction(QtWidgets.QAction("X0", self,  enabled=True, triggered= self.X0))
        popMenu.addAction(QtWidgets.QAction("T", self,  enabled=True, triggered= self.T))
        popMenu.addAction(QtWidgets.QAction("K", self,  enabled=True,triggered= self.K))
        popMenu.addAction(QtWidgets.QAction("D", self,  enabled=True,triggered= self.D))
        popMenu.addAction(QtWidgets.QAction("S", self,  enabled=True,triggered= self.S))
        popMenu.addAction(QtWidgets.QAction("I", self,  enabled=True,triggered= self.I))
        popMenu.addAction(QtWidgets.QAction("----------", self,  enabled=False)) 
        popMenu.addAction(QtWidgets.QAction("Set Line 1", self,  enabled=True,triggered= self.setLine1))
        popMenu.addAction(QtWidgets.QAction("Set Line 2", self,  enabled=True,triggered= self.setLine2))
        popMenu.addAction(QtWidgets.QAction("----------", self,  enabled=False)) 
        popMenu.addAction(QtWidgets.QAction("Erese", self,  enabled=True, triggered= self.Erese))
        popMenu.exec_(QtWidgets.QCursor.pos())
     
    def keyPressEvent(self, event):          
         key = event.key()
         if key == QtCore.Qt.Key_Up:
             nframe=self.Table.currentRow()+50
             self.cap.set(cv2.CAP_PROP_POS_FRAMES,nframe)
             self.nextFrameSlot()         
         if key == QtCore.Qt.Key_Right:
             self.nextFrameSlot()
         if key == QtCore.Qt.Key_Down:
             self.backwards(52)
         if key == QtCore.Qt.Key_Left:
             self.backwards(2)
         if key == QtCore.Qt.Key_Shift:
             self.playBtn()
        
    def X0(self): self.menuAction("X0")
    def T(self): self.menuAction("T")      
    def K(self): self.menuAction("K")    
    def D(self): self.menuAction("D")     
    def S(self): self.menuAction("S")    
    def I(self): self.menuAction("I")
    def Erese(self): self.menuAction("-")
    
    def setLine1(self, event):
        self.line1_x=self.x
        self.videoFrame.video_screen.update()
#        self.nextFrameSlot()
#        self.backwards(1)
        
    def setLine2(self, event):
        self.line2_x=self.x
        self.videoFrame.video_screen.update()
#        self.nextFrameSlot()
#        self.backwards(1)
    
    def getPos(self , event):
        self.x = event.pos().x()
        self.y = event.pos().y()
               
    def tableClick(self):
        self.cap.set(1,self.Table.currentRow())
        self.refresh()
    
    def tableHeader(self):
        self.Table.setHorizontalHeaderLabels(["Frame","Time (ms)", "Rat "+self.LableRat1.text(),"Rat "+self.LableRat2.text(),"Rat "+self.LableRat3.text()])
        self.TableSumary.setVerticalHeaderLabels(["Rat "+self.LableRat1.text(),"Rat "+self.LableRat2.text(),"Rat "+self.LableRat3.text()])
    
    def menuAction(self, value):
        currentFrame=int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        
        if self.x<=self.line1_x: j=2
        if self.x<=self.line2_x and self.x>=self.line1_x: j=3
        if self.x>=self.line2_x: j=4
            
        olditem=self.Table.item(currentFrame, j).text()
        newitem = QtWidgets.QTableWidgetItem(value)
        self.Table.setItem(currentFrame, j, newitem)
        self.Table.selectRow(currentFrame)
        
        if not olditem==value:
            self.Summary(value, j, 1)
        
        if not olditem=="-":
            if not olditem==value:
                self.Summary(olditem, j,-1)
        
        self.playBtn()
                
    def Summary(self, value, Rat, operator):
        Rat=Rat-2
        suma0=int(self.TableSumary.item(Rat,0).text())
        suma1=int(self.TableSumary.item(Rat,1).text())
        suma2=int(self.TableSumary.item(Rat,2).text())
        suma3=int(self.TableSumary.item(Rat,3).text())
        suma4=int(self.TableSumary.item(Rat,4).text())
        suma5=int(self.TableSumary.item(Rat,5).text())
        suma6=int(self.TableSumary.item(Rat,6).text())
        suma7=int(self.TableSumary.item(Rat,7).text())
        
        if value=="X0":
            suma0=int(self.TableSumary.item(Rat,0).text())+operator
            newitem = QtWidgets.QTableWidgetItem(str(suma0))
            self.TableSumary.setItem(Rat,0, newitem)
        if value=="T":
            suma1=int(self.TableSumary.item(Rat,1).text())+operator
            newitem = QtWidgets.QTableWidgetItem(str(suma1))
            self.TableSumary.setItem(Rat,1, newitem)
        if value=="K":
            suma2=int(self.TableSumary.item(Rat,2).text())+operator
            newitem = QtWidgets.QTableWidgetItem(str(suma2))
            self.TableSumary.setItem(Rat,2, newitem)
        if value=="D":
            suma3=int(self.TableSumary.item(Rat,3).text())+operator
            newitem = QtWidgets.QTableWidgetItem(str(suma3))
            self.TableSumary.setItem(Rat,3, newitem)
        if value=="S":
            suma4=int(self.TableSumary.item(Rat,4).text())+operator
            newitem = QtWidgets.QTableWidgetItem(str(suma4))
            self.TableSumary.setItem(Rat,4, newitem)
        if value=="I":
            suma5=int(self.TableSumary.item(Rat,5).text())+operator
            newitem = QtWidgets.QTableWidgetItem(str(suma5))
            self.TableSumary.setItem(Rat,5, newitem)
        
        suma6=suma0+suma1+suma2+suma3+suma4+suma5
        newitem = QtWidgets.QTableWidgetItem(str(suma6))
        self.TableSumary.setItem(Rat,6, newitem)
        
        suma7=suma2+suma3+suma4+suma5
        newitem = QtWidgets.QTableWidgetItem(str(suma7))
        self.TableSumary.setItem(Rat,7, newitem)
        
    def handleSave(self):
        s = self.filename
        end = s.find(self.filename)-4
        s[0:end]
        filename=s[0:end]
        with open(filename+".txt", "w") as text_file:
            text_file.write("Frame")
            text_file.write("\t")
            text_file.write("Time (ms)")
            text_file.write("\t")
            text_file.write("Rat "+self.LableRat1.text())
            text_file.write("\t")
            text_file.write("Rat "+self.LableRat2.text())
            text_file.write("\t")
            text_file.write("Rat "+self.LableRat3.text())
            text_file.write("\n")            
            for row in range(self.Table.rowCount()):
                for column in range(self.Table.columnCount()):
                    item = self.Table.item(row, column)
                    text_file.write(item.text())
                    text_file.write("\t")
                text_file.write("\n")
        
        filename2=filename+"_S"
        Rat=[self.LableRat1.text(),self.LableRat2.text(),self.LableRat3.text()]
        with open(filename2+".txt", "w") as text_file:
            text_file.write("Animal")
            text_file.write("\t")
            text_file.write("Camera")
            text_file.write("\t")
            text_file.write("X0")
            text_file.write("\t")
            text_file.write("T")
            text_file.write("\t")
            text_file.write("K")
            text_file.write("\t")
            text_file.write("D")
            text_file.write("\t")
            text_file.write("S")
            text_file.write("\t")
            text_file.write("I")
            text_file.write("\t")
            text_file.write("Attempts")
            text_file.write("\t")
            text_file.write("Trials")
            text_file.write("\n")      
            
            for row in range(self.TableSumary.rowCount()):
                text_file.write(Rat[row])
                text_file.write("\t")
                text_file.write(self.Camera.currentText())
                text_file.write("\t")
                for column in range(self.TableSumary.columnCount()):
                    item = self.TableSumary.item(row, column)
                    text_file.write(item.text())
                    text_file.write("\t")
                text_file.write("\n")
            
class videoWindow(QtWidgets.QWidget):
        def __init__(self, window):
            self.window = window
            QtWidgets.QWidget.__init__(self)
                        
            self.resize(500, 500)
            layout = QtWidgets.QGridLayout()
            self.setLayout(layout)
            self.keyPressEvent= self.window.keyPressEvent
            
            self.video_frame=QtWidgets.QLabel()
            self.video_frame.setGeometry(QtCore.QRect(10, 40, 640, 480))
            self.video_frame.setFrameShape(QtWidgets.QFrame.Box)
            
            self.video_screen=QtWidgets.QLabel()
            self.video_screen.setGeometry(QtCore.QRect(10, 40, 640, 480))
            self.video_screen.paintEvent= self.PaintVerticalLine
            self.video_screen.mousePressEvent= self.window.getPos
            self.video_screen.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.video_screen.customContextMenuRequested.connect(self.openright)
            
            self.sl_frame = QtWidgets.QSlider()
            self.sl_frame.setOrientation(QtCore.Qt.Horizontal)
            self.sl_frame.setMinimum(1)
            self.sl_frame.setMaximum(255)
            self.sl_frame.setValue(1)
            self.sl_frame.setTickPosition(QtWidgets.QSlider.TicksBelow)
            self.sl_frame.setTickInterval(1000)
            self.sl_frame.setGeometry(QtCore.QRect(9, 530, 640, 20))
            self.sl_frame.setEnabled(False)
                        
            layout.addWidget(self.video_frame, 0,0)
            layout.addWidget(self.video_screen, 0,0)
            layout.addWidget(self.sl_frame, 1,0)
            self.show()
            
        def PaintVerticalLine(self, event):
            painter = QtGui.QPainter(self.video_screen)
            pen = QtGui.QPen()
            pen.setColor(QtGui.QColor(0,255,0))
            pen.setWidth(2)
            painter.setPen(pen)
            painter.drawLine(self.window.line1_x, 0, self.window.line1_x, self.video_screen.height())
            painter.drawLine(self.window.line2_x, 0, self.window.line2_x, self.video_screen.height())
            painter.drawText(int(self.window.line1_x/2-5), 15, "Rat L")
            painter.drawText(int((self.window.line2_x + self.window.line1_x)/2-5), 15, "Rat M")
            painter.drawText(int((self.video_screen.width() + self.window.line2_x)/2-5), 15, "Rat R")
            
        def openright(self):
            popMenu = QtWidgets.QMenu()
            
            if self.window.play_button.text() == "Stop":
                self.window.playBtn()
            popMenu.addAction(QtWidgets.QAction("X0", self,  enabled=True, triggered= self.window.X0))
            popMenu.addAction(QtWidgets.QAction("T", self,  enabled=True, triggered= self.window.T))
            popMenu.addAction(QtWidgets.QAction("K", self,  enabled=True,triggered= self.window.K))
            popMenu.addAction(QtWidgets.QAction("D", self,  enabled=True,triggered= self.window.D))
            popMenu.addAction(QtWidgets.QAction("S", self,  enabled=True,triggered= self.window.S))
            popMenu.addAction(QtWidgets.QAction("I", self,  enabled=True,triggered= self.window.I))
            popMenu.addAction(QtWidgets.QAction("----------", self,  enabled=True)) 
            popMenu.addAction(QtWidgets.QAction("Set Line 1", self,  enabled=True,triggered= self.window.setLine1))
            popMenu.addAction(QtWidgets.QAction("Set Line 2", self,  enabled=True,triggered= self.window.setLine2))
            popMenu.addAction(QtWidgets.QAction("----------", self,  enabled=False)) 
            popMenu.addAction(QtWidgets.QAction("Erese", self,  enabled=True, triggered= self.window.Erese))
            popMenu.exec_(QtGui.QCursor.pos())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ControlWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
