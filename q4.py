import pickle
def createfile():
    f= open("Book.dat", "ab")
    bookno = int(input("Enter Book Number: "))
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Price: "))
    record = [bookno, book_name, author, price]
    pickle.dump(record, f)
    f.close()

def countrec(author_name):

    count = 0
    f = open("Book.dat", "rb")
    while True:
        try:
            record = pickle.load(f)
            if record[2] == author_name:
                count += 1
            return count
        except EOFError:
            break
    f.close()
author_name = input("Enter the author name: ")
createfile()
countrec(author_name)

