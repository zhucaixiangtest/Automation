#coding:utf-8
from selenium import webdriver
import time

class Browser():



    def chromes(self,website):
        br=webdriver.Chrome()
        br.maximize_window()
        if website !='':
            br.get(website)
            return br
        else:
            print '检查输入网址是否有错误'





    def firefoxs(self,website):
        br = webdriver.Firefox()
        br.maximize_window()
        if website != '':
            br.get(website)
            return br



        else:
            print '检查输入网址是否有错误'




    def IES(self,website):
        br = webdriver.Ie()
        br.maximize_window()
        if website != '':
            br.get(website)
            return br



        else:
            print '检查输入网址是否有错误'

