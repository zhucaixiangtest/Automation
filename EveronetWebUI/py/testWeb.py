# coding:utf-8

import StringManipulation
from BrowserClass import Browser_names
import os
from KeyWord import Basics_key
from Callkey import Judge_use_case
from selenium import webdriver
import time
import xlrd

def opens(browsers,website):

    if browsers and website:

       test=Browser_names()

       driver=test._run_browser(browsers,website)
       return driver

    else:
       print("请检查浏览器和网址填写是否正确...")


def Readcase(case):

    _data_exc = xlrd.open_workbook(case)
    _table_exc = _data_exc.sheet_by_index(0)
    exc_nrows = _table_exc.nrows
    sheet_value=[]
    exc_num=1

    while exc_num < exc_nrows:

        _get_exc_value = _table_exc.row_values(exc_num)
        exc_num+=1

        if _get_exc_value[0] =='':
            continue
        sheet_value.append(_get_exc_value)

    if sheet_value:
        return sheet_value

    else:
        print("excel没有数据")

def  _case_path(case_name):

        selenium_path=os.path.abspath('..')
        path_exc=selenium_path+'\\Case\\'
        _read_case_path=path_exc+case_name
        return _read_case_path


def Case(driver,case_name):

    try:
            _read_case_path= _case_path(case_name)
            ActualResults='False'
            ExpectedResults='True'

            if case_name:
                print ('**********************正在执行用例:'+_read_case_path)
                print ''

                get_exce_datas=Readcase(_read_case_path)

                for list_exc in get_exce_datas:

                    Operation_method=list_exc[0]

                    Positioning_mode = list_exc[1]

                    Location_element = list_exc[2]

                    Input_content = list_exc[3]

                    output = list_exc[4]
                    _case_run=Judge_use_case()
                    get_ActualResults=_case_run._case_selenium(driver,Operation_method,Positioning_mode,Location_element,Input_content,output)
                    if get_ActualResults == 'False':
                        print("****************************************用例执行完毕:"+_read_case_path)
                        return ActualResults,ExpectedResults

                print("****************************************用例执行完毕:"+_read_case_path)
                return ExpectedResults,ExpectedResults

    except Exception as error_logs:
        print('未找到页面元素或其他原因')
        print("(具体失败原因:)", error_logs)

        StringManipulation._save_img(driver)
        time.sleep(2)
        print("已截图到ErrorIMG文件夹")

        driver.quit()
        print("**************************用例执行失败--具体查看日志抛异常")
        print('')
        _read_case_path= _case_path(case_name)
        print("****************************************用例执行完毕:"+_read_case_path)
        ActualResults='False'
        ExpectedResults='True'
        return ActualResults,ExpectedResults

    else:
        pass

    finally:
        pass