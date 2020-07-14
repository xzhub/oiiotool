#!/usr/local/bin/python
from oiio import OpenImageIO as oiio
import sys


def report_size(source):
    try:
        buf = oiio.ImageBuf(source)
        spec = buf.spec()
        w = spec.width
        h = spec.height
        m = max(w, h)
        return m
    except BaseException as e:
        print(f"Get size failed: {e}")


if __name__ == "__main__":

    if (len(sys.argv) < 2):
        print(f"sys.argv[0] img_file")
        exit(1)

    filename = int(sys.argv[1])
    size = report_size(filename)
    print(size)
