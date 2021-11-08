from PIL import Image
im = Image.open('1635500514589.jpg')
print(im.format, im.size, im.mode)
im.show()
