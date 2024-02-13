import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QWidget
from PyQt5.QtGui import QIcon

class Button(QPushButton):
    def __init__(self,text):
        super().__init__(text)

        self.setFixedSize(150,70)
        self.setStyleSheet(""" background:black;
                           color:black;
                           border-radius:15px;
                           font-size:20pt;
                           border:2px solid lime""")
class Button2(QPushButton):
    def __init__(self,text):
        super().__init__(text)

        self.setFixedSize(230,50)
        self.setStyleSheet(""" background:black;
                           color:lime;
                           border-radius:15px;
                           font-size:20pt;
                           border:2px solid lime""")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.count = 0
        self.num_x = ''
        self.num_o = ''

        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("Iks Noll")
        self.setFixedSize(500, 600)
        self.setStyleSheet('background: black;color;lime')

        self.btn1 = Button('1')
        self.btn2 = Button('2')
        self.btn3 = Button('3')
        self.btn4 = Button('4')
        self.btn5 = Button('5')
        self.btn6 = Button('6')
        self.btn7 = Button('7')
        self.btn8 = Button('8')
        self.btn9 = Button('9')

        self.btn_list =[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9]

        self.label = QLabel()
        self.label.setText("Har safar x boshlaydi")
        self.label.setFixedSize(480,60)
        self.label.setStyleSheet(""" background:black;
                           color:lime;
                           border-radius:15px;
                           font-size:20pt;
                           border:2px solid""")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.btn_res = Button2("New game")
        self.btn_exit = Button2("Exit")
        
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.h_box1.addWidget(self.btn1)
        self.h_box1.addWidget(self.btn2)
        self.h_box1.addWidget(self.btn3)

        self.h_box2.addWidget(self.btn4)
        self.h_box2.addWidget(self.btn5)
        self.h_box2.addWidget(self.btn6)

        self.h_box3.addWidget(self.btn7)
        self.h_box3.addWidget(self.btn8)
        self.h_box3.addWidget(self.btn9)

        self.h_box4.addWidget(self.btn_res)
        self.h_box4.addWidget(self.btn_exit)
        
        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

        self.btn1.clicked.connect(lambda:self.__x_o(self.btn1))
        self.btn2.clicked.connect(lambda:self.__x_o(self.btn2))
        self.btn3.clicked.connect(lambda:self.__x_o(self.btn3))
        self.btn4.clicked.connect(lambda:self.__x_o(self.btn4))
        self.btn5.clicked.connect(lambda:self.__x_o(self.btn5))
        self.btn6.clicked.connect(lambda:self.__x_o(self.btn6))
        self.btn7.clicked.connect(lambda:self.__x_o(self.btn7))
        self.btn8.clicked.connect(lambda:self.__x_o(self.btn8))
        self.btn9.clicked.connect(lambda:self.__x_o(self.btn9))

        self.btn_res.clicked.connect(self.res)
        self.btn_exit.clicked.connect(self.exit)
    
    def exit(self):
        self.close()

    def res(self):
        new = Window()
        self.close()
        new.show()

    def __x_o(self,btn):
        text = btn.text()
        win = ['123','456','789','147','258','369','159','357']

        if self.count % 2 == 0 :
            self.count +=1
            btn.setText("X")
            btn.setEnabled(False)
            self.num_x += text
            btn.setStyleSheet(""" background:black;
                           color:lime;
                           border-radius:15px;
                           font-size:20pt;
                           border:2px solid""")
            
            for i in win:
                count = 0
                for j in self.num_x:
                    if j in i:
                        count += 1
                        
                if count == 3:
                    self.label.setText("X yutti")
                    self.__block()
                    self.num_x = ''
                    break

        else:
            count_o = 0 
            self.count +=1
            btn.setText("O")
            btn.setEnabled(False)
            self.num_o += text
            btn.setStyleSheet(""" background:lime;
                           color:black;
                           border-radius:15px;
                           font-size:20pt;
                           border:2px solid""")
            for i in win:
                count_o = 0
                for j in self.num_o:
                    if j in i:
                        count_o+=1
                
                if count_o ==3:
                        self.label.setText("O yutti")
                        self.__block()
                        self.num_o = ''
                    
        if self.count == 9 and self.label.text() == "":
            self.label.setText("Durrang")

    def __block(self):
        for i in range(len(self.btn_list)):
            self.btn_list[i].setEnabled(False)
                   
app = QApplication(sys.argv)

win = Window()
win.show()

app.exec_()