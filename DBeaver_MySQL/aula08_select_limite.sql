USE base_de_dados;

-- LIMIT limita a qtd de valores
-- offset desloca o cursor para exibir os próximos dados
SELECT id, first_name, email as uemail 
FROM users u
WHERE id > 20
order by id asc
limit 2 offset 1;

SELECT id, first_name, email as uemail 
FROM users u
WHERE id > 20
order by id asc
limit 6, 3; 