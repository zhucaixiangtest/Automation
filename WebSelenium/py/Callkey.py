# coding:utf-8

import xlrd
import os
from Underlyingkeyword import Underlykey
import StringManipulation
from DateBaseClass import Database


class Judge_use_case(Underlykey):

    def _start_(self):

        pass

    def _case_seleniums(self,driver,Operation_method,Positioning_mode,Location_element,Input_content,output):


            if Operation_method == self.basics_click:
                #点击
                self._click_element_key(driver,Positioning_mode,Location_element)

            #输入
            elif Operation_method == self.basics_input:

                self._input_element_key(driver,Positioning_mode,Location_element,Input_content)

            # select
            elif Operation_method ==self.basics_option:

                self._select_element_key(driver,Positioning_mode,Location_element,Input_content)

            #sleep
            elif  Operation_method ==self.basics_sleep:

                self._sleeps_time_key(Input_content)

            #智能等待
            elif Operation_method == self.basics_wait:

                self._wait_key(driver,Input_content)

           #float
            elif Operation_method == self.basics_float:
                self._suspension_element_key(driver,Positioning_mode,Location_element)

            # js弹窗
            elif Operation_method == self.basics_prompt:

                self._prompts_js_key(driver,Location_element,Input_content)

            elif Operation_method ==self.basics_autoit:
                 self._Autoit_file_key(Input_content)


            elif Operation_method == self.basics_iframe_into:
                 self._iframe_into_key(driver,Positioning_mode, Location_element)

            elif Operation_method ==self.basics_iframe_out:

                self._iframe_out_key(driver)

            elif Operation_method ==self.basics_push:
                self._push_input_key(driver,Positioning_mode,Location_element,Input_content)


            elif Operation_method ==self.basics_find:

                ActualRresults = self._find_value_key(driver,Positioning_mode,Location_element,Input_content,output)

                return ActualRresults

            elif Operation_method == self.basics_enter:
                self._enter_element_key(driver,Positioning_mode,Location_element)

            elif Operation_method == self.basics_clear:
                self._clear_element_key(driver, Positioning_mode, Location_element)

            elif Operation_method == self.basics_mysql:

                Database().db_mysqls(Positioning_mode, Location_element,Input_content)

            elif Operation_method == self.basics_oracle:

                Database().db_mysqls(Positioning_mode, Location_element,Input_content)

            elif Operation_method ==self.basics_find_file:
                ActualRresults=self.find_file_key(output)
                return ActualRresults


            elif Operation_method ==self.basics_quit:
                driver.quit()

            elif Operation_method == self.basics_time:
                self._time_js_input(driver,Positioning_mode,Location_element,Input_content)

            else:
                pass

            print ''

            print output, '-----TRUE'

    # 继承调用selenium方法
    def _case_selenium(self,driver,Operation_method,Positioning_mode,Location_element,Input_content,output):

            ActualRresults=self._case_seleniums(driver,Operation_method,Positioning_mode,Location_element,Input_content,output)

            if Operation_method == self.basics_case:
                test=StringManipulation
                Input_content=test._Case_file(Input_content)

                data_case = xlrd.open_workbook(Input_content)
                table = data_case.sheet_by_index(0)
                # 获取excel的总行数
                nrows_case = table.nrows
                agin_values=[]
                for i in range(1, nrows_case):
                    value_exc = table.row_values(i)
                    agin_values.append(value_exc)
                for value in agin_values:

                    # 操作方法
                    Operation_method = value[0]
                    # 定位方式
                    Positioning_mode = value[1]
                    # 定位元素
                    Location_element = value[2]
                    # 输入内容
                    Input_content = value[3]
                    # log print
                    output = value[4]

                    ActualRresults = self._case_seleniums(driver, Operation_method, Positioning_mode, Location_element, Input_content,output)
                    if ActualRresults:
                       return ActualRresults
            return ActualRresults
























































