from PIL import Image
import argparse

def getbits(img, start, to):#
    image = img
    dectuplelist = image.get_flattened_data()
    bitlist = []
    for dectuple in dectuplelist:
        for dec in dectuple:
            bitlist.append(format(dec, '08b')[start:to])#oh man...
    return bitlist


def hide(carrier, message):
    imcarrier = Image.open(carrier)
    immessage = Image.open(message)
    size = immessage.size
    carrierbits = getbits(imcarrier, 0,8)
    msgbits = getbits(immessage, 0,2)
    width = format(size[0], "016b")
    height = format(size[1], "016b")
    binsize = width + height
    sizebits = []
    for i in range(0,len(binsize),2):
        sizebits.append(binsize[i:i+2])
    sizebits.extend(msgbits)

    msgbits = sizebits
    for i in range(len(msgbits)):
        carrierbits[i] = carrierbits[i][0:6] +  msgbits[i]

    data = [int(byte, 2) for byte in carrierbits]
    data = bytes(data)

    carrier = Image.frombytes("RGB", imcarrier.size, data, decoder_name='raw')
    carrier.save("carrier.png")


def extract(image):
    img = Image.open(image)
    bits = getbits(img, 6, 8)

    width = ""
    for i in bits[:8]:
        width = width + i
    height = ""

    for i in bits[8:16]:
        height = height + i


    bits = bits[16:]

    for i in range(len(bits)):
        bits[i] = bits[i] + "000000"



    size = (int(width,2),int(height,2))
    data = [int(byte, 2) for byte in bits]
    data = bytes(data)

    carrier = Image.frombytes("RGB", size, data, decoder_name='raw')
    carrier.save("recovered.png")

def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")

    hide_parser = commands.add_parser('hide')
    hide_parser.add_argument('carrier')
    hide_parser.add_argument('msg')

    extract_parser = commands.add_parser('extract')
    extract_parser.add_argument('carrier')

    args = parser.parse_args()
    if args.command == "hide":
        hide(args.carrier, args.msg)
    else:
        extract(args.carrier)

main()