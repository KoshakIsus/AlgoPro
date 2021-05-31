from PIL import Image


def get_image_resize(img, height_new):  # изменение размера
   width, height = img.size
   width_new = width // (height//height_new)
   img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
   return img_new


def get_image_symbols(img_new):
   count = len(symbols)
   full = 256 * 256 * 256  # максимальное значение
   segment = int(full // count)  # длина сегмента
   result = ''
   width, height = img_new.size
   for y in range(height):
      for x in range(width):
         r, g, b = img_new.getpixel((x, y))
         if inv_clr == 1:
            color = (255-r) * (255-g) * (255-b)
         if inv_clr == 2:
            color = r * g * b
         pos = color // segment
         result += symbols[pos] * 2
      result += '\n'
   picture.append(result)
   return result


def invert_sides_LR(result):  # отражение по горизонтали (левое с правым)
   inv_sides_lr = input("Отразить по горизонтали?\n"
"1 = да\n"
"2 = нет\n")

   if inv_sides_lr == 1:
      f1 = 'empty_file.txt'
      with open(f1, 'r') as fr, open(f1, 'w') as fw:
         picture = fr.read()
         for y in range(len(picture)):
            for x in range(len(picture)-1, 0, -1):  # меняем порядок символов (шаг -1, т.е. все символы задом наперёд)
               fw.write(picture[y][x]) 
         #fr.close()
         #fw.close()


def invert_sides_UD(result):  # отражение по вертикали (вверх ногами)
   inv_sides_ud = input("Отразить по вертикали?\n"
"1 = да\n"
"2 = нет\n")

   if inv_sides_ud == 1:
      f2 = 'empty_file.txt'
      with open(f2, 'r') as fr2, open(f2, 'w') as fw2:
         picture = fr2.read()
         for x in range(len(picture)):
            for y in range(len(picture)-1, 0, -1):
               fw2.write(picture[x][y])
         #fr2.close()
         #fw2.close()

# выводим файл
def final_file():
   empty_file = 'empty_file.txt'
   final = open(empty_file, mode='w', encoding='utf-8')
   final.writelines(result)
   final.close()


picture = []  # picture <= result, чтобы не менять сам result


name_image = 'doge.jpeg'  # берем картинку и меняем размер
img = Image.open(name_image)
img_new = get_image_resize(img, 75)

# инверсия цвета
inv_clr = int(input("Инвертировать цвет?\n"
"1 = да\n"
"2 = нет\n"))

symbols = ' .-=*|8#▓█'  # указывает символы
result = get_image_symbols(img_new)  # делаем дело

final_file()
                             
# Инвертировать стороны? 

invert_sides_LR(result)
invert_sides_UD(result)
