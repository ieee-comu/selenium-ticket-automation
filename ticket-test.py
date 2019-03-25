#!/usr/bin/python3.6
# created by cicek on 24.03.2019 20:44

from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("https://www.onurair.com/en/")
sleep(5)

departure = browser.find_element_by_xpath("//*[@id='depPortArea']/label/span[2]/span[1]")
departure.click()
sleep(2)
departureSelect = browser.find_element_by_xpath("/html/body/div[3]/div/span/span/ul/li[2]/span/ul/li[4]/span")
departureSelect.click()
sleep(2)

arrival = browser.find_element_by_xpath("//*[@id='arrPortArea']/div/label/span[2]/span[1]")
arrival.click()
sleep(2)
arrivalSelect = browser.find_element_by_xpath("/html/body/div[3]/div/span/span/ul/li[3]/span/ul/li[2]/span")
arrivalSelect.click()
sleep(2)

# select one way ticket
oneWay = browser.find_element_by_xpath("//*[@id='radio']/tbody/tr/td[2]/label")
oneWay.click()
sleep(2)

departureDate = browser.find_element_by_xpath("//*[@id='departureDate']")
departureDate.click()
sleep(2)
departureDateSelect = browser.find_element_by_xpath("/html/body/div[1]/div[1]/table/tbody/tr[6]/td[6]")
departureDateSelect.click()
sleep(2)

continueButton = browser.find_element_by_xpath("//*[@id='btnSearch']")
continueButton.click()
sleep(3)

# new page (passenger info)(1/2)

price = browser.find_element_by_xpath("//*[@id='bundleSelectDivId_0_3_0_0']/div[2]/div[1]/div[1]")
price.click()
sleep(2)
fixThePrice = browser.find_element_by_xpath("//*[@id='priceFreeze']/div/div/label")
fixThePrice.click()

continueButton2 = browser.find_element_by_xpath("//*[@id='btnContinue']")
continueButton2.click()
sleep(3)

# new page (passenger info)(2/2)

passengerTitle = browser.find_element_by_xpath("//*[@id='gender1-selectized']")
passengerTitle.click()
sleep(2)
passengerTitleMr = browser.find_element_by_xpath("//*[@id='tabPax1']/div/div[2]/span[1]/div/div/div[2]/div/div[1]")
passengerTitleMr.click()
sleep(2)

passengerName = browser.find_element_by_xpath("//*[@id='name1']")
print("enter your name: ", end="")
nameInput = str(input())
passengerName.send_keys(nameInput)

passengerSurname = browser.find_element_by_xpath("//*[@id='surname1']")
print("enter your surname: ", end="")
surnameInput = str(input())
passengerSurname.send_keys(surnameInput)

passengerNationality = browser.find_element_by_xpath("//*[@id='nationality1-selectized']")
passengerNationality.click()
sleep(2)
passengerNationalityTr = browser.find_element_by_xpath("//*[@id='nationalityGroup1']/div/div/div[2]/div/div[1]")
passengerNationalityTr.click()
sleep(2)

# birth day
birth1 = browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[1]/div/div")
birth1.click()
sleep(2)

print("enter your birth day (DAY)(2, 4, 23 etc...): ", end="")
day = int(input())
passengerBirthDay = browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[1]/div/div/div[2]/div/div[{0}]".format(day))
passengerBirthDay.click()
sleep(2)

# birth month
birth2 = browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[2]/div/div")
birth2.click()
sleep(2)

print("enter your birth month (MONTH)(1, 6, 12 etc...): ", end="")
month = int(input())
passengerBirthMonth = browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[2]/div/div/div[2]/div/div[{0}]".format(month))
passengerBirthMonth.click()
sleep(2)

# birth year
birth3 = browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[3]/div/div")
birth3.click()
sleep(2)

print("enter your birth year (YEAR)(1950, 1980, 1994 etc...): ", end="")
year = int(input())
passengerBirthYear = browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[3]/div/div/div[2]/div/div[{0}]".format((2008-year)))
passengerBirthYear.click()
sleep(2)

# ID
passengerID = browser.find_element_by_xpath("//*[@id='natId1']")
print("enter your ID: ", end="")
ID = str(input())
passengerID.send_keys(ID)
sleep(2)

# autofilled by the system
# contact info
# contactName = browser.find_element_by_xpath("//*[@id='contact_name0']")
# contactName.send_keys(nameInput)
# contactSurname = browser.find_element_by_xpath("//*[@id='contact_surname0']")
# contactSurname.send_keys(surnameInput)

contactTel = browser.find_element_by_xpath("//*[@id='frst-tel-number0']")
print("enter your contact number:+90", end="")
tel = int(input())
contactTel.send_keys(tel)
sleep(2)

contactMail = browser.find_element_by_xpath("//*[@id='email0']")
print("enter your mail: ", end="")
mail = str(input())
contactMail.send_keys(mail)
sleep(2)

continueButton3 = browser.find_element_by_xpath("//*[@id='btnSave']")
continueButton3.click()

sleep(10)  # optional
browser.close()  # optional
