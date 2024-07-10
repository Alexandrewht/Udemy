use base_de_dados;

-- SELECT com vários JOINs
select u.id as uid, u.first_name, p.bio, r.name as role_name
from users as u
left join profiles as p on u.id = p.id 
inner join users_roles as ur on u.id  = ur.users_id 
inner join roles as r on ur.role_id = r.id
where u.id = 10
order by uid asc
limit 2,1;
