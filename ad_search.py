import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


########

def addi(arr, soupi):
    if soupi:
        arr.append(" ".join(soupi.get_text().split()))
        # print(arr)
        return
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


# def add_from_page(soup):
#     boxes = soup.find_all(
#         'div', class_='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light')

#     for box in boxes:
#         info_box0 = box.find('div', class_='mb1')
#         if info_box0:
#             a_link = info_box0.find('a')
#             if a_link:
#                 hrefs.append(a_link['href'])
#                 print(hrefs)
#             else:
#                 hrefs.append(None)
#                 print("href None")

#             if a_link:
#                 name_span = a_link.find('span', attrs={'aria-hidden': 'true'})
#                 addi(names, name_span)
#             else:
#                 names.append("None")
#         else:
#             hrefs.append("None")
#             names.append("None")

#         about_div = box.find(
#             'div', class_='entity-result__primary-subtitle t-14 t-black t-normal')
#         addi(abouts, about_div)

#         loc_div = box.find(
#             'div', class_='entity-result__secondary-subtitle t-14 t-normal')
#         addi(locations, loc_div)
########
s = Service('D:\Aryan\Python\allumni\driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)

url0 = 'https://www.linkedin.com/search/results/people/?'
# curr_comp
url = input("Enter url...   ")
driver.get("https://www.linkedin.com/login/")

file = open("config.txt")
line = file.readlines()
username = line[0]
password = line[1]


# elementID = driver.find_element_by_id('username')
elementID = driver.find_element(By.ID, 'username')
elementID.send_keys(username)
# elementID = driver.find_element_by_id('password')
elementID = driver.find_element(By.ID, 'password')
elementID.send_keys(password)
elementID.submit()

driver.get(url)
time.sleep(5)

# src = driver.page_source
# soup = BeautifulSoup(src, 'lxml')


# file = open('search_box.html', encoding="utf8")
# content = file.read()
# # print(content)

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

total_res_div = soup.find('h2', class_='pb2 t-black--light t-14')
total_res = int(total_res_div.get_text().split()[0])
print(total_res)
round = (total_res+9)//10

names = []
abouts = []
locations = []
hrefs = []

add_from_page(soup)
curr_round = 2
while curr_round <= round:
    new_url = url+"&page="+str(curr_round)
    driver.get(new_url)
    time.sleep(10)
    add_from_page(BeautifulSoup(driver.page_source, 'lxml'))
    curr_round += 1

print(len(names), len(locations), len(abouts), len(hrefs))
print(len(names) == total_res)

for i in range(total_res):
    print(names[i], locations[i], abouts[i])

comb = [names, locations, abouts, hrefs]
# comb = zip([names, locations, abouts, hrefs])

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(comb)

# soup = BeautifulSoup(content, 'lxml')

# search-container = soup.find('div', class_='search-results-container')
