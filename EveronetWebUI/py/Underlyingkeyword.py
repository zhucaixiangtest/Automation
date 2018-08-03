# coding:utf-8
import re
import StringManipulation
from selenium.webdriver.support.select import Select
from KeyWord import Basics_key
import os
import time
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys
from DateBaseClass import Database

class Underlykey(Basics_key):

        def _i_n(self):

            pass

        # click
        def _click_element_key(self,driver,Positioning_mode,Location_element):

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).click()

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).click()

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).click()

            elif Positioning_mode == self.Location_css:
                driver.find_element_by_css_selector(Location_element).click()

            else:
                pass

        # send_keys
        def _input_element_key(self,driver,Positioning_mode,Location_element,Input_content):


            Input_content = StringManipulation._filter_value(Input_content)

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_css:
                driver.find_element_by_css_selector(Location_element).send_keys(Input_content)

            else:
                pass


        #  select下拉框
        def _select_element_key(self,driver,Positioning_mode,Location_element,Input_content):

            if Positioning_mode == self.Location_xpath:
                if isinstance(Input_content, float):
                    # Input_content = StringManipulation._filter_value(Input_content)
                    # Input_content = str(Input_content)
                    Input_content=int(Input_content)
                    Input_content=str(Input_content)

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
                    Input_content=int(Input_content)
                    Input_content=str(Input_content)
                    Select(driver.find_element_by_id(Location_element)).select_by_value(Input_content)

                else:
                    Select(driver.find_element_by_id(Location_element)).select_by_value(Input_content)


            elif Positioning_mode == self.Location_css:

                if isinstance(Input_content, float):
                    Input_content = StringManipulation._filter_value(Input_content)
                    Input_content = str(Input_content)
                    Select(driver.find_element_by_css_selector(Location_element)).select_by_value(Input_content)

                else:
                    Select(driver.find_element_by_css_selector(Location_element)).select_by_value(Input_content)

            else:
                pass

        # sleep强制等待
        def _sleeps_time_key(self,Input_content):

            if Input_content:
                Input_content = int(Input_content)
                time.sleep(Input_content)

            else:
                pass

        # 智能等待
        def _wait_key(self,driver,Input_content):

            if Input_content:
                Input_content = int(Input_content)
                driver.implicitly_wait(Input_content)

            else:
                pass

        # 悬浮操作
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

            elif Positioning_mode == self.Location_css:

                _ele_key = driver.find_element_by_css_selector(Location_element)
                ActionChains(driver).move_to_element(_ele_key).perform()

            else:
                pass
        #  js弹窗确认/取消/输入值确认或取消
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

        # autoit上传文件
        def _Autoit_file_key(self, Input_content):

            test=StringManipulation
            paths=test._Autoit_file(Input_content)
            time.sleep(1)
            os.system(paths)
            time.sleep(1)

        # 切入iframe
        def _iframe_into_key(self, driver,Positioning_mode, Location_element):

            if Positioning_mode == self.Location_name:
                time.sleep(1)
                driver.switch_to.frame(driver.find_element_by_xpath(Location_element))
                time.sleep(1)

            elif Positioning_mode == self.Location_id:
                time.sleep(1)
                driver.switch_to.frame(driver.find_element_by_xpath(Location_element))
                time.sleep(1)

            elif Positioning_mode == self.Location_xpath:
                time.sleep(1)
                driver.switch_to.frame(driver.find_element_by_xpath(Location_element))
                time.sleep(1)

            elif Positioning_mode == self.Location_css:
                time.sleep(1)
                driver.switch_to.frame(driver.find_element_by_css_selector(Location_element))
                time.sleep(1)

            else:
                pass

        #  切出iframe
        def _iframe_out_key(self, driver):
            time.sleep(1)
            driver.switch_to_default_content()
            time.sleep(1)

        # send_keys单独封装成一个上传文件
        def _push_input_key(self,driver,Positioning_mode,Location_element,Input_content):

            test=StringManipulation
            Input_content = test._push_file(Input_content)

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).send_keys(Input_content)

            elif Positioning_mode == self.Location_css:
                driver.find_element_by_css_selector(Location_element).send_keys(Input_content)

            else:
                pass

        # 元素text断言,暂时只要xpath
        def _find_value_key(self,driver,Positioning_mode,Location_element,Input_content,output):

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
                    print(output,"-----TRUE")
                    ActualResults=('True')
                    return ActualResults
                else:
                    print '--------------------------------------'
                    print ('预期结果',text)
                    print ('实际结果',value)
                    print('')
                    print ('实际结果和预期不匹配')
                    print '--------------------------------------'
                    driver.quit()
                    ActualResults='False'
                    return ActualResults
            else:
                print("find目前只用xpath定位方式")

        # 回车键操作
        def _enter_element_key(self,driver,Positioning_mode,Location_element):

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).send_keys(Keys.ENTER)

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).send_keys(Keys.ENTER)

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).send_keys(Keys.ENTER)

            elif Positioning_mode == self.Location_css:
                driver.find_element_by_css_selector(Location_element).send_keys(Keys.ENTER)

            else:
                pass

        # 清除文本框操作
        def _clear_element_key(self, driver, Positioning_mode, Location_element):

            if Positioning_mode == self.Location_id:
                driver.find_element_by_id(Location_element).clear()

            elif Positioning_mode == self.Location_name:
                driver.find_element_by_name(Location_element).clear()

            elif Positioning_mode == self.Location_xpath:
                driver.find_element_by_xpath(Location_element).clear()

            elif Positioning_mode == self.Location_css:
                driver.find_element_by_css_selector(Location_element).clear()

            else:
                pass

        # 得到目录文件
        def file_name(self, file_dir):
            for root, dirs, name in os.walk(file_dir):
                return name

        # 查看是否有文件
        def list_none(self, value):
            if value:
                return 'True'
            else:
                return 'False'

        # 断言是否下载文件成功
        def find_file_key(self,driver,output):

            test_exc=StringManipulation._pull_file()

            files = self.file_name(test_exc)
            list_value = self.list_none(files)

            if list_value == 'True':

                filename = test_exc + files[0]
                os.remove(filename)
                print(output,"-----TRUE")
                ActualRresults='True'
                print '下载成功，文件名是', files[0], '因为需要初始化，正在删除此文件.....'
                return ActualRresults

            else:
                    print '指定的目录没有查询到下载的文件'

                    ActualResults='False'
                    driver.quit()
                    return ActualResults

        # 当时间控件不可输入时，需要用js去除removeAttribute属性再把值写进去
        def _time_js_input(self,driver,Positioning_mode,Location_element,Input_content):

            time.sleep(1)
            elements=r"'"+Location_element+"'"
            if Positioning_mode==self.Location_id:
                jsa = "document.getElementById("+elements+").removeAttribute('readonly')"
                driver.execute_script(jsa)
                if isinstance(Input_content,float):
                    Input_content=int(Input_content)
                    Input_content=str(Input_content)
                    driver.find_element_by_id(Location_element).send_keys(Input_content)
                    time.sleep(1)
                else:
                    driver.find_element_by_id(Location_element).send_keys(Input_content)
                    time.sleep(1)
            else:
                print('对于时间空间暂时先写id方法，后面用到其他在Underlyingkeyword.py维护')

        # Positioning_mode配置文件项  Input_content sql语句
        # def _oracle_sql(self,Positioning_mode,Input_content):
        #
        #     # Positioning_mode, Location_element, Input_content
        #     if Positioning_mode and Input_content:
        #         need_value='select'
        #         sql_select=Input_content[0:7]
        #         print(sql_select)
        #         contrast_select = re.search(need_value,sql_select , re.IGNORECASE)
        #         false_be_true=bool(contrast_select)
        #
        #         print(false_be_true)
        #
        #         if false_be_true ==True:
        #
        #             Database().db_oracle(Positioning_mode,need_value,Input_content)
        #
        #         else:
        #
        #             Database().db_oracle(Positioning_mode,' ' , Input_content)
        #     else:
        #         print("填写参数有误")
























