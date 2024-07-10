-- 1) Insira 5 usuários
-- 2) Insira 5 perfís para os usuários inseridos
-- 3) Insira permissões (roles) para os usuários inseridos
-- 4) Selecione os últimos 5 usuários por ordem decrescente
-- 5) Atualize o último usuário inserido
-- 6) Remova uma permissão de algum usuário
-- 7) Remova um usuário que tem a permissão "PUT"
-- 8) Selecione usuários com perfís e permissões (obrigatório)
-- 9) Selecione usuários com perfís e permissões (opcional)
-- 10) Selecione usuários com perfís e permissões ordenando por salário

use base_de_dados;

select * from users;

-- 1 Insira 5 usuários.
insert into users (first_name, last_name, email, password_hash) 
values
	("Marcela", "Camargo", "marcela.camargo@exemplo.com", "n9OqhCK4@U"),
	("Oliver", "Vieira", "luan.vieira@exemplo.com", "3EwTwhvi"),
	("Pietro", "Carvalho", "pietro.carvalho@exemplo.com", "6PrD&jKQO"),
	("Thales", "da Mata", "thales.mata@exemplo.com", "wDg!2bXeKT"),
	("Miguel", "Cassiano", " miguel.cassiano@exemplo.com", "U@8qIOda4$");
	
-- 2 Insira 5 perfís para os usuários inseridos.
insert ignore into profiles (bio, description, user_id)
select 
	concat('Bio de ', first_name), 
	concat('Description de ', first_name), id
from users;
	
-- 3 Insira permissões (roles) para os usuários inseridos.
insert ignore into users_roles (users_id, role_id)
select id, (select id from roles order by rand() limit 1) as qualquer 
from users;

-- 4 Selecione os últimos 5 usuários por ordem decrescente.
select first_name 
from users u
order by first_name 
desc limit 5;
	
-- 5 Atualize o último usuário inserido.
SET @last_id = (SELECT id FROM users ORDER BY id DESC LIMIT 1); 

update users set first_name = 'Alexandre'
where id = @last_id;
	
select id, first_name 
from users 
order by id 
desc limit 1;

-- 6 Remova uma permissão de algum usuário.
select u.id as users_id, u.first_name, ur.role_id 
from users as u, users_roles ur
where u.id = ur.users_id;
delete from users_roles 
where users_id = 3 and role_id = 4;

-- 7 Remova um usuário que tem a permissão "PUT".
select u.id as users_id, u.first_name, ur.role_id 
from users as u, users_roles ur
where u.id = ur.users_id 
order by ur.role_id asc;

delete from users_roles 
where users_id = 16 and role_id = 4
	
-- 8 Selecione usuários com perfís e permissões (obrigatório).
select u.id as users_id, u.first_name, ur.role_id 
from users as u, users_roles ur 
where u.id = ur.users_id;

-- 9 Selecione usuários com perfís e permissões (opcional).
select u.id as users_id, u.first_name, 
count(ur.role_id) as sum_roles
from users u
join users_roles ur on u.id = ur.users_id
group by u.id, u.first_name;

-- 10 Selecione usuários com perfís e permissões ordenando por salário.
select u.id as users_id, p.id as profile_id, u.first_name, u.salary 
from users as u
right join profiles p
on u.id = p.user_id
where u.salary  is not null 
order by u.salary desc;