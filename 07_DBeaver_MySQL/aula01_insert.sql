-- Seleciona a base de dados
use base_de_dados;

-- Mostra as tabelas da base de dados
show tables;

-- Descreve as colunas da tabela
describe users;

-- Inserir registros na base de dados
insert into users 
	(first_name, last_name, email, password_hash) values
	("Helena", "A.", " ha@exemplo.com", "sql"),
	("Joana", "B.", " jb@exemplo.com", "dados"),
	("Rosana", "C.", " rc@exemplo.com", "falsos");