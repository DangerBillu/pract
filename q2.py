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
            display_stack()
        elif choice == '4':
            print("Exiting the program.")
            break
menu()
