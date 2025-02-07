n=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack=[]
for i in n:
    if i%2==0:
        stack.append(i)

print(n, "orignal list")
print(stack, "filtered list of even numbers")

def push():
    l = int(input("Enter the number to be pushed: "))
    if l%2 == 0:
        stack.append(l)
        print(stack, "number pushed into stack")
    else:
        print("cannot be added to the stack because not an even number")
def pop():
    if len(stack)==0:
        return None   
    else:
        z = stack.pop()
    print(z)
    print(stack, "stack after popped number")

def display():
    print(stack[::-1])

def menu():
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display Stack")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            push()
        elif choice == '2':
            pop()
        elif choice == '3':
            display()
        elif choice == '4':
            print("Exiting the program.")
            break
menu()

