from PIL import Image

img = Image.open('256x400.png')

width, height = img.size

#kx = 256 / width  # коэф для пересчета
ky = 256 / height

for x in range(width):
        for y in range(height):
                clr1 = int(ky * y)
                #clr2 = int(kx * x)
                if clr1 > x:
                        r, g, b = x-clr1, clr1-x, x+clr1
                if x >= clr1:
                        r, g, b = x+clr1, x-clr1, clr1-x
#r, g, b = clr1, y//2, y//4
#if x <= 128 and x > 64:
#r, g, b = y//2, y//4, clr1
#if x <= 192 and x > 128:
#r, g, b = y//4, clr1, y//2
#if x > 192:

                img.putpixel((x, y), (r, g, b))

img.show()
