# coding:utf-8
from BrowserClass import Browser_names
from ReadExcelClass import ReadExcel,_get_excel_datas
import os
from selenium import webdriver



def opens(browsers,website):

    if browsers and website:

       test=Browser_names()

       driver=test._run_browser(browsers,website)

       return driver

    else:
       print("请检查浏览器和网址填写是否正确...")


def Case(driver,case_name):
    if case_name:
        selenium_path=os.path.abspath('..')
        path_exc=selenium_path+'\\Case\\'
        _read_case_path=path_exc+case_name
        print ('**********************正在执行用例：',_read_case_path)
        print ''
        try:
            _get_excel_datas()._Handle_data(driver,_read_case_path)
        except Exception as _log_error:
            driver.quit()
            go_pass=("invalid syntax (<string>, line 1)")
            _log_errors=str(_log_error)
            if _log_errors==go_pass:
                pass
            else:
                print(_log_error)
            print ('*******************此用例执行失败具体查看log.*********************************')
            yu_str='True'
            shi_str='False'
            print ('')
            print ('**********************用例执行完：', _read_case_path)
            print ('')
            return yu_str,shi_str
        else:
            print ('**********************用例执行完：', _read_case_path)
            yu_str = ('True')
            shi_str = ('True')
            return yu_str, shi_str
        finally:
            pass

br=webdriver.Chrome()
br.get("http://www.aliyun.com")
br.maximize_window()
Case(br,"aliyun.xls")