#coding:utf-8
from BrowserClass import Browser
from ReadExcelClass import ReadExcel
from selenium import webdriver


import os




def opens(browsers,website):

    if browsers ==  'Chrome' :
        driver=Browser().chromes(website)
        return driver

    elif browsers =='FireFox':
        driver=Browser().firefoxs(website)
        return driver

    elif browsers =='IE':
        driver=Browser().IES(website)
        return driver

    else:
        print '检查浏览器输入是否正确，目前只支持了谷歌、火狐'


# def Case(driver,case_path,case_name):
def Case(driver,case_name):
    if case_name !='':
        paths=os.path.abspath('..')
        path_exc=paths+'\\Case\\'
        read_case=path_exc+case_name
        print '**********************正在执行用例：',path_exc+case_name
        print ''
        try:
            ReadExcel().Readcase(driver,read_case)
        except Exception as a:
            driver.quit()
            print a
            print '*******************此用例执行失败具体查看log.*********************************'
            yu_str='True'
            shi_str='False'
            print ''
            print '**********************用例执行完：', path_exc + case_name
            print ''
            return yu_str,shi_str
        print '**********************用例执行完：', path_exc + case_name
        yu_str = 'True'
        shi_str = 'True'
        return yu_str, shi_str




