from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget 
from PySide6.QtCore import Qt
from tokenizer import tokenizer
from parser import parser
from PySide6.QtGui import QPen
import sys

class MathWidget(QWidget): #My GUI interface. It renders a tree, and has selected nodes
    def __init__(self, tree):
        super().__init__()
        self.tree=tree
        self.setFocusPolicy(Qt.StrongFocus)
        self.input_text =""
        self.node_positions=[]
        self.selected_node= None

    def paintEvent(self,event): #resets node positions each time, and calls recursive drawnode function
        self.node_positions=[]
        painter=QPainter(self)
        if self.tree is None:
            return
        self.tree.render(painter,50,50,self.node_positions)
        if self.selected_node !=None:
            painter.drawRect(self.selected_node.xpos,self.selected_node.ypos+3,self.selected_node.width,-self.selected_node.height)


    def mousePressEvent(self, event):
        x=event.position().x()
        y=event.position().y()
        for node, nx,ny,xwidth,ywidth in reversed(self.node_positions):
            if nx<=x<=nx+xwidth and ny-ywidth<=y<=ny:
                print("clicked:", node.kind, node.value)
                self.selected_node = node
                self.update()
                return
        

    def keyPressEvent(self, event):
        key=event.text()
        code = event.key()
        if event.key() == Qt.Key_Return:
            self.selected_node = None
            self.update()
            return
        if self.selected_node is not None:
            if self.selected_node.kind == "Number":
                if key.isdigit():
                    self.selected_node.value = key
                    self.selected_node.display= key
                    self.update()
                    return
        if key.isdigit():
            self.input_text+= key
        elif key == "+":
            self.input_text+= key
        elif code == Qt.Key_Backspace:
            self.selected_node.value = ""
        
        print(self.input_text)
        self.update()
        

tokens = tokenizer("11+22")
tree = parser(tokens)


app=QApplication(sys.argv)
wid=MathWidget(tree)

wid.resize(400,200)
wid.show()
app.exec()

