use base_de_dados;

-- SELECT IN seleciona elementos entre os valores enviados
select * from users u 
where id in (10, 15, 30, 50, 100, 110)
and first_name in ('Paulo', 'Keelie');