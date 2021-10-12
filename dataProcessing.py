# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:17:31 2021

@author: memoh
"""
import pdfScraping as pdfs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def youTubeSearch(recipeNames):
    
    recipe_list = []

    for i in recipeNames:
        Ydriver = webdriver.Chrome(r'./chromedriver_win32/chromedriver.exe')
        Ydriver.get('https://www.youtube.com/')
        Ydriver.minimize_window()
        WebDriverWait(Ydriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='search_query']"))).send_keys(i)

        search_button = Ydriver.find_element_by_id("search-icon-legacy")

        search_button.click()
        time.sleep(5)
        user_data = Ydriver.find_elements_by_xpath('//*[@id="video-title"]')
        print('here')
        links = []
        names = []
        for i in user_data:
            if i.get_attribute('href')!=None:
                links.append(i.get_attribute('href'))
            if i.get_attribute('title')!='':
                names.append(i.get_attribute('title'))
                rows=[]
                for i in range (len(links)):
                    rows.append([names[i], links[i]])

        if(len(recipeNames) == 3):
            recipe_list.append(links[0])
        elif (len(recipeNames) == 2):
            recipe_list.append(links[0])
            recipe_list.append(links[1])
        elif (len(recipeNames) == 1 ):
            recipe_list.append(links[0])
            recipe_list.append(links[1])
            recipe_list.append(links[2])

        Ydriver.close()

    return recipe_list
    
def getCalorieData(searchString):
  
    search_string = searchString + ' calorie content'
    driver = webdriver.Chrome(r'./chromedriver_win32/chromedriver.exe')
    
    driver.get("https://www.google.com/search?q=" + search_string)
    calorie_data_element = driver.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/form/div[1]/div')[0]
    calorie_data = calorie_data_element.text
    Nutrition_data = driver.find_elements_by_xpath('/html/body/div[7]/div/div[9]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/table[1]/tbody')[0]
    s = Nutrition_data.text
    Nutrition_list = s.split("\n")
    e = []    
    for j in Nutrition_list:
        if(j.strip() !=''):
            e.append(j.strip())
    
    Nutrition_main_List = []
    Nutrition_main_List.append(calorie_data)
    Nutrition_main_List.append(e[1])
    Nutrition_main_List.append(e[6])
    Nutrition_main_List.append(e[8])  
    driver.close()
    
    return Nutrition_main_List[0],Nutrition_main_List[1],Nutrition_main_List[2],Nutrition_main_List[3],Nutrition_main_List[4]
    


