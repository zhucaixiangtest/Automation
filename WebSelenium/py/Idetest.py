#coding:utf-8
import time

from BrowserClass import Browser
from ReadExcelClass import ReadExcel
from selenium import webdriver
from selenium.webdriver.support.select import Select
from DataBaseClass import Database
from MainMethodClass import run_main,case_get
import SmallClass
from ReadExcelClass import ReadExcel

from pymongo import MongoClient


# #--------------- ide调试---------------------------------
#
# br=webdriver.Chrome()
# br.maximize_window()
# br.get("http://192.168.1.176:3800/#/login")
#
#
#
#
# ReadExcel().Readcase(br,"D:/WebSelenium/Case/role_management.xlsx")
#
