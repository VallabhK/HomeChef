"""
# Data Focused Python B1
# Created by: 
# 1. Vallabh Karanjkar-vkaranjk
# 2. Mohini Jain- mohinij
# 3. Rohit Jain- rohitj
# Group 24
"""
import matplotlib.pyplot as plt
import numpy as np
import v5_pdf_scraping as pdfs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def youtubeScraper(recipeData):
    recipe_list = []
    recipeLinks = ''
    counter = 0

#loop to run Youtube the number of times as the number of recipes
    for i in recipeData[1]:
        counter += 1
        #opens chrome
        Ydriver = webdriver.Chrome(r'./chromedriver_win32/chromedriver.exe')
        #navigates to Youtube
        Ydriver.get('https://www.youtube.com/')
        Ydriver.minimize_window()
        WebDriverWait(Ydriver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='search_query']"))).send_keys(i)

        search_button = Ydriver.find_element_by_id("search-icon-legacy")
        search_button.click()
        time.sleep(5)
        user_data = Ydriver.find_elements_by_xpath('//*[@id="video-title"]')
        links = []
        names = []
        for i in user_data:
            if i.get_attribute('href') != None:
                links.append(i.get_attribute('href'))
            if i.get_attribute('title') != '':
                names.append(i.get_attribute('title'))
                rows = []
                for i in range(len(links)):
                    rows.append([names[i], links[i]])
        #get the links in the list
        if (len(recipeData[1]) == 3):
           recipeLinks += links[0] +","
        elif (len(recipeData[1]) == 2):
            if(counter==2):
                recipeLinks += links[0] +"," + links[1] + ","
            elif(counter==1):
                recipeLinks += links[0] +","
        elif (len(recipeData[1]) == 1):
           recipeLinks += links[0] +"," + links[1] + "," + links[2]+","
        #close the webdriver
        Ydriver.close()
    return recipeLinks