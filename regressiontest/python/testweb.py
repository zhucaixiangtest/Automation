# coding:utf-8

import os
import time
import xlrd
import string_manipulation
from open_browser import BrowserOpen
from Callkey import JudgeCase
import customDef


def opens(browsers, website):
    if browsers and website:
        _instance_var = BrowserOpen()
        driver = _instance_var.run_browser(browsers, website)
        return driver
    else:
        print("请检查浏览器和网址填写是否正确...")


def read_cases(case_exc):

    _data_exc = xlrd.open_workbook(case_exc)
    _table_exc = _data_exc.sheet_by_index(0)
    exc_nrows = _table_exc.nrows
    sheet_value = []
    exc_num = 1
    while exc_num < exc_nrows:
        _get_exc_value = _table_exc.row_values(exc_num)
        exc_num += 1

        if _get_exc_value[0] == '':
            continue
        sheet_value.append(_get_exc_value)
    if sheet_value:
        return sheet_value
    else:
        print("excel没有数据")


def case_path(case_name):
    selenium_path = os.path.abspath('..')
    path_exc = selenium_path + '\\cases\\'
    _read_case_path = path_exc + case_name
    return _read_case_path


def case(driver, case_name):
    try:
        read_case_path = case_path(case_name)
        actual_results = 'False'
        expected_results = 'True'

        if case_name:
            print ('**********************CASE START FRO:', read_case_path)
            print ''

            get_exc_list = read_cases(read_case_path)

            for list_exc in get_exc_list:

                operation_method = list_exc[0]

                positioning_mode = list_exc[1]

                location_element = list_exc[2]

                input_contents = list_exc[3]

                input_content = customDef.username_add(input_contents)

                output = list_exc[4]
                _case = JudgeCase()
                get_actual_results = _case.case_selenium(driver,
                                                         operation_method,
                                                         positioning_mode,
                                                         location_element,
                                                         input_content,
                                                         output)

                if get_actual_results == 'False':
                    print("****************************************""CASE END FOR:", read_case_path)
                    return actual_results, expected_results
            print("****************************************""CASE END FOR:", read_case_path)
            return expected_results, expected_results

    except Exception as test_web_log:
        errorlog = str(test_web_log)
        print('未找到页面元素或其他原因')
        print("具体失败原因:" + errorlog)
        im_save = string_manipulation
        im_save.save_img(driver)
        time.sleep(1)
        im_save.write_log_txt(errorlog)
        print("已截图并写入日志到errorlog文件夹")
        driver.quit()
        print("**************************用例执行失败--具体查看日志抛异常")
        print('')
        read_case_path = case_path(case_name)
        print("****************************************CASE END FOR:",
              read_case_path)
        actual_results = 'False'
        expected_results = 'True'
        return actual_results, expected_results

    else:
        pass

    finally:
        print("*******************CASE OVER*********************:")
