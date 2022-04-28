import os
import random
import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# import numpy as np
# import time
# from selenium import webdriver 
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome('/driver/chromedriver')

# s = Service('D:\Aryan\Python\allumni\driver\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.youtube.com/")


browser.get("https://www.linkedin.com/login/")

file = open("config.txt")
line = file.readlines()
username = line[0]
password = line[1]


# elementID = browser.find_element_by_id('username')
elementID = browser.find_element(By.ID, 'username')
elementID.send_keys(username)
# elementID = browser.find_element_by_id('password')
elementID = browser.find_element(By.ID, 'password')
elementID.send_keys(password)
elementID.submit()


browser.get('https://www.linkedin.com/school/svnit/people/')

time.sleep(5)

rep = 10  # determine the rep enough to scroll all the page
last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(rep):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    new_height = last_height

src = browser.page_source
soup = BeautifulSoup(src, 'lxml')

pav = soup.find('div', {'class': 'artdeco-card pv5 pl5 pr1 mt4'})
# artdeco-card pv5 pl5 pr1 mt4
all_links = pav.find_all(
    'a', {'class': 'app-aware-link'})

profilesID = set()
for link in all_links:
    profilesID.add(link.get('href'))


dicti = {'links': profilesID}

df = pd.DataFrame(dicti)

df.to_csv('res.csv')
