import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)


images[0].save(
    "costumes.gif", save_all=True, append_images=[1], duration=22, loop=0
)
