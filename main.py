# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    img = Image.open('wolf.bmp')
    rgb_im = img.convert('RGB')
    for row in range(10):
        first_row = [rgb_im.getpixel((i, row)) for i in range(rgb_im.size[0])]
        print(first_row)
        print(first_row.count((0, 0, 0)))
        print(len(first_row))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Sebastian')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
