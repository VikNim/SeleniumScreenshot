# SeleniumScreenshot
The small project to capture screens and extract data using pytesseract

I have built a mini project using Selenium and Pytesseract.
The purpose of the project is to capture a screenshot of websire elements using Selenium Webdriver and save them in png format.
Interpret the saved images one by one and extract the data using Pytesseract.


ScreenshotSel is a main class and it begins the process:
      - Creates object for ImageCapture and AutomationClass
      - Invokes ImageCapture class to create directories
      - Invokes AutomationClass constructor to get screenshot
      - Invokes extract_data of ImageCapture to extract the information
      - Writes extracted info in text file.

AutomationClass achieves following tasks:
			- Initiate the Firefox webdriver and visit the website
			- Capture a screenshot of a particular HTML element
			- Store a captured screenshot in directory initially created by ImageCapture
			- Store screenshots in PNG format

ImageCapture class performs following tasks
			- creates directories according to date
			- reads newly saved screenshot
			- Extracts data from image using PyTesseract

Future Enhancement:
			- Extract data using TesserOCR api along with tessdata_best approach(Link: https://github.com/tesseract-ocr/tessdata_best)

This mini project can be used for individual purpose as well. Alter a website name and HTML element and you will be able to extract data from it.

Please reach me out at: nimbalkarvicky9@gmail.com for anything !
