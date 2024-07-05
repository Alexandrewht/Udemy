from PIL import Image
from pathlib import Path

ROOT_DIR = Path(__file__).parent

icon_path = ROOT_DIR / 'calculadora_icone.jpg'  # Caminho correto do seu ícone .jpg
NEW_IMAGE = ROOT_DIR / '32x32.jpg'  # Caminho onde deseja salvar a nova imagem

# Abrir a imagem original
pil_image = Image.open(icon_path)

# # Obter as dimensões originais
width, height = pil_image.size

# Definir o novo tamanho desejado
new_width = 32
new_height = 32

# Redimensionar a imagem
new_image = pil_image.resize((new_width, new_height))

# Salvar a nova imagem redimensionada
new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
)
