# coding:utf-8

import os
import time
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from KeyWord import BasicsKey
import string_manipulation


class UnderKey(BasicsKey):

    def i_n(self):

        pass

    # click
    def click_element_key(self, driver, positioning_mode, location_element):

        if positioning_mode == self.location_id:
            driver.find_element_by_id(location_element).click()

        elif positioning_mode == self.location_name:
            driver.find_element_by_name(location_element).click()

        elif positioning_mode == self.location_xpath:
            driver.find_element_by_xpath(location_element).click()

        elif positioning_mode == self.location_css:
            driver.find_element_by_css_selector(location_element).click()

        else:
            pass

    # send_keys
    def input_element_key(self, driver, positioning_mode, location_element, input_content):

        filter_va = string_manipulation
        input_content = filter_va.filter_value(input_content)

        if positioning_mode == self.location_id:
            driver.find_element_by_id(location_element).send_keys(input_content)

        elif positioning_mode == self.location_name:
            driver.find_element_by_name(location_element).send_keys(input_content)

        elif positioning_mode == self.location_xpath:
            driver.find_element_by_xpath(location_element).send_keys(input_content)

        elif positioning_mode == self.location_css:
            driver.find_element_by_css_selector(location_element).send_keys(input_content)

        else:
            pass

    # select下拉框
    def select_element_key(self, driver, positioning_mode, location_element, input_content):
        if positioning_mode == self.location_xpath:
            if isinstance(input_content, float):
                input_content = int(input_content)
                input_content = str(input_content)

                Select(driver.find_element_by_xpath(location_element)).select_by_value(input_content)
            else:
                Select(driver.find_element_by_xpath(location_element)).select_by_value(input_content)

        elif positioning_mode == self.location_name:
            if isinstance(input_content, float):
                input_content = string_manipulation.filter_value(input_content)
                input_content = str(input_content)
                Select(driver.find_element_by_name(location_element)).select_by_value(input_content)
            else:
                Select(driver.find_element_by_name(location_element)).select_by_value(input_content)

        elif positioning_mode == self.location_id:

            if isinstance(input_content, float):
                input_content = int(input_content)
                input_content = str(input_content)
                Select(driver.find_element_by_id(location_element)).select_by_value(input_content)

            else:
                Select(driver.find_element_by_id(location_element)).select_by_value(input_content)

        elif positioning_mode == self.location_css:

            if isinstance(input_content, float):
                input_content = string_manipulation.filter_value(input_content)
                input_content = str(input_content)
                Select(driver.find_element_by_css_selector(location_element)).select_by_value(input_content)

            else:
                Select(driver.find_element_by_css_selector(location_element)).select_by_value(input_content)

        else:
            pass

    # sleep强制等待
    def process_waiting(self, input_content):
        if input_content:
            input_content = int(input_content)
            time.sleep(input_content)

        else:
            pass

    # 智能等待
    def wait_key(self, driver, input_content):

        if input_content:
            input_content = int(input_content)
            driver.implicitly_wait(input_content)

        else:
            pass

    # 悬浮操作
    def suspension_element_key(self, driver, positioning_mode, location_element):

        if positioning_mode == self.location_id:
            _ele_key = driver.find_element_by_id(location_element)
            ActionChains(driver).move_to_element(_ele_key).perform()

        elif positioning_mode == self.location_name:
            _ele_key = driver.find_element_by_name(location_element)
            ActionChains(driver).move_to_element(_ele_key).perform()

        elif positioning_mode == self.location_xpath:
            _ele_key = driver.find_element_by_xpath(location_element)
            ActionChains(driver).move_to_element(_ele_key).perform()

        elif positioning_mode == self.location_css:
            _ele_key = driver.find_element_by_css_selector(location_element)
            ActionChains(driver).move_to_element(_ele_key).perform()

        else:
            pass

    #  js弹窗确认/取消/输入值确认或取消
    def prompts_js_key(self, driver, location_element, input_content):
        dialog_box = driver.switch_to_alert()
        time.sleep(2)
        if location_element == u'确认' and input_content != '':
            text = str(input_content)
            dialog_box.send_keys(input_content)
            time.sleep(2)
            dialog_box.accept()
            time.sleep(2)

        if location_element == u'取消' and input_content != '':
            dialog_box.dismiss()
            time.sleep(2)

        elif location_element == u'确认' and input_content == '':
            dialog_box.accept()
            time.sleep(2)

        elif location_element == u'取消' and input_content == '':
            dialog_box.dismiss()
            time.sleep(2)

        else:
            pass

    # auto it上传文件
    def auto_it_push(self, input_content):
        test = string_manipulation
        paths = test.auto_it_file(input_content)
        time.sleep(1)
        os.system(paths)
        time.sleep(1)

    # 切入iframe
    def frame_into_key(self, driver, positioning_mode, location_element):
        if positioning_mode == self.location_name:
            time.sleep(1)
            driver.switch_to.frame(driver.find_element_by_xpath(location_element))
            time.sleep(1)

        elif positioning_mode == self.location_id:
            time.sleep(1)
            driver.switch_to.frame(driver.find_element_by_xpath(location_element))
            time.sleep(1)

        elif positioning_mode == self.location_xpath:
            time.sleep(1)
            driver.switch_to.frame(driver.find_element_by_xpath(location_element))
            time.sleep(1)

        elif positioning_mode == self.location_css:
            time.sleep(1)
            driver.switch_to.frame(driver.find_element_by_css_selector(location_element))
            time.sleep(1)

        else:
            pass

    #  切出iframe
    def frame_out_key(self, driver):
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)

    # send_keys单独封装成一个上传文件
    def push_input_key(self, driver, positioning_mode, location_element, input_content):

        test = string_manipulation
        input_content = test.push_file(input_content)

        if positioning_mode == self.location_id:
            driver.find_element_by_id(location_element).send_keys(input_content)

        elif positioning_mode == self.location_name:
            driver.find_element_by_name(location_element).send_keys(input_content)

        elif positioning_mode == self.location_xpath:
            driver.find_element_by_xpath(location_element).send_keys(input_content)

        elif positioning_mode == self.location_css:
            driver.find_element_by_css_selector(location_element).send_keys(input_content)

        else:
            pass

    # 元素text断言,暂时只要xpath
    def _find_value_key(self, driver, positioning_mode, location_element, input_content, output):

        if positioning_mode == self.location_xpath:
            value = driver.find_element_by_xpath(location_element).text
            value = value.encode("utf-8")
            value = str(value)
            test = string_manipulation
            input_content = test.filter_value(input_content)

            if isinstance(input_content, int):
                input_content = str(input_content)
                input_content = input_content + 'X'
                value = value + 'X'

            if isinstance(input_content, float):
                input_content = str(input_content)
                input_content = input_content + 'X'
                value = value + 'X'

            text = input_content.encode("utf-8")
            text = str(text)
            if value == text:
                print(output, "-----TRUE")
                print ('预期结果:' + text)
                print ('实际结果:' + value)
                return "True"
            else:
                print '--------------------------------------'
                print ('预期结果:'+text)
                print ('实际结果:'+value)
                print('')
                print ('实际结果和预期不匹配')
                print '--------------------------------------'
                driver.quit()
                actual_results = 'False'
                return actual_results
        else:
            print("find目前只用xpath定位方式")

    # 回车键操作
    def _enter_element_key(self, driver, positioning_mode, location_element):

        if positioning_mode == self.location_id:
            driver.find_element_by_id(location_element).send_keys(Keys.ENTER)

        elif positioning_mode == self.location_name:
            driver.find_element_by_name(location_element).send_keys(Keys.ENTER)

        elif positioning_mode == self.location_xpath:
            driver.find_element_by_xpath(location_element).send_keys(Keys.ENTER)

        elif positioning_mode == self.location_css:
            driver.find_element_by_css_selector(location_element).send_keys(Keys.ENTER)

        else:
            pass

    # 清除文本框操作
    def _clear_element_key(self, driver, positioning_mode, location_element):

        if positioning_mode == self.location_id:
            driver.find_element_by_id(location_element).clear()

        elif positioning_mode == self.location_name:
            driver.find_element_by_name(location_element).clear()

        elif positioning_mode == self.location_xpath:
            driver.find_element_by_xpath(location_element).clear()

        elif positioning_mode == self.location_css:
            driver.find_element_by_css_selector(location_element).clear()

        else:
            pass

    # 得到目录文件
    def file_name(self, file_dir):
        for files, value, name in os.walk(file_dir):
            return name

    # 查看是否有文件
    def false_belis(self, value):
        if value:
            return 'True'
        else:
            return 'False'

    # 断言是否下载文件成功
    def find_file_key(self, driver, output):
        test_exc = string_manipulation.pull_file()
        files = self.file_name(test_exc)
        list_value = self.false_belis(files)
        if list_value == 'True':
            filename = test_exc + files[0]
            os.remove(filename)
            print(output, "-----TRUE")
            actual_results = 'True'
            print ('下载成功，文件名是', files[0], '因为需要初始化，正在删除此文件.....')
            return actual_results
        else:

            actual_results = 'False'
            driver.quit()
            print ('指定的目录没有查询到下载的文件')
            return actual_results

    # 当时间控件不可输入时，需要用js去除removeAttribute属性再把值写进去
    def time_js_input(self, driver, positioning_mode, location_element, input_content):
        time.sleep(1)
        elements = r"'"+location_element+"'"
        if positioning_mode == self.location_id:
            jsa = "document.getElementById("+elements+").removeAttribute('readonly')"
            driver.execute_script(jsa)
            if isinstance(input_content, float):
                input_content = int(input_content)
                input_content = str(input_content)
                driver.find_element_by_id(location_element).send_keys(input_content)
                time.sleep(1)
            else:
                driver.find_element_by_id(location_element).send_keys(input_content)
                time.sleep(1)

        else:
            print("对于时间空间暂时先写id方法，后面用到其他在Underlyingkeyword.py维护")

    # 拿到url
    def get_urls(self, input_content):
        geturl_value = open('..\config\getUrl.txt')
        get_url = geturl_value.readline()
        geturl_value.close()
        input_contents = get_url+input_content
        return input_contents

    #  positioning_mode配置文件项  input_content sql语句
    # def _oracle_sql(self,positioning_mode,input_content):
    #
    #     # positioning_mode, location_element, input_content
    #     if positioning_mode and input_content:
    #         need_value='select'
    #         sql_select=input_content[0:7]
    #         print(sql_select)
    #         contrast_select = re.search(need_value,sql_select , re.IGNORECASE)
    #         false_be_true=bool(contrast_select)
    #
    #         print(false_be_true)
    #
    #         if false_be_true ==True:
    #
    #             Database().db_oracle(positioning_mode,need_value,input_content)
    #
    #         else:
    #
    #             Database().db_oracle(positioning_mode,' ' , input_content)
    #     else:
    #         print("填写参数有误")
