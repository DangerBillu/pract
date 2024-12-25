Herbs = {
    'Adrak': 'Ginger',
    'Amla': 'Gooseberry',
    'Babool': 'Indian Gum',
    'Dhania': 'Coriander',
    'Lahsun': 'Garlic',
    'Tulsi': 'Basil'
}

stack = []
poppeds = []
def display_herbs():
    for key, value in Herbs.items():
        if value.startswith('G'):
            stack.append((key, value))


def add_herb(herb, meaning):
        stack.append((herb, meaning))

def remove_herb():
    return stack.pop()

def display_stack():
    for item in stack[::-1]:
        print(item)
herb = input("Enter the name of the herb: ")
meaning = input("Enter the meaning of the herb: ")


display_herbs()
remove_herb()
add_herb(herb, meaning)
display_stack()

print("Stack contents:")
print(stack)
