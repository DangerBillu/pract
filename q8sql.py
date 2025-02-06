'''
q1: To display the name and designation of the youngest Employee  
a1: select name, designation from employee where dob = (select min(dob) from employee);

q2: To decrease the HRA of S02 grade employees by 2% 
a2: update employee set hra = hra - 0.02*hra where grade = 'S02';

q3: To display last three characters of employee names with DOJ in descending order of DOJ 
a3: select substr(name, -3) from employee order by doj desc;

q4: To remove primary key from employee table 
a4: alter table employee drop primary key;
'''