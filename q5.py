n=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack=[]
s= len(n)
def push():
    l = int(input("Enter the number to be pushed: "))
    n.append(l)
    print(n)
def pop():
    n.pop()
    print(n)
def display():
    for i in range(s):
        d= n.pop()
        stack.append(d)
    print(stack)
pop()
push()
display()