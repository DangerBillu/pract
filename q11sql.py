'''
q1: To display all booking details of the bookings whose destination is KOL in descending order of price. 
a1: select * from booking where destination = 'KOL' order by price desc;

q2: To list all ticket numbers with their respective flight ids and companies(of flights) 
a2: select ticketno, flightid, company from booking, flight where booking.flightid = flight.flightid;

q3:To increase the size of destination by 5 characters 
a3: alter table booking modify destination varchar(25);

q4: To remove the primary key from flights table 
a4: alter table flight drop primary key;
'''