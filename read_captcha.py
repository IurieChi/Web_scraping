# pip install tesseract

import cv2
import easyocr
import pandas as pd



def read_captchea(object):
    
    image = cv2.imread(object)

    reader = easyocr.Reader(['en'],gpu= False)

    result = reader.readtext(image, detail=1, paragraph= False)
    return result


# print(result[0][1])

# if result[0][2] >= 0.90:
#     name = result[0][1]
#     print(name)

# else:
#     print(result)
