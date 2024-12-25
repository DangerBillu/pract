R={1: "A",2: "B", 3:"D", 4:"B", 5:"C"} 
stack=[]
def push():
    for key, value in R.items():
        if value == "B" or value == "A":
            stack.append(key)
    print(stack)
push()

def pop():
    return stack.pop()
print(pop())

def display_stack():
    for item in stack[::-1]:
        print(item)
display_stack()