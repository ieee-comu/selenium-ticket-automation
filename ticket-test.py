#!/usr/bin/python3.6
# created by cicek on 23.03.2019 20:44

from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("https://www.onurair.com/en/")

sleep(6)
browser.close()

