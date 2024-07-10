USE base_de_dados;

-- Selecionando users id, profile id e first name
select u.id as users_id, p.id as profile_id, u.first_name
from users as u, profiles as p
where u.id = p.user_id;

-- tabela da esquerda = users
-- tabela da direita = profiles

-- LEFT JOIN, irá considerar os users
-- se não existir um relacionamento com profiles,
-- irá trazer os valores nulos (NULL)
select u.id as users_id, p.id as profile_id, u.first_name
from users as u
left join profiles p
on u.id = p.user_id;