class Node:
    def __init__(self, kind, value):
        self.kind=kind
        if self.kind=="Number":
            self.value=int(value)
            self.display=str(value)
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
    def render(self):
        if self.kind=="Number":
            return self.display
        if self.kind =="Add":
            return self.children[0].render()+self.display+self.children[1].render()




    def width(self):
        if self.kind=="Number":
            return len(self.value)*7
        if self.kind=="Add":
            return self.children[0].width() +7+ self.children[1].width()

#root=Node("Add","")
#x_node=Node("Number","5")
#two_node=Node("Number","2")
#root.add_child(x_node)
#root.add_child(two_node)

#print(root.render())
#two_node.show()

#print(root.evaluate())