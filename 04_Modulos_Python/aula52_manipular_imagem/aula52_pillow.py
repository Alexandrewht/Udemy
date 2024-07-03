# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photshop do Python
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'lufy.png'
NEW_IMAGE = ROOT_FOLDER / 'lufy_resized.png'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info.get('exif')

#width   new_width
#height  new_height
new_width = 640
new_height = round(height * new_width / width)
# print(width, height)
# print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    exif=exif
)