USE base_de_dados;

-- INSERT de dados para a tabela roles
insert into roles (name)
values
('POST'),('PUT'),('DELETE'),('GET');

insert into users_roles (users_id, role_id)
values 
(6, 7);

select users_id , role_id from users_roles 
where users_id = 6 and role_id = 7;

select id, 
(select id from roles order by rand() limit 1) as qualquer 
from users;

-- Adicionando randomicamente em users_id, permissões (users_roles)
insert into users_roles (users_id, role_id)
select id, 
(select id from roles order by rand() limit 1) as qualquer 
from users;
