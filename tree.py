class Node:
    def __init__(self, kind, value, display):
        self.kind=kind
        self.value=value
        self.display=display
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def show(self,level=0):
        print("  " * level + self.kind + " "+ self.value)
        for child in self.children:
            child.show(level+1)
    def evaluate(self):
        if self.kind == "Number":
            return int(self.value)
        if self.kind == "Add":
            return self.children[0].evaluate() + self.children[1].evaluate()
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


#two_node.show()

#print(root.evaluate())