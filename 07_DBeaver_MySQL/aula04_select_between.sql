use base_de_dados;

-- SELECT BETWEEN seleciona um range de dados
select * from users u 
where id between 90 and 110;

select * from users u 
where 
created_at between '2020-06-12 00:00:00'
and '2020-09-04 23:59:59'
and id between 90 and 110

