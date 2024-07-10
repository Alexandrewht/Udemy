USE base_de_dados;

-- SELECT - selecionando valores de mais de uma tabela

-- Selecionando id de users e profile e o nome relacionado
select u.id as users_id, p.id as profile_id, u.first_name
from users as u, profiles as p
where u.id = p.user_id;