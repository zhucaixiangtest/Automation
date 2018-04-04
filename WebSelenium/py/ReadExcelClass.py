#coding:utf-8
import xlrd
from MainMethodClass import run_main
import SmallClass
from Keyword import keywords
from MainMethodClass import case_get


class ReadExcel(keywords):

#初始化
    def start(self):
        pass


    def Readcasea(self,case):
        data = xlrd.open_workbook(case)
        table = data.sheet_by_index(0)
        # 获取excel的总行数
        rows = table.nrows
        get_sheet=[]
        _run_rows=1
        while _run_rows<rows:
             value = table.row_values(_run_rows)

             get_sheet.append(value)

             _run_rows+=1


        return get_sheet







        # for i in range(1,nrows):
        #     value = table.row_values(i)
        #     get_values=get_sheet.append(value)
        #     # if value[0]=='':
        #     #        continue
        # print get_values



    def  Readcase(self,driver,case):

        get_values=self.Readcasea(case)

        for value in get_values:
            if value[0]=='':
                continue

            #操作方法
            method=value[0]
            #定位方式
            Location=value[1]
            #定位元素
            element=value[2]
            #输入内容
            # text=SmallClass.Transformation(value[3])
            text=value[3]
            #log print
            logs=value[4]

            #根据excel走方法
            run_main().runs(driver,method,Location,element,text,logs)
            case_get().case_again(driver,method,text)

            if method==self.quits:
                driver.quit()
            else:
                pass


