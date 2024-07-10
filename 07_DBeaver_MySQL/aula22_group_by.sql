use base_de_dados;

-- GROUP BY (agrupar por)
select first_name, COUNT(id) as Total from users u 
group by first_name 
order by Total desc;


select u.first_name, COUNT(u.id) as Total from users u 
left join profiles as p
on p.user_id = u.id
where u.id in (47, 49, 676, 3)
group by first_name
order by Total desc
limit 5;