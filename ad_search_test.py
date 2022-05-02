import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def addi(arr, soupi):
    if soupi:
        arr.append(" ".join(soupi.get_text().split()))
        return
    print("appended None", arr)
    arr.append(None)


def add_from_page(soupi):
    boxes = soupi.find_all(
        'div', class_='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light')

    for box in boxes:
        title_div = box.find('div', class_='t-roman t-sans')
        link_div = title_div.find('a')

        # names
        if link_div:
            name_span = link_div.find('span', attrs={'aria-hidden': 'true'})
            addi(names, name_span)
        else:
            names.append(None)
            print("link_div not found - names None")

        # href
        if link_div:
            hrefs.append(link_div['href'])
        else:
            hrefs.append(None)
            print("link_div not found - hrefs None")

        # abouts
        about_div = box.find(
            'div', class_='entity-result__primary-subtitle t-14 t-black t-normal')
        addi(abouts, about_div)

        # locations
        loc_div = box.find(
            'div', class_='entity-result__secondary-subtitle t-14 t-normal')
        addi(locations, loc_div)


file = open('search_box.html', encoding="utf8")
content = file.read()

soup = BeautifulSoup(content, 'lxml')


names = []
abouts = []
locations = []
hrefs = []

add_from_page(soup)

print(len(names), len(abouts), len(locations), len(hrefs))

for i in range(len(names)):
    print(names[i], abouts[i])
