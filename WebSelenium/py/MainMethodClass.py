#coding:utf-8
from selenium import webdriver
import time
from SpecialSceneClass import Special
from SmallClass import Transformation
from selenium.webdriver.common.keys import Keys
from DataBaseClass import Database
from Keyword import keywords
import os
from BrowserClass import Browser
import xlrd
from selenium.webdriver.support.select import Select


class run_main(keywords):

    def start(self):

        pass



    def runs(self,driver,method,Location,element,text,logs):
        #点击事件

        if method==self.clicks:
            if Location==self.ids:
                driver.find_element_by_id(element).click()


            elif  Location==self.names:

                   driver.find_element_by_name(element).click()


            elif Location==self.xpaths:

                 driver.find_element_by_xpath(element).click()
            else:
                pass
         # select下的option值选择
        elif method==self.options:
            text=Transformation(text)

            # text=text.encode("utf-8")
            text=str(text)
            Select(driver.find_element_by_xpath(element)).select_by_value(text)


        # s输入事件

        elif method == self.inputs:
            text=Transformation(text)
            if Location == self.ids:


                driver.find_element_by_id(element).send_keys(text)

            elif Location == self.names:

                driver.find_element_by_name(element).send_keys(text)


            elif Location == self.xpaths:

                driver.find_element_by_xpath(element).send_keys(text)
            else:
                pass

        #等待事件-强制等待
        elif method == self.sleeps:
            text=int(text)

            time.sleep(text)

        #等待事件-隐性等待
        elif method==self.waits:
            text=int(text)
            driver.implicitly_wait(text)


         #判断浮动操作
        elif method==self.floats:
            Special().suspension(driver,Location,element)

           #弹窗
        elif method == self.prompts:
            text=Transformation(text)
            Special().prompts(driver,element,text)


        #插件上传判断
        elif method ==self.autoits:

            Special().PushAutoit(text)


        #input上传单独拿出来用
        elif method==self.input_push and Location == self.ids:
            path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径
            paths=path2+'\\PushFile\\'+text

            driver.find_element_by_id(element).send_keys(paths)


        elif method == self.inputs and Location == self.names:
             path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径
             paths=path2+'\\PushFile\\'+text

             driver.find_element_by_name(element).send_keys(paths)


        elif method == self.inputs and Location == self.xpaths:
            path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径
            paths=path2+'\\PushFile\\'+text

            driver.find_element_by_xpath(element).send_keys(paths)


           #iframe 切入
        elif method==self.iframe_intos:
            time.sleep(1)
            Special().iframe_in(driver,element)
            time.sleep(1)

          #iframe切出
        elif method==self.iframe_outs:
            time.sleep(1)
            Special().iframe_out(driver)
            time.sleep(1)

        # 找值 text   --只要写xpath，考虑页面不知道是否存在相同的id name ,xpath比较唯一性，判断准确点
        elif method==self.finds and Location==self.xpaths:
            value=driver.find_element_by_xpath(element).text
            value=value.encode("utf-8")
            value=str(value)
            # text=str(text)
            texta=Transformation(text)
            if isinstance(texta,int):
                texta=str(texta)
                texta=texta+'X'
                value=value+'X'
            if isinstance(texta,float):
                texta=str(texta)
                texta=texta+'X'
                value=value+'X'

            text= texta.encode("utf-8")
            text=str(text)



            if value==text:
                pass
            else:
                print ('实际结果和预期不匹配')
                a='false'
                eval(a)



        # elif method=='times' and  Location=='id':
        #     time.sleep(1)
        #     elements=r"'"+element+"'"
        #     jsa = "document.getElementById("+elements+").removeAttribute('readonly')"
        #     driver.execute_script(jsa)
        #     driver.find_element_by_id(element).send_keys(text)
        #     time.sleep(1)

         # 回车键，有时候场景需要哦~
        elif method==self.enter:
            if Location ==self.xpaths:
                 driver.find_element_by_xpath(element).send_keys(Keys.ENTER)

            elif Location ==self.ids:
                driver.find_element_by_id(element).send_keys(Keys.ENTER)

            elif Location ==self.names:
                 driver.find_element_by_name(element).send_keys(Keys.ENTER)

        # mysql  Location填写数据库地址 例如 178,element填写库名,text填写sql
        elif method==self.mysqls:

            str_va='${save_value}'
            if str_va in text:
                path2=os.path.abspath('..')
                value_path=path2+'\\values\\'+'save_value.txt'
                f = open(value_path,'r')
                s=f.read()
                f.close()

                text=text.replace('${save_value}',s)
                test_mysql=Database()
                test_mysql.db_mysqls(Location,element,text)
            else:
                 test_mysql=Database()
                 test_mysql.db_mysqls(Location,element,text)

        # mysql  Location填写数据库地址 如果是select element填写select例如 base_109,text填写sql
        # elif method==self.oracles:
        #     test_oracle=Database()
        #
        #     text=text.encode("utf-8")
        #     test_oracle.db_oracle(Location,element,text)

        #打开谷歌浏览器
        elif method==self.opens:
            if Location==self.chromes:
               Browser().chromes(text)
         #打开火狐浏览器
            elif Location==self.fireFoxs:
                Browser().firefoxs(text)


        # 查看下载后的文件是否在指定的目录下，只判断文件名，若判断内容需要后期加
        elif method==self.find_excel:

            Special().find_excel()

        # 清楚input
        elif method=='clear':
            if Location=='id':
                driver.find_element_by_id(element).clear()

            elif Location=='xpath':
                driver.find_element_by_xpath(element).clear()

            elif Location=='name':
                driver.find_element_by_name(element).clear()
            else:
                pass

        elif method=='refresh':
            driver.refresh()




        else:
            pass

        print ''

        print logs,'-----TRUE'


class case_get(run_main,keywords):

    def case_again(self,driver,method,text):

            if method==self.case:
                 paths=os.path.abspath('..')
                 path_exc=paths+'\\Case\\'

                 text=path_exc+text

                 data_case = xlrd.open_workbook(text)
                 table = data_case.sheet_by_index(0)
                  #获取excel的总行数
                 nrows_case = table.nrows
                 for a in range(1,nrows_case):
                     valuea = table.row_values(a)
                     #操作方法
                     method=valuea[0]
                     #定位方式
                     Location=valuea[1]
                     #定位元素
                     element=valuea[2]
                     #输入内容
                     text=valuea[3]
                     #log print
                     logs=valuea[4]

                     self.runs(driver,method,Location,element,text,logs)


















