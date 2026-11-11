from PIL import Image
import argparse

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
def hide(carrier,msg):
    carrierbits = getbits(carrier,0,6)
    msgbits = getbits(msg,0,2)

    carrierbits = putemtogehter(carrierbits, msgbits)
    width = 640
    height = 434
    size = (width,height)
    data = [int(byte,2) for byte in carrierbits]
    data = bytes(data)

    carrier = Image.frombytes("RGB", size, data, decoder_name='raw')
    carrier.save("carrier.png")


def extract(img):
    bits = getbits(img,6,8)
    i = 0
    for i in range(len(bits)):
        bits[i] = bits[i] + "000000"
    width = 640
    height = 434
    size = (width, height)
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
