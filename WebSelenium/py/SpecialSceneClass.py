#coding:utf-8
from selenium.webdriver.common.action_chains import *
import time
import os
# import pytesseract
from selenium.webdriver.support.select import Select
from Keyword import keywords

class Special(keywords):

    def start(self):

         pass

    #浮动方法
    def suspension(self,driver, Location, element):

        if Location ==self.ids:
            ele = driver.find_element_by_id(element)
            ActionChains(driver).move_to_element(ele).perform()


        elif Location == self.names:
            ele = driver.find_element_by_name(element)
            ActionChains(driver).move_to_element(ele).perform()


        elif Location == self.xpaths:
            ele = driver.find_element_by_xpath(element)
            ActionChains(driver).move_to_element(ele).perform()
        else:
            pass

            #prompt对话框
    def  prompts(self,driver,element,text):

        dialog_box = driver.switch_to_alert()
        time.sleep(2)
        if element==u'确认' and text !='':
            text=str(text)
            dialog_box.send_keys(text)
            time.sleep(2)
            dialog_box.accept()
            time.sleep(2)
        if element == u'取消' and text != '':
            dialog_box.dismiss()
            time.sleep(2)

        elif element==u'确认'and text=='':
            dialog_box.accept()
            time.sleep(2)
        elif element==u'取消'and text=='':
            dialog_box.dismiss()
            time.sleep(2)
        else:
            pass

     #传入文件exe路径，os调用
    def PushAutoit(self,exe_name):
        path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径
        paths=path2+'\\Autoit\\'+exe_name
        os.system(paths)



    #select下的option（下拉框的值的选择）
    def options(self,driver,element,text):

        Select(driver.find_element_by_xpath(element)).select_by_value(text)

    #切入iframe
    def iframe_in(self,driver,element):

        driver.switch_to.frame(driver.find_element_by_xpath(element))

    #切出iframe
    def iframe_out(self,driver):

        driver.switch_to_default_content()  # 切出iframe


    def file_name(self,file_dir):
        for root, dirs, name in os.walk(file_dir):

            return name

    def list_none(self,value):
        if value:
            return 'True'
        else:
            return 'False'

#python2转码在这一刻尤其恶心，本想根据填写的文件名去对比是否下载成功，现在是下载完了，查看指定的文件有没有下载的文件，有的话passs并删除掉下载的文件（这个需要删除作为初始化） 没有fail
        #注意 需要浏览器手动设置下载路径
    def find_excel(self):

        paths=os.path.abspath('..')
        path_exc=paths+'\\PullFile\\'

        files=self.file_name(path_exc)
        list_value=self.list_none(files)

        if list_value=='True':

            filename = path_exc+files[0]
            print '下载成功，文件名是',files[0],'因为需要初始化，正在删除此文件.....'
            # os.remove(filename)

        else:
            # list_value=='False':

            print '指定的目录没有查询到下载的文件'
            # eval('false')








# if __name__=='_main_':
#     pass
# else:
#
#      Special().find_excel()

