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



def log_in(usr, pwd):
    driver.get("https://www.linkedin.com/login/")
    elementID = driver.find_element(By.ID, 'username')
    elementID.send_keys(usr)
    elementID = driver.find_element(By.ID, 'password')
    elementID.send_keys(pwd)
    elementID.submit()


def connect(soup):
    boxes = soup.find_all('button', class_= "artdeco-button artdeco-button--2 artdeco-button--secondary ember-view")[2:]

    for box in boxes:
        status = box.find('span', class_="artdeco-button__text").get_text().strip()
        print(status, len(status))
        if box and status == "Connect":
            box.click()
            send = soup.find('button', class_ = 'artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1')
            send.click()
            print(box.get_attribute('aria-label'))
        else:
            print(status)


########################################################################################################


chrome_driver_path = input("Enter absolute path of chrome driver \n")
url = input("Enter the Search URL\n")

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
connect(soup)

for curr_page in range(2, total_page+1):
    new_url = url+"&page="+str(curr_page)
    driver.get(new_url)
    time.sleep(10)
    new_src = driver.page_source
    new_soup = BeautifulSoup(new_src, 'lxml')
    connect(new_soup)

driver.quit()

