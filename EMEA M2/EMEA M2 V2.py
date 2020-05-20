import unittest
import time
import datetime
from threading import Thread
import csv

from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import pytesseract
from PIL import Image
from nltk import word_tokenize
from nltk.corpus import stopwords


def read():
    with open('input.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        input = []
        for row in csv_reader:
            # print(f'\t{row[0]}')
            # print(f'\t{row[3]}')
            input.append(row[3])
            line_count += 1
        # print(f'Processed {line_count} lines. {len(input)}')
        return input


def get_captcha_text(location, size, adjust):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    im = Image.open('screenshot1.png')
    left = location['x'] + adjust[0]
    top = location['y'] + adjust[1]
    right = left + size['width'] + adjust[2]
    bottom = top + size['height'] + adjust[3]

    im = im.crop((left, top, right, bottom))
    im.save('screenshot2.png')
    captcha_text = pytesseract.image_to_string(Image.open('screenshot2.png'))
    return captcha_text


class EMEAM2(unittest.TestCase):
    # region testGeoPopup
    def testGeoPopup(self):
        self.assertIsInstance(self.geo_popup, object, "Geo Popup is not detected.")
    # endregion

    # region testGeoPopupFlag
    def testGeoPopupFlag(self):
        # Xpath of image
        image_src = self.driver.find_element_by_xpath(self.input[31]).get_attribute("src")
        temp = image_src.split("/")
        # Get the last element of xpath to get the name of image
        image = temp[len(temp) - 1]
        self.assertTrue(self.input[32] in image, "Flag image not detected or wrong image name.")

if __name__ == "__main__":
    unittest.main()
