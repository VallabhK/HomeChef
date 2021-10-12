# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:17:31 2021

@author: memoh
"""
import PDF_Scraping as pdfs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

search_string = pdfs.search_string + ' calorie content'
search_input = pdfs.get_recipe(string)
recipe_list = []
print(search_input[1])
for i in search_input[1]:
    Ydriver = webdriver.Chrome(r'C:\Users\memoh\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    Ydriver.get('https://www.youtube.com/')
    WebDriverWait(Ydriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='search_query']"))).send_keys(i)
    #text_box = driver.find_element_by_id("search")
    #text_box.send_keys("avocado on toast recipe")
    search_button = Ydriver.find_element_by_id("search-icon-legacy")
    search_button.click()
    time.sleep(5)
    #user_data = driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a ')
    user_data = Ydriver.find_elements_by_xpath('//*[@id="video-title"]')
    links = []
    names = []
    for i in user_data:
        if i.get_attribute('href')!=None:
            links.append(i.get_attribute('href'))
        if i.get_attribute('title')!='':
            names.append(i.get_attribute('title'))
            rows=[]
            for i in range (len(links)):
                rows.append([names[i],links[i]])
    recipe_list.append([names[0],links[0]])
    Ydriver.close()    




driver = webdriver.Chrome(r'C:\Users\memoh\Downloads\chromedriver_win32 (1)\chromedriver.exe')

driver.get("https://www.google.com/search?q=" + search_string)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))).send_keys("potato calorie content")
#text_box = driver.find_element_by_id("search")
#text_box.send_keys("avocado on toast recipe")
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
print(Nutrition_main_List) 
driver.close()
    


