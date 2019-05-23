from PIL import Image
import random
import sys

img_name = sys.argv[1]

im = Image.open(img_name) # Can be many different formats.
pix = im.load()

h,w = im.size  # Get the width and hight of the image for iterating over
numpix = h*w

numblack = (0,0,0,255)

for i in range(h):
        for j in range(w):
                pix[i,j] = numblack if (sum(pix[i,j]) < 555 and all([z < 100 for z in list(pix[i,j][:3])])) else pix[i,j]


im.save(img_name.split('.')[0] + "_amoledified." + img_name.split('.')[1])
