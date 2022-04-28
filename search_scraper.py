import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Functions

def add_item(arr, soupi):
    if soupi:
        arr.append(" ".join(soupi.get_text().split()))
        return
    arr.append(None)


def add_from_page(soupi):
    boxes = soupi.find_all(
        'div', class_='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light')

    time_taken = 0
    while not boxes and time_taken < 30:
        time.sleep(5)
        time_taken += 5
        boxes = soupi.find_all(
            'div', class_='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light')

    for box in boxes:
        profile = []
        title_div = box.find('div', class_='t-roman t-sans')
        link_div = title_div.find('a')

        # names
        if link_div:
            name_span = link_div.find('span', attrs={'aria-hidden': 'true'})
            add_item(profile, name_span)
        else:
            profile.append(None)
            print("link_div not found - names None")

        # abouts
        about_div = box.find(
            'div', class_='entity-result__primary-subtitle t-14 t-black t-normal')
        add_item(profile, about_div)

        # locations
        loc_div = box.find(
            'div', class_='entity-result__secondary-subtitle t-14 t-normal')
        add_item(profile, loc_div)

        # href
        if link_div:
            profile.append(link_div['href'])
        else:
            profile.append(None)
            print("link_div not found - hrefs None")

        profiles.append(profile)


def log_in(usr, pwd):
    driver.get("https://www.linkedin.com/login/")
    elementID = driver.find_element(By.ID, 'username')
    elementID.send_keys(usr)
    elementID = driver.find_element(By.ID, 'password')
    elementID.send_keys(pwd)
    elementID.submit()

########


chrome_driver_path = input("Enter absolute path of chrome driver \n")
url = input("Enter the Search URL\n")
output_file = input("Enter the name of output file\n")

s = Service(chrome_driver_path) if chrome_driver_path else Service(
    'D:\Aryan\Python\allumni\driver\chromedriver.exe')

driver = webdriver.Chrome(service=s)

file = open("config.txt")
line = file.readlines()
log_in(line[0], line[1])

driver.get(url)
time.sleep(10)

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

total_res_div = soup.find('h2', class_='pb2 t-black--light t-14')

time_taken = 10
while not total_res_div and time_taken < 30:
    time.sleep(5)
    total_res_div = soup.find('h2', class_='pb2 t-black--light t-14')
    time_taken += 5

total_res = int(total_res_div.get_text().split()[0])
total_page = (total_res+9)//10

print("Total number of results are", total_res)
print("Total number of pages are", total_page)

profiles = []
add_from_page(soup)

for curr_page in range(2, total_page+1):
    new_url = url+"&page="+str(curr_page)
    driver.get(new_url)
    time.sleep(10)
    new_src = driver.page_source
    new_soup = BeautifulSoup(new_src, 'lxml')
    add_from_page(new_soup)

driver.quit()

print(len(profiles), "Profiles scraped successfully")
print(total_res-len(profiles), "Profiles failed")


with open(output_file, 'w', newline='', encoding="utf-8") as f:
    wr = csv.writer(f)
    wr.writerows(profiles)
