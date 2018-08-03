#coding:utf-8

try:
    from selenium import webdriver

except Exception as install_error:

    print (install_error,"检查是否安装好selenium")
import os

import time

class Browser_names():


    def __init__(self):

        self.chromes='Chrome'

        self.FireFoxs='FireFox'

        self.PhantomJS='PhantomJS'

        self.ies = 'Ie'

        self.edges = 'Edge'


        self.home_http='http'



    def _run_browser(self,browsers,website):
            # 调用谷歌浏览器并配置下载路径，下载用例需要这样的方法
            if browsers == self.chromes and self.home_http in website:

                options=webdriver.ChromeOptions()
                path=os.path.abspath("..")#表示当前所处的文件夹上一级文件夹的绝对路径
                filepath=path+"\\PullFile"

                prefs={'profile.default_content_settings.popups':0,'download.default_directory':filepath}
                options.add_experimental_option('prefs',prefs)
                if website != '':
                    br=webdriver.Chrome(chrome_options=options)
                    br.maximize_window()
                    br.get(website)
                    return  br


                #  调用ie11浏览器
            elif browsers == self.Ie and self.home_http in website:
                br = webdriver.Ie()
                br.maximize_window()
                br.get(website)
                return br

                #  调用win10自带edge浏览器
            elif browsers == self.edges and self.home_http in website:
                br = webdriver.Edge()
                br.maximize_window()
                br.get(website)
                return br

                 #  调用火狐浏览器
            elif browsers == self.FireFoxs and self.home_http in website:
                br = webdriver.Firefox()
                br.maximize_window()
                br.get(website)
                return br


            elif browsers == self.PhantomJS and self.home_http in website:
                br = webdriver.PhantomJS()
                br.maximize_window()
                br.get(website)
                return br





            elif browsers[0] =='c' or browsers[0] =='f':
                print ("填写浏览器名时首字母请大写")

            elif self.home_http not in website:
                print ("注意填写网址是需要加上http://...")

            else:
                print ('暂时不支持其他浏览器，可在browserclass中添加')

