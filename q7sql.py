'''
q1: To display highest and lowest salaries drawn in each department
a1: select department, min(salary) from teacher group by department; 
    select department, max(salary) from teacher group by department;

q2: To display all teacher’s name along with their place of posting in ascending order of their names 
a2: select name, place from teacher, placement where teacher.department = placement.department order by name;

q3: To decrease the width of department by 2 characters 
a3: alter table teacher modify department varchar(20);

q4: To change the department of Saman to geography 
a4: update teacher set department = 'geography' where name = 'Saman';
'''