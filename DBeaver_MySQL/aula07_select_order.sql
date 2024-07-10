USE base_de_dados;

SELECT id, first_name, email as uemail 
FROM users u
WHERE id > 20
order by first_name desc, id asc;

