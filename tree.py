class Node:
    def __init__(self, kind, value):
        self.kind=kind
        if self.kind=="Number":
            self.value=int(value)
        elif self.kind=="Add":
            self.value=""
            self.display="+"
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def show(self,level=0):
        print("  " * level + self.kind + " "+ self.display)
        for child in self.children:
            child.show(level+1)
    def evaluate(self):

        if self.kind == "Number":
            return int(self.value)
        if self.kind == "Add":
            return self.children[0].evaluate() + self.children[1].evaluate()
    def render(self,painter,x,y,node_positions):
        metrics = painter.fontMetrics()
        if self.kind=="Number":
            self.display=str(self.value)
            self.xpos=x
            self.ypos=y
            self.width= metrics.horizontalAdvance(self.display)
            self.height = metrics.height()
            painter.drawText(self.xpos,self.ypos, self.display)
            node_positions.append((self,self.xpos,self.ypos,self.width,self.height)) #This node position thing needs worked on code works if this is commented out
            return
        if self.kind =="Add":
            self.display="+"
            self.children[0].render(painter,x,y,node_positions)
            self.xpos=x+self.children[0].width
            self.ypos=y
            self.width= metrics.horizontalAdvance(self.display)
            self.height=metrics.height()
            painter.drawText(self.xpos,self.ypos, self.display)
            node_positions.append((self,self.xpos,self.ypos,self.width,self.height)) # This node position thing needs worked on
            self.children[1].render(painter,self.xpos+self.width,y,node_positions)
            return

#root=Node("Add","")
#x_node=Node("Number","5")
#two_node=Node("Number","2")
#root.add_child(x_node)
#root.add_child(two_node)

#print(root.render())
#two_node.show()

#print(root.evaluate())