use base_de_dados;

-- SELECIONA
select u.first_name, p.bio from users u
left join profiles p on p.user_id = u.id 
where u.first_name = 'Mario';

-- DELETE 
delete p, u from users u
left join profiles p on p.user_id = u.id 
where u.first_name = 'Mario';