from PIL import Image

im = Image.open('flower.png')
im.resize((3000,2000)).save("flower.png")