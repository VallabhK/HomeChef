# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:17:31 2021

@author: memoh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome('C:/Users/memoh/Downloads/chromeDriverTest/chromedriver_win32/chromedriver')
driver.get('https://www.youtube.com/')
text_box = driver.find_element_by_id("search")
text_box.send_keys("avocado on toast recipe")
search_button = driver.find_element_by_id("search-icon-legacy")
search_button.click()
time.sleep(5)
#user_data = driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a ')
user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
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
print(rows)

#fout=open("C:/Users/memoh/OneDrive/Desktop/DFP/Project/Video_Recipe_Table.txt",mode="wt",encoding="utf-8")
df_1 = pd.DataFrame(rows, columns=["Video Name", "Video Link"])
dfAsString_1 = df_1.to_string(header=True, index = False)
df_1.to_csv("C:/Users/memoh/OneDrive/Desktop/DFP/Project/Video_Recipe_Table.csv")
#fout.close()
    


