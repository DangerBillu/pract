'''
q1: Display book name ,author name and price of computer type books in ascending order of their prices. 
a1: select bookname, authorname, price from book where type = 'computer' order by price;

q2:To increase the price of all history books by Rs 50.
a2: update book set price = price + 50 where type = 'history';

q3:to add a column stock_date in issued table to store date of taking stocks of books 
a3: alter table issued add stock_date date;

q4: To display book id, book name and quantity issued for all books which have been issued.
a4: select bookid, bookname, quantity from book, issued where book.bookid = issued.bookid;
'''