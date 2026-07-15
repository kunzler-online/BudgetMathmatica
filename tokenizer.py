from tree import Node

# A little dictionary to handle possible inputs
char_types={
    "0":"Number",
    "1":"Number",
    "2":"Number",
    "3":"Number",
    "4":"Number",
    "5":"Number",
    "6":"Number",
    "7":"Number",
    "8":"Number",
    "9":"Number",   
    " ":"Space",
    "+":"Add"     
}

#My tokenizer function
def tokenizer(input):
    pos=0
    ret=[] # We return a list with the tokens, start it as empty
    while pos<len(input):
        currentchar=input[pos] 
        typecurrent=char_types[currentchar]
        
        if typecurrent == "Number": #Use a recursive helper function to handle long strings. 
            ntret=numbertokenizer(input+" ", pos+1, currentchar)
            Token={
                "type":"NUMBER",
                "value":ntret[0]
            }
            pos+=ntret[1]

        elif typecurrent=="Space": #Skip Spaces
            pos+=1
            continue

        elif typecurrent=="Add": #Create Add token
           Token={
                "type":"ADD",
                "value":""
            }
        ret.append(Token)
        pos+=1
    return ret
        
def numbertokenizer(input, pos, numbervalue={},reps=0): #Recursive helper function for number strings, keeps track of total number value and recursion depth to help with pos
    currentchar=input[pos]
    typecurrent=char_types[currentchar]
    if typecurrent == "Number": 
        return numbertokenizer(input,pos+1,numbervalue+currentchar,reps+1)
    elif typecurrent != "Number":
        return (numbervalue, reps)

    def __init__(self, kind, value):
        self.kind=kind
        self.value=value
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
        
