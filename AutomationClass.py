import os
import time
from selenium import webdriver

class AutomationClass:
	"""
		AutomationClass achieves following tasks:
			- Initiate the Firefox webdriver and visit the website
			- Capture a screenshot of a particular HTML element
			- Store a captured screenshot in directory initially created by ImageCapture
			- Store screenshots in PNG format
	"""
	def __init__(self):
		self.driver = webdriver.Firefox()

		self.automation_script()

		self.scrnshot()

	def automation_script(self):
		self.driver.get("https://public.tableau.com/views/COVID-19CasesandDeathsinthePhilippines_15866705872710/Home?:language=en&:display_count=y&:origin=viz_share_link")
		time.sleep(5)

	#screenshots the needed data and moves to file/date dir
	def scrnshot(self):
		self.driver.find_element_by_id('primaryContent').screenshot('date_cases_capiz.png')
		self.driver.close()
