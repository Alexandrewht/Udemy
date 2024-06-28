# Vamos usar a pasta aula32 para fazer raspagem de dados
# requests para requisições HTTP no Python
# Tutorial -> https://www.youtube.com/watch?v=Qd8JT0bnJGs
import requests

# para rodar o servidor localmente
# usar o comando no console
# python -m http.server -d C:\Dev\Udemy\04_Modulos_Python\aula32_site 3333

# Serving HTTP on :: port 3333 (http://[::]:3333/) ...
# ::1 - - [25/Jun/2024 15:57:54] "GET / HTTP/1.1" 200 -
# ::1 - - [25/Jun/2024 15:57:54] "GET /style.css HTTP/1.1" 200 -
# ::1 - - [25/Jun/2024 15:57:58] code 404, message File not found
# ::1 - - [25/Jun/2024 15:57:58] "GET /favicon.ico HTTP/1.1" 404 -
# favicon é um arquivo de imagem

# http:// -> 8080
# A porta padrão para HTTPS é 443, 
# e não 0443 ou 4430. Vamos esclarecer

# Porta 443: Utilizada para HTTPS, permitindo comunicação segura e criptografada 
# entre navegadores web e servidores.
# o nosso iremos usar a porta 3333
url = 'http://localhost:3333'
response = requests.get(url)

# print(response)
print(response.status_code)
# print(response.headers)
# print(response.content) # retorna o conteúdo em bytes
print(response.text)