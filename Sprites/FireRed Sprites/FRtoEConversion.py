from PIL import Image
from os import listdir
from os.path import isfile, join

WIDTH = 256
HEIGHT = 128
SRC_DIR = 'Sprites'
DEST_DIR = 'Sprites (Emerald Compatible)'

for file in listdir(SRC_DIR):
    img = join(SRC_DIR, file)
    if not isfile(img):
        continue
    spritesheet = Image.open(img).convert("RGBA")
    new_spritesheet = Image.new('RGBA', (WIDTH, HEIGHT))
    if spritesheet.size[0] != 256 or spritesheet.size[1] != 64:
        print(f'Wrong dimesions on {spritesheet}. Skipping')
        continue
    front_sprite = spritesheet.crop((0, 0, 128, 64))

    new_spritesheet.paste(spritesheet, (0, 0))
    new_spritesheet.paste(front_sprite, (0, 64))

    new_spritesheet.save(join(DEST_DIR, file))