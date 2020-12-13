import os
from datetime import datetime
from ImageCapture import ImageCapture
from AutomationClass import AutomationClass


class ScreenshotSel:
	"""
		ScreenshotSel class performs following:
			- Creates object for ImageCapture and AutomationClass
			- Invokes ImageCapture class to create directories
			- Invokes AutomationClass constructor to get screenshot
			- Invokes extract_data of ImageCapture to extract the information
			- Writes extracted info in text file.
	"""
	def __init__(self):
		self.root_dir = os.getcwd()
		self.image_cap = ImageCapture()
	
	def main(self):	
		os.chdir(self.root_dir)
		# with open('data.txt', 'r') as file:
		# 	for line in file.readlines():
		# 		print(line)
		# 		print('\n')
		self.process_begin()
		data_dict = self.image_cap.extract_data()
		print(data_dict)

		user_choice = input('Write data? y/n')
		if user_choice == 'y':
			# appends to txt file in root folder for future purposes
			self.image_cap.write_to_file(data_dict)


	def process_begin(self):
		self.image_cap.set_directory()
		folder_name = self.image_cap.folder_date()
		process_image = AutomationClass()
		

if __name__ == '__main__':
	sel_obj = ScreenshotSel()
	sel_obj.main()
