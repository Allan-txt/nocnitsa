from PIL import Image

im = Image.open('images/flower.png')
im.resize((3000,2000)).save("flower.png")