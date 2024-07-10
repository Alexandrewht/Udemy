use base_de_dados;

-- INSERT IGNORE
insert ignore into users_roles (users_id, role_id)
select id, 
(select id from roles order by rand() limit 1) as qualquer 
from users order by rand() limit 5;