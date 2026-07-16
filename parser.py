from tree import Node
from tokenizer import tokenizer

def parser(input):
    a=parseAddition(input)
    if a!=None:
        return a
    n=parseNumber(input)
    if n!=None:
        return n

def parseAddition(input):
    pos=len(input)-1
    while pos>=0:
        if input[pos]["type"] == "ADD":
            add=Node("Add","")
            add.add_child(parser(input[0:pos]))
            add.add_child(parser(input[pos+1:]))
            return(add)
        pos+= -1
        

def parseNumber(input):
    pos=0
    while pos<len(input):
        if input[pos]["type"] == "NUMBER":
            number=Node("Number",input[pos]["value"])
            return(number)
        pos+=1
            


tokens=tokenizer("2+3+5")
#print(tokens)
parsed=parser(tokens)
parsed.show()
print(parsed.render())
#print(parsed.evaluate())
