# coding:utf-8
import xlrd
from KeyWord import Basics_key
from Callkey import Judge_use_case
from selenium import webdriver

class ReadExcel():

    def _start_(self):

        pass

    def Readcase(self,case):
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


class _get_excel_datas(ReadExcel,Basics_key):

    def _Handle_data(self,driver,case):

        get_exce_datas=self.Readcase(case)

        for list_exc in get_exce_datas:

            self.Operation_method=list_exc[0]

            self.Positioning_mode = list_exc[1]

            self.Location_element = list_exc[2]

            self.Input_content = list_exc[3]

            self.output = list_exc[4]

            _case_run=Judge_use_case()
            _case_run._case_selenium(driver,self.Operation_method,self.Positioning_mode,self.Location_element,self.Input_content,self.output)