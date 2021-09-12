# importing all the necessary libraries

from selenium import webdriver
import gspread
from selenium.webdriver.common.keys import Keys
import time
from test import get_list

# opening the cowin homepage

driver=webdriver.Chrome()
driver.get("https://selfregistration.cowin.gov.in/")

driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys('9619451797')
driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button').click()
time.sleep(30)

#extracting the OTP sms and getting it from google sheets

gc = gspread.service_account(filename='api.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oj0juHVUiEsAy3np3lISHBLOE0E3mtXoQdKKUvdUWxI/edit#gid=0')
worksheet=sh.sheet1
val = worksheet.acell('A1').value
l=val.split()[6]
otp=l[:-1]

#inputting the otp

driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(otp)
driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]/div/ion-button').click()
center = get_list()
driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[2]/ion-col/ion-grid/ion-row[5]/ion-col[2]/ul/li/a').click()
time.sleep(5)

