use base_de_dados;

-- Seleciona colunas
select u.email as uemail, u.id as uid, users.first_name ufn # mesmo sem o as também funciona
from users u; -- u aqui é considerado um apelido

-- no select colocamos u. para puxar do users com as colunas solicitadas
