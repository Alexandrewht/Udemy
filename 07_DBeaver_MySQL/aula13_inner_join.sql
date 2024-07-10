USE base_de_dados;

-- INNER JOIN
select u.id as users_id, p.id as profile_id, u.first_name
from users as u, profiles as p
where u.id = p.user_id;

delete from profiles  where id between 170 and 172;

-- tabela da esquerda = users
-- tabela da direita = profiles
select u.id as users_id, p.id as profile_id, u.first_name
from users as u
inner join profiles p
on u.id = p.user_id 
where u.first_name like '%a'
order by u.first_name desc
limit 10;