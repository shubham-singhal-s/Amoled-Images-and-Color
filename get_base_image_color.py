from PIL import Image
import random

im = Image.open('d.png') # Can be many different formats.
pix = im.load()
h,w = im.size  # Get the width and hight of the image for iterating over
numpix = h*w
print(pix[h-10,w-1])
numblack = (0,0,0)
nums = {}
for i in range(h):
        for j in range(w):
                nums[pix[i,j]] = 1 if pix[i,j] not in nums else nums[pix[i,j]] + 1

nums = sorted(nums.items(), key=lambda x: x[1])
cols = nums[:3]
col = (0,0,0,0)
for it in cols:
        a = it[0]
        col = tuple(map(sum, zip(a, col)))

col = tuple(int(ti/3) for ti in col)
for i in range(h):
        for j in range(w):
                pix[i,j] = col

im.save('base_color.png')
