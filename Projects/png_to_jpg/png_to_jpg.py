from PIL import Image

im = Image.open("colors.png")
rgb_im = im.convert("RGB")
rgb_im.save("colors.jpg")
