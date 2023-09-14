# pip install tesseract

import pytesseract
from PIL import Image

# img = Image.open('kaptcha.jpg')


print(pytesseract.image_to_string(Image.open('kaptcha2.jpeg'),lang='eng'))
print(pytesseract.image_to_string('kaptcha2.jpeg'))

