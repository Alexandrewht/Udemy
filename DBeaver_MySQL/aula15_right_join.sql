USE base_de_dados;

-- Selecionando users id, profile id e first name
select u.id as users_id, p.id as profile_id, u.first_name
from users as u, profiles as p
where u.id = p.user_id;

delete from users where id = 1;

-- tabela da esquerda = users
-- tabela da direita = profiles

-- RIGHT JOIN, todos os registros da tabela profiles,
-- mesmo q não tenha uma relação com users,
-- irá mostrar NULL
select u.id as users_id, p.id as profile_id, u.first_name
from users as u
right join profiles p
on u.id = p.user_id;

-- OBS. Caso tenha deletado de users e ainda manter o profile,
-- irá dar erro ao atrelar a relação da chave estrangeira.
-- para isso, é necessário criar um id de usuários ao que está faltando
-- ou deletar o profile.