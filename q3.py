import csv 
def add():
    f = open("furdata.csv", "a", newline='')
    writer = csv.writer(f)
    n = int(input("Enter the number of items: "))
    for i in range(n):
        fid = input("Enter the id: ")
        fname = input("Enter the name: ")
        fprice = int(input("Enter the price: "))
        writer.writerow([fid, fname, fprice])
    f.close()
add()
def search():
    f = open("furdata.csv", "r")
    reader = csv.reader(f)
    for i in reader:
        if int(i[2]) > 10000:
            print(i)
    f.close()
search()