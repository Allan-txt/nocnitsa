from PIL import Image

def getbits(img, start, to):#
    image = Image.open(img)
    dectuplelist = image.get_flattened_data()
    bitlist = []
    for dectuple in dectuplelist:
        for dec in dectuple:
            bitlist.append(format(dec, '08b')[start:to])#oh man...
    return bitlist
def putemtogehter(carrierbits, msgbits):
    for i in range(len(carrierbits)):
        carrierbits[i] = carrierbits[i] +  msgbits[i]
    return carrierbits
def hide():
    carrierbits = getbits(input("carrier: "),0,6)
    msgbits = getbits(input("msg: "),6,8)

    carrierbits = putemtogehter(carrierbits, msgbits)
    width = 640
    height = 434
    size = (width,height)
    data = [int(byte,2) for byte in carrierbits]
    data = bytes(data)

    carrier = Image.frombytes("RGB", size, data, decoder_name='raw')
    carrier.save("carrier.png")



