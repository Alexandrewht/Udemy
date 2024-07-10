use base_de_dados;

-- Funções de agregação - max, min, avg, sum e count + group by

select 
max(salary) as max_salary,
min(salary) as min_salary,
avg(salary) as avg_salary,
sum(salary) as sum_salary,
count(salary) as count_salary
from users u
where first_name = 'Carly';

select
u.first_name,
max(u.salary) as max_salary,
min(u.salary) as min_salary,
avg(u.salary) as avg_salary,
sum(u.salary) as sum_salary,
count(u.id) as Total
from users u
left join profiles as p on p.user_id = u.id
-- where u.id in (47, 49, 676, 3)
group by first_name
order by sum_salary desc
-- limit 5;