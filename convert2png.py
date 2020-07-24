#!/usr/local/bin/python
from oiio import OpenImageIO as oiio
import sys
import os


def convert(img):
    filename, ext = os.path.splitext(img)
    outfile = filename + ".png"
    if ext == '.png':
        return
    if ext in ['.PNG']:        
        os.rename(img, outfile)
    else:
        buf = oiio.ImageBuf(img)
        buf.write(outfile)
        os.remove(img)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"sys.argv[0] image_folder/")
        exit(1)

    folder = sys.argv[1]
    files = os.listdir(folder)
    for f in files:
        convert(os.path.join(folder, f))
