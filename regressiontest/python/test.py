# coding:utf-8

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://test.everonet.com/everonet/#/login")