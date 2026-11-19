from PIL import Image

def showbits(path, bit):
    bitlist = getbits(path,0,6)
    print(bitlist)
    for i in bitlist:
        bitlist[i] = bitlist[i] + ""
    width = 640
    height = 434
    size = (width, height)
    data = [int(byte, 2) for byte in bitlist]
    data = bytes(data)

    carrier = Image.frombytes("RGB", size, data, decoder_name='raw')
    carrier.save("carrier.png")

def getbits(img, start, to):#
    image = Image.open(img)
    dectuplelist = image.get_flattened_data()
    bitlist = []
    for dectuple in dectuplelist:
        for dec in dectuple:
            bitlist.append(format(dec, '08b')[start:to])#oh man...
    return bitlist



showbits("v1/carrier.png", 3)




