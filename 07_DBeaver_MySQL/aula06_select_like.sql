USE base_de_dados;

-- LIKE (parecido)
-- % qualquer coisa
-- _ um caractere

-- Busca todos os usuários cujos primeiros nomes terminam com 'a'
SELECT * FROM users u 
WHERE first_name LIKE '%a'; -- O caractere % antes de 'a' permite qualquer sequência de caracteres antes de 'a'

-- Busca todos os usuários cujos primeiros nomes terminam com 'o'
SELECT * FROM users u 
WHERE first_name LIKE '%o'; -- O caractere % antes de 'o' permite qualquer sequência de caracteres antes de 'o'

-- Busca todos os usuários cujos primeiros nomes começam com 'h'
SELECT * FROM users u 
WHERE first_name LIKE 'h%'; -- O caractere % após 'h' permite qualquer sequência de caracteres depois de 'h'

-- Busca todos os usuários cujos primeiros nomes começam com 'he'
SELECT * FROM users u 
WHERE first_name LIKE 'he%'; -- O caractere % após 'he' permite qualquer sequência de caracteres depois de 'he'

-- Busca todos os usuários cujos primeiros nomes contêm 'mo' em qualquer posição
SELECT * FROM users u 
WHERE first_name LIKE '%mo%'; -- O caractere % antes e depois de 'mo' permite qualquer sequência de caracteres antes e depois de 'mo'

-- Busca todos os usuários cujos primeiros nomes tem 5 letras (5 underlines)
SELECT * FROM users u 
WHERE first_name LIKE '_____'; 