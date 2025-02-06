'''
q1: Display the Trainer Name, City & Salary in descending order of their Hiredate.
a1: select tname, city, salary from trainer order by hiredate desc;

q2: To display the TNAME and CNAME of all trainers who joined the Institute in the month of December 2001. 
a2: select tname, cname from trainer, course where trainer.tid = course.tid and hiredate between '2001-12-01' and '2001-12-31';

q3: To display number of Trainers from each city.
a3: select city, count(*) from trainer group by city;

q4: To display the Trainer ID and Name of the trainer who does not belong to ‘Mumbai’ and ‘DELHI’
a4: select tid, tname from trainer where city not in ('Mumbai', 'DELHI');
'''