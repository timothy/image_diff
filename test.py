from PIL import Image, ImageChops


img1 = Image.open('./1.png').convert('RGB')
img2 = Image.open('./2.png').convert('RGB')

img3 = Image.open('./A.jpg')
img4 = Image.open('./B.jpg')
diff1 = ImageChops.difference(img3, img4)
diff = ImageChops.difference(img2, img1)

print(diff.getbbox())
if diff.getbbox():
    diff.show()

print(diff1.getbbox())

if diff1.getbbox():
    diff1.show()
