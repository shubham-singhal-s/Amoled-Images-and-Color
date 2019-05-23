from PIL import Image
import random
import sys

img_name = sys.argv[1]

im = Image.open(img_name) # Can be many different formats.
pix = im.load()

h,w = im.size  # Get the width and hight of the image for iterating over
numpix = h*w

numblack = 0

for i in range(h):
        for j in range(w):
                if all([z == 0 for z in list(pix[i,j][:3])]):
                    numblack+=1


print(str((numblack/numpix)*100) + "%")
