USE base_de_dados;

-- INSERT SELECT
-- insere valores em uma tabela usando outra
insert into profiles 
(bio, description, user_id)
select 
concat('Bio de ', first_name), 
concat('Description de ', first_name), 
id 
from users;


delete from profiles;  # CUIDADO AO EXECUTAR ISSO EM UMA TABELA EM PRODUÇÃO