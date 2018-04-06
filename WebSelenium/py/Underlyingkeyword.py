# coding:utf-8

import StringManipulation
from selenium.webdriver.support.select import Select
from KeyWord import Basics_key
from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys


class Underlykey(Basics_key):

        def _i_n(self):

            pass

                    #click
        def _click_element_key(self,driver,Positioning_mode,Location_element):

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).click()

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).click()

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).click()
            else:
                pass

         #input

        def _input_element_key(self,driver,Positioning_mode,Location_element,Input_content):


            Input_content = StringManipulation._filter_value(Input_content)
            Input_content = str(Input_content)

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).send_keys(Input_content)
            else:
                pass


        #select
        def _select_element_key(self,driver,Positioning_mode,Location_element,Input_content):

            if Positioning_mode == self.Location_xpath:
                if isinstance(Input_content, float):
                    Input_content = StringManipulation._filter_value(Input_content)
                    Input_content = str(Input_content)
                    Select(driver.find_element_by_xpath(Location_element)).select_by_value(Input_content)
                else:
                    Select(driver.find_element_by_xpath(Location_element)).select_by_value(Input_content)

            elif Positioning_mode == self.Location_name:
                if isinstance(Input_content, float):
                    Input_content = StringManipulation._filter_value(Input_content)
                    Input_content = str(Input_content)
                    Select(driver.find_element_by_name(Location_element)).select_by_value(Input_content)
                else:
                    Select(driver.find_element_by_name(Location_element)).select_by_value(Input_content)

            elif Positioning_mode == self.Location_id:
                if isinstance(Input_content, float):
                    Input_content = StringManipulation._filter_value(Input_content)
                    Input_content = str(Input_content)
                    Select(driver.find_element_by_id(Location_element)).select_by_value(Input_content)
                else:
                    Select(driver.find_element_by_id(Location_element)).select_by_value(Input_content)
            else:
                pass

         # sleep
        def _sleeps_time_key(self,Input_content):
            if Input_content:
                Input_content = int(Input_content)
                time.sleep(Input_content)
            else:
                pass

        def _wait_key(self,driver,Input_content):
            if Input_content:
                Input_content = int(Input_content)
                driver.implicitly_wait(Input_content)
            else:
                pass


        def _suspension_element_key(self,driver,Positioning_mode,Location_element):

            if Positioning_mode ==self.Location_id:
                _ele_key = driver.find_element_by_id(Location_element)
                ActionChains(driver).move_to_element(_ele_key).perform()


            elif Positioning_mode == self.Location_name:
                _ele_key = driver.find_element_by_name(Location_element)
                ActionChains(driver).move_to_element(_ele_key).perform()


            elif Positioning_mode == self.Location_xpath:
                _ele_key = driver.find_element_by_xpath(Location_element)
                ActionChains(driver).move_to_element(_ele_key).perform()
            else:
                pass
       # js弹窗
        def _prompts_js_key(self,driver,Location_element, Input_content):

            dialog_box = driver.switch_to_alert()
            time.sleep(2)
            if Location_element == u'确认' and Input_content != '':
                text = str(Input_content)
                dialog_box.send_keys(Input_content)
                time.sleep(2)
                dialog_box.accept()
                time.sleep(2)
            if Location_element == u'取消' and Input_content != '':
                dialog_box.dismiss()
                time.sleep(2)

            elif Location_element == u'确认' and Input_content == '':
                dialog_box.accept()
                time.sleep(2)
            elif Location_element == u'取消' and Input_content == '':
                dialog_box.dismiss()
                time.sleep(2)
            else:
                pass

        def _Autoit_file_key(self, Input_content):
            test=StringManipulation
            paths=test._Autoit_file(Input_content)
            time.sleep(1)
            os.system(paths)
            time.sleep(1)

        # 切入iframe
        def _iframe_into_key(self, driver, Location_element):
            time.sleep(1)
            driver.switch_to.frame(driver.find_element_by_xpath(Location_element))
            time.sleep(1)

        # 切出iframe
        def _iframe_out_key(self, driver):
            time.sleep(1)
            driver.switch_to_default_content()  # 切出iframe
            time.sleep(1)


        def _push_input_key(self,driver,Positioning_mode,Location_element,Input_content):
            test=StringManipulation
            Input_content = test._push_file(Input_content)

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).send_keys(Input_content)
            else:
                pass

        def _find_value_key(self,driver,Positioning_mode,Location_element,Input_content):
            if Positioning_mode == self.Location_xpath:
                value = driver.find_element_by_xpath(Location_element).text
                value = value.encode("utf-8")
                value = str(value)
                # text=str(text)
                test=StringManipulation
                Input_content = test._filter_value(Input_content)
                if isinstance(Input_content, int):
                    Input_content = str(Input_content)
                    Input_content = Input_content + 'X'
                    value = value + 'X'
                if isinstance(Input_content, float):
                    Input_content = str(Input_content)
                    Input_content = Input_content + 'X'
                    value = value + 'X'

                text = Input_content.encode("utf-8")
                text = str(text)

                if value == text:
                    pass
                else:
                    print ('实际结果和预期不匹配')
                    a = 'no find date'
                    eval(a)
            else:
                print("find只需要xpath")

        def _enter_element_key(self,driver,Positioning_mode,Location_element):
            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).send_keys(Keys.ENTER)

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).send_keys(Keys.ENTER)

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).send_keys(Keys.ENTER)
            else:
                pass

        def _clear_element_key(self, driver, Positioning_mode, Location_element):

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).clear()

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).clear()

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).clear()
            else:
                pass


        def file_name(self, file_dir):
            for root, dirs, name in os.walk(file_dir):
                return name

        def list_none(self, value):
            if value:
                return 'True'
            else:
                return 'False'



        def find_file_key(self):

            test_exc=StringManipulation._pull_file()

            files = self.file_name(test_exc)
            list_value = self.list_none(files)

            if list_value == 'True':

                filename = test_exc + files[0]
                os.remove(filename)
                print '下载成功，文件名是', files[0], '因为需要初始化，正在删除此文件.....'


            else:
                print '指定的目录没有查询到下载的文件'
                eval('false')













