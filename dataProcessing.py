# -*- coding: utf-8 -*-
"""
# Data Focused Python B1
# Created by: 
# 1. Vallabh Karanjkar-vkaranjk
# 2. Mohini Jain- mohinij
# 3. Rohit Jain- rohitj
# Group 24
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def getCalorieData(search_string):
    #open chrome
    driver = webdriver.Chrome(r'./chromedriver_win32/chromedriver.exe')
    search_string = search_string + " calorie content"
    #add the search strig in the link to directly reach on the page
    driver.get("https://www.google.com/search?q=" + search_string)
    #select the data to extract via xpath
    calorie_data_element = driver.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/form/div[1]/div')[0]
    calorie_data = calorie_data_element.text
    try:
        Nutrition_data = driver.find_elements_by_xpath('/html/body/div[7]/div/div[9]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/table[1]/tbody')[0]
        s = Nutrition_data.text
        #print(s)
        Nutrition_list = s.split("\n")
        e = []
        for j in Nutrition_list:
            if (j.strip() != ''):
                e.append(j.strip())
        #add if data is found
        Nutrition_main_List = []
        Nutrition_main_List.append(calorie_data)
        Nutrition_main_List.append(e[1])
        Nutrition_main_List.append(e[6])
        Nutrition_main_List.append(e[9])
    except:
        Nutrition_main_List = []
        #customize list if data not found as per xpath
        Nutrition_main_List.append(calorie_data)
        Nutrition_main_List.append("")
        Nutrition_main_List.append("")
        Nutrition_main_List.append("No other data found")

    driver.close()

    return Nutrition_main_List


