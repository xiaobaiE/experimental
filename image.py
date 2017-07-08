#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PIL import Image
import  argparse

parser=argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('--width',type=int,default=100)
parser.add_argument('--height',type=int,default=60)
args=parser.parse_args()

fileName=args.file
WIDTH=args.width
HEIGHT=args.height

txt=''

def transfer(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    ascii_char=list('334idntidmebghodnbfwodfgnojdjljfaj ')
    grey=int(0.2126*r+0.7152*g+0.0722*b)
    length=len(ascii_char)
    return ascii_char[int(grey/257.0*length)]

if __name__=='__main__':
    im=Image.open(fileName)
    im= im.resize((WIDTH,HEIGHT),Image.NEAREST)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=transfer(*im.getpixel((j,i)))
        txt+='\n'
    print txt
