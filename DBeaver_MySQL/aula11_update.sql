USE base_de_dados;

select * from users;

-- UPDATE - Atualiza registros
update users set first_name = 'Mario',
last_name = 'Miranda'
where id between 11 and 15;  -- CUIDADO COM O UPDATE

select * from users where id between 10 and 21;

