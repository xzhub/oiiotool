#!/usr/local/bin/python
from oiio import OpenImageIO as oiio
import json
import sys
import os


def remove_model(img):
    buf = oiio.ImageBuf(img)
    Make = buf.spec().get_string_attribute("Make")
    Model = buf.spec().get_string_attribute("Model")
    print(f"Removing Make: {Make}, Model: {Model}")
    buf.spec().attribute("Make", "there_is_no")
    buf.spec().attribute("Model", "such_model")
    buf.write(img)


if (len(sys.argv) < 2):
    print(f"sys.argv[0] img_files ...")
    exit(1)

for i in range(len(sys.argv) - 1):
    infile = sys.argv[i + 1]

    remove_model(infile)
