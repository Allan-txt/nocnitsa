from PIL import Image
from io import BytesIO

def getbits(img, start, to):#
    image = Image.open(img)
    dectuplelist = image.get_flattened_data()
    bitlist = []
    for dectuple in dectuplelist:
        for dec in dectuple:
            bitlist.append(format(dec, '08b')[start:to])#oh man...
    #print(bitlist)
    return bitlist
def putemtogehter(carrierbits, msgbits):
    for i in range(len(carrierbits)):
        print("carrierbit: ", carrierbits[i])
        print("msgbit: ", msgbits[i])
        carrierbits[i] = carrierbits[i] +  msgbits[i]
        print("new: ", carrierbits[i])
    return carrierbits
def main():
    #carrier = Image.open("tree.png")
    #msg = Image.open("cat.png")
    carrierbits = getbits("tree.png",0,6)
    msgbits = getbits("cat.png",6,8)

    carrierbits = putemtogehter(carrierbits, msgbits)
    print(carrierbits)
    width = 640
    height = 434
    Image.frombytes(mode, size, data, decoder_name='raw', *args)


main()
