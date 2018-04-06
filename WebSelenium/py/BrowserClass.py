#coding:utf-8




try:
    from selenium import webdriver

except Exception as install_error:

    print (install_error,"检查是否安装好selenium")

import time

class Browser_names():


    def __init__(self):

        self.chromes='Chrome'

        self.FireFoxs='FireFox'

        self.home_http='http'



    def _run_browser(self,browsers,website):

            if browsers == self.chromes and self.home_http in website:
                br = webdriver.Chrome()
                br.maximize_window()
                br.get(website)
                return br

            elif browsers == self.FireFoxs and self.home_http in website:
                br = webdriver.Firefox()
                br.maximize_window()
                br.get(website)
                return br


            elif browsers[0] =='c' or browsers[0] =='f':


                print ("填写浏览器名时首字母请大写")


            elif self.home_http not in website:

                print ("注意填写网址是需要加上http://...")

            else:

                print ('暂时不支持其他浏览器，可在browserclass中添加')

