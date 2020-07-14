#!/usr/local/bin/python
from oiio import OpenImageIO as oiio
import sys

def inplace_resize(source, goal_width=100, goal_height=100):
    #resize to 100 x 100
    print(f"working on {source}")
    try:
        buf = oiio.ImageBuf(source)
        spec = buf.spec()
        w = spec.width
        h = spec.height
        # https://openimageio.readthedocs.io/en/latest/imagebuf.html
        if (w == 0 or h == 0):  #not a good photo
            return False

        if float(h) > 0:
            aspect = float(w) / float(h)
            if aspect >= 1.0:
                # source image is landscape (or square)
                goal_height = int(h * goal_height / w)
            else:
                # source image is portrait
                goal_width = int(w * goal_width / h)

        # resized = oiio.ImageBuf(spec)    
        resized = oiio.ImageBuf(
            oiio.ImageSpec(goal_width, goal_height, spec.nchannels, spec.format))    
        
        oiio.ImageBufAlgo.resize(resized, buf)       

        #orientaion
        resized.orientation = buf.orientation

        #make/model
        Make = buf.spec().get_string_attribute("Make")
        Model = buf.spec().get_string_attribute("Model")
        resized.spec().attribute("Make", Make)
        resized.spec().attribute("Model", Model)

        resized.write(source)

        
    except BaseException as e:
        print(f"Resize failed: {e}")

    return True


if __name__ == "__main__":

    if (len(sys.argv) < 3):
        print(f"sys.argv[0] max_w_h_size img_files ...")
        exit(1)

    size=int(sys.argv[1])
    for i in range(len(sys.argv) - 2):
        infile = sys.argv[i + 2]

        inplace_resize(infile,size,size)