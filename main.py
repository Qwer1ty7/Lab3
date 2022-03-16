from PIL import Image
import pytesseract
from matplotlib import pyplot as plt
import numpy as np

def process_image(image_path, lang_code):
	img = Image.open(image_path)
	plt.figure(figsize = (50, 50))
	plt.imshow(img, interpolation='nearest')
	return pytesseract.image_to_string(img, lang = lang_code)


def main():
	text_eng = process_image("test.png", "eng")
	print(text_eng)

main()