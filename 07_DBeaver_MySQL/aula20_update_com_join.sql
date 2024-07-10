use base_de_dados;

-- UPDATE COM JOIN

-- SELECIONA 
select u.first_name, p.bio from users u
join profiles p on p.user_id = u.id 
where u.first_name = 'Mario';

-- UPDATE 
update users as u
join profiles p on p.user_id = u.id
set p.bio = concat(p.bio, ' Atualizado') 
where u.first_name = 'Mario';