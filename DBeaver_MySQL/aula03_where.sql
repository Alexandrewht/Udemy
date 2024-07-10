-- where filtra registros
-- Operadores de comparação    = < <= > >= <> != 
-- Operadores lógicos and e or
use base_de_dados;

select * from users 
where id <> 15; # <> esse simbolo quer dizer diferente

select * from users u 
where created_at < '2024-07-08 12:13:14';

select * from users u 
where created_at < '2024-07-08 12:13:14'
and first_name = 'Alexandre';

select * from users 
where id!= 15 
or password_hash = 'a123';