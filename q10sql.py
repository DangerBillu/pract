'''
q1: To display the name of the employee with least sales 
a1: select name from employee where sales = (select min(sales) from employee);

q2: To display the average salaries of all types of jobs(use jobId) 
a2: select jobId, avg(salary) from job group by jobId;

q3: To add a column location-varchar(20) in Job table 
a3: alter table job add location varchar(20);

q4: To increase the sales of all employees by 2% of all employees with names beginning with S 
a4: update employee set sales = sales + 0.02*sales where name like 'S%';
'''