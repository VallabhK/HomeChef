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
    for i in recipeData[1]:
        Ydriver = webdriver.Chrome(r'./chromedriver_win32/chromedriver.exe')
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
        # recipe_list.append(links[0])
        # if (len(search_input[1]) == 3):
        #    recipe_list.append(links[0])
        #    print(recipe_list)
        # elif (len(search_input[1]) == 2):
        #    recipe_list.append(links[0])
        #    recipe_list.append(links[1])
        #    print(recipe_list)
        # elif (len(search_input[1]) == 1):
        #    recipe_list.append(links[0])
        #    recipe_list.append(links[1])
        #    recipe_list.append(links[2])
        #    print(recipe_list)
        Ydriver.close()
        return links