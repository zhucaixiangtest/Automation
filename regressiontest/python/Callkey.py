# coding:utf-8

import xlrd
from underlying_keyword import UnderKey
import string_manipulation
from DateBaseClass import Database


class JudgeCase(UnderKey):

    def _start_(self):
        pass

    def selenium_for(self, driver, operation_method, positioning_mode, location_element, input_content, output):
            # 点击事件
            if operation_method == self.basics_click:
                self.click_element_key(driver, positioning_mode, location_element)

            # 输入
            elif operation_method == self.basics_input:
                self.input_element_key(driver, positioning_mode, location_element, input_content)

            # select下拉框
            elif operation_method == self.basics_option:
                self.select_element_key(driver, positioning_mode, location_element, input_content)

            # sleep
            elif operation_method == self.basics_sleep:
                self.process_waiting(input_content)

            # 智能等待
            elif operation_method == self.basics_wait:
                self.wait_key(driver, input_content)

            #  float
            elif operation_method == self.basics_float:
                self.suspension_element_key(driver, positioning_mode, location_element)

            # js弹窗
            elif operation_method == self.basics_prompt:
                self.prompts_js_key(driver, location_element, input_content)

            # auto it上传
            elif operation_method == self.basics_autoit:
                self.auto_it_push(input_content)

            elif operation_method == self.basics_iframe_into:
                self.frame_into_key(driver, positioning_mode, location_element)

            elif operation_method == self.basics_iframe_out:
                self.frame_out_key(driver)

            elif operation_method == self.basics_push:
                self.push_input_key(driver, positioning_mode, location_element, input_content)

            elif operation_method == self.basics_find:
                actual_results = self._find_value_key(driver, positioning_mode, location_element, input_content, output)
                return actual_results

            elif operation_method == self.basics_enter:
                self._enter_element_key(driver, positioning_mode, location_element)

            elif operation_method == self.basics_clear:
                self._clear_element_key(driver, positioning_mode, location_element)

            elif operation_method == self.basics_mysql:

                Database().db_mysql(positioning_mode, location_element, input_content)

            elif operation_method == self.basics_mongo:

                Database().db_mongodb(positioning_mode, location_element, input_content)

            elif operation_method == self.basics_str:
                actual_results = self.find_str(driver, positioning_mode, location_element)
                return actual_results

            #  elif operation_method == self.basics_oracle:
            #
            #     self._oracle_sql(positioning_mode,input_content)

            elif operation_method == self.basics_find_file:
                actual_results = self.find_file_key(driver, output)
                return actual_results

            elif operation_method == self.basics_quit:
                driver.quit()

            elif operation_method == self.basics_time:
                self.time_js_input(driver, positioning_mode, location_element, input_content)

            elif operation_method == self.basics_gets:
                input_content = self.get_urls(input_content)
                driver.get(input_content)

            elif operation_method == self.basics_lens:
                actual_results = self.find_lens(driver, positioning_mode, location_element, input_content)
                return actual_results

            elif operation_method == self.basics_save:
                self.find_save_value(driver, positioning_mode, location_element)

            else:
                pass

            print ('')
            print (output+':            -----TRUE')

    # 继承调用selenium方法
    def case_selenium(self, driver, operation_method, positioning_mode, location_element, input_content, output):

            actual_results = self.selenium_for(driver, operation_method, positioning_mode,
                                               location_element, input_content, output)
            if operation_method == self.basics_case:
                test = string_manipulation
                input_content = test.case_file(input_content)
                data_case = xlrd.open_workbook(input_content)
                table = data_case.sheet_by_index(0)
                # 获取excel的总行数
                nrows_case = table.nrows
                agin_values = []
                for i in range(1, nrows_case):
                    value_exc = table.row_values(i)
                    agin_values.append(value_exc)
                for value in agin_values:
                    # 操作方法
                    operation_method = value[0]
                    # 定位方式
                    positioning_mode = value[1]
                    # 定位元素
                    location_element = value[2]
                    # 输入内容
                    input_content = value[3]
                    # log print
                    output = value[4]

                    actual_results = self.selenium_for(driver, operation_method, positioning_mode, location_element,
                                                       input_content, output)
                    if actual_results:
                        return actual_results

            return actual_results
