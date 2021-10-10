# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:06:32 2021

@author: memoh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome(r'C:\Users\memoh\Downloads\chromedriver_win32 (1)\chromedriver.exe')
search_string = "potato calorie content"
driver.get("https://www.google.com/search?q=" + search_string)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))).send_keys("potato calorie content")
#text_box = driver.find_element_by_id("search")
#text_box.send_keys("avocado on toast recipe")
calorie_data_element = driver.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/form/div[1]/div')[0]
calorie_data = calorie_data_element.text
print(calorie_data)
fat_data_element = driver.find_elements_by_xpath('/html/body/div[7]/div/div[9]/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr[2]/td[1]')[0]
fat_data = fat_data_element.text
print(fat_data)
carb_data_element = driver.find_elements_by_xpath('/html/body/div[7]/div/div[9]/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr[7]/td[1]')[0]
carb_data = carb_data_element.text
print(carb_data)
protein_data_element = driver.find_elements_by_xpath('/html/body/div[7]/div/div[9]/div[2]/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/table[1]/tbody/tr[10]/td[1]')[0]
protein_data = protein_data_element.text
print(protein_data)



