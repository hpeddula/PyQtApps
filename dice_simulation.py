import random
import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QVBoxLayout,QLabel,QWidget,QHBoxLayout
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.l=QLabel("Dice Simulator")
        self.l1=QLabel("Would you like to roll a  die,Please Click Yes or No")
        self.l2=QLabel()
        self.Yes=QPushButton("Yes")
        self.No=QPushButton("No")

        layout=QVBoxLayout()
        hlayout=QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(self.Yes)
        hlayout.addWidget(self.No)
        hlayout.addStretch()
        layout.addStretch()
        layout.addWidget(self.l)
        layout.addWidget(self.l1)
        layout.addWidget(self.l2)
        layout.addStretch()
        layout.addLayout(hlayout)
        self.Yes.clicked.connect(self.roll_die)
        self.No.clicked.connect(self.roll_die)
        self.setLayout(layout)
        self.show()
        self.setWindowTitle("Dice Simulator")

    def roll_die(self):
        sender = self.sender()
        if sender.text() == "Yes":
            n = random.randrange(1, 6)
            self.l2.setText(str(n))
        else:
            self.l2.setText("It's Ok!!")

app=QApplication(sys.argv)
a=Window()
sys.exit(app.exec_())