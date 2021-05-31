from PIL import Image

img = Image.open('150x150.png')

width, height = img.size

kx = 256 / width  # коэф для пересчета
ky = 256 / height

for y in range(width):
        for x in range(height):
                clr1 = int(ky * y)
                clr2 = int(kx * x)
                if x < y:
                        r, g, b = x+y, y, 0
                if x > y:
                        r, g, b = x+y, x, 0
                if x == y:
                        r, g, b = x+y, (x+y)//2, 0
                if x >= 130 and x <= 150 and y <= 150 and y >= 130: # right-down
                        r, g, b = 0, 0, 0
                if x >= 130 and x <= 150 and y <= 20 and y >= 0: # right-up
                        r, g, b = 0, 0, 0
                if x >= 0 and x <= 20 and y <= 20 and y >= 0: # left-up
                        r, g, b = 0, 0, 0
                if x >= 0 and x <= 20 and y >= 130 and y <= 150: # left-down
                        r, g, b = 0, 0, 0
                if (x >= 30 and x <= 45 and y >= 30 and y <= 45) or (x <= 120 and x >= 105 and y >= 30 and y <= 45):  #left and right eyes
                        r, g, b = 0, 0, 0
                if (x >= 30 and x <= 37 and y >= 30 and y <= 37) or (x <= 112 and x >= 105 and y >= 30 and y <= 37): # зрачки белые
                        r, g, b = 255, 255, 255                                                                       
                if (x <= 30 and x >= 15 and y >= 115 and y <= 130) or (x >= 120 and x <= 135 and y >= 115 and y <= 130): #края рта
                        r, g, b = 0, 0, 0
                if y >= 120 and y <= 135 and x <= 120 and x >= 30: # рот
                        r, g, b = 0, 0, 0
                if x <= 80 and x >= 75 and y >=60 and y <= 80: #нос
                        r, g, b = 0, 0, 0
                if x <= 85 and x >= 70 and y <=90 and y >= 70: # нос 2
                        r, g, b = 0, 0, 0
                        
                img.putpixel((x, y), (r, g, b))

img.show()
