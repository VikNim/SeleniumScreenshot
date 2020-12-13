import locale
locale.setlocale(locale.LC_ALL, 'C')
import os
import cv2
import numpy as np
import pytesseract as tess
from datetime import datetime
from tesserocr import PyTessBaseAPI


class ImageCapture:
	"""
		ImageCapture class performs following tasks
			- creates directories according to date
			- reads newly saved screenshot
			- Extracts data from image using PyTesseract
		Future Enhancement:
			- Extract data using TesserOCR api along with tessdata_best approach

	"""
	def __init__(self):
		self.root = os.getcwd()
		self.date = datetime.now()

	def set_directory(self):
		try:
			if not os.getcwd() == self.root:
				os.chdir(self.root)
			if not os.path.exists('files'):
				os.makedirs('files')
				os.chdir('files')
			else:
				os.chdir('files')
		except:
			raise FileNotFoundError
	
	def folder_date(self):
		file_path = os.getcwd()
		if self.root == file_path:
			set_directory()
			file_path = os.getcwd()

		list_dirs = os.listdir()
		folder_name = self.date.strftime('%m-%d-%Y')
		
		if not os.path.exists(folder_name):
			os.mkdir('{}/{}'.format(file_path, folder_name))
			os.chdir(folder_name)
		else:
			os.chdir(folder_name)
		return folder_name

	def write_to_file(self, data):
		os.chdir(self.root)
		with open('data.txt', 'a') as file:
			file.write(str(data) + '\n')

	def image_preproc(self, image):
		# greyimg = ImageOps.grayscale(img)
		# invertimg = ImageOps.invert(greyimg)
		# sharpimg = ImageEnhance.Sharpness(invertimg)
		# factor = 1.25
		# sharpened = sharpimg.enhance(factor)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		threshold_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		return threshold_img
	
	def extract_data(self):
		files = os.listdir()
		data = dict()
		data['_id'] = self.date.strftime('%m-%d-%Y')
		for _file in files:
			if _file.endswith('.png'):
				img = cv2.imread(_file)
				img = self.image_preproc(img)
				text = tess.image_to_string(img, config="--oem 3 --psm 6", lang='eng')
				# print("Path: "+ self.root + '/tessdata/.')
				# with PyTessBaseAPI(path=self.root + '/tessdata_best/.', lang='eng') as api:
				# 	api.SetImageFile(_file)
				# 	text = api.GetUTF8Text()
				data['{}'.format(_file.strip('.png'))] = text.split()
		return data
