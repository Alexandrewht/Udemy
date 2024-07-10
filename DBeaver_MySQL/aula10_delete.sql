USE base_de_dados;

-- DELETE apaga registros da tabela
delete from users where id = 73;

select * from users where id between 70 and 80;

-- AVISO: use select para garantir que está 
-- apagando os valores corretos

-- Ao usar CASCADE ao atrelar users com roles, ao deletar de users
-- os dados deletados também serão deletados dos roles
