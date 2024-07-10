USE base_de_dados;

-- Criamos uma coluna nova chama salary em users
-- Vamos preencher usando RAND e ROUND

-- RAND recebe números float randomicos
-- ROUND está recebendo (RAND * 10000, 2 casas decimais)
select ROUND(rand()* 10000, 2);

-- configura um salário aleatório para users
update users set salary = ROUND(rand()* 10000, 2);

select salary from users 
where salary between 1000 and 1500
order by salary asc;