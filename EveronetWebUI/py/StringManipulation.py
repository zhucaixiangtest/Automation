# coding:utf-8
import datetime
import os

def _filter_value(value):

    if value:
        if isinstance(value, float):

            len_str = str(value)

            len_star = len(len_str)

            len_value = len_star - 2

            get_value = len_str[len_value:]

            if get_value == '.0':

                value = int(value)
                value=str(value)
                return value
            else:
                value=str(value)
                return value
        else:
            return value


def  _selenium_file():
    _selenium_pa = os.path.abspath('..')
    return _selenium_pa



def _Autoit_file(file_name):

    selenium_path= _selenium_file()
    paths = selenium_path + '\\Autoit\\' + file_name

    return  paths


def _push_file(file_name):

    selenium_path = _selenium_file()
    paths = selenium_path + '\\PushFile\\' + file_name
    return paths


def _Case_file(file_name):

    selenium_path = _selenium_file()
    paths = selenium_path + '\\Case\\' + file_name
    return paths

def _oracle_file():

    oracle_path =_selenium_file()
    oracle_path = oracle_path + '\\DBConfig\\' + 'DataBase_oracle.ini'
    return oracle_path

def _mysql_path():
        oracle_path = _selenium_file()
        oracle_path = oracle_path + '\\DBConfig\\' + 'DataBase_mysql.ini'
        return oracle_path


def _mongo_path():
    oracle_path = _selenium_file()
    oracle_path = oracle_path + '\\DBConfig\\' + 'DataBase_mongo.ini'
    return oracle_path


def _pull_file():
    pull_path = _selenium_file()
    path_file = pull_path + '\\PullFile\\'
    return path_file




def _save_img(driver):
    _save_img_path=_selenium_file()
    _save_img_path=_save_img_path+"\\ErrorIMG\\"

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    nowTime=str(nowTime).replace(' ','-')
    nowTime=nowTime.replace(':','-')

    errorImgName=(_save_img_path+nowTime+".png").replace('\\','/')

    driver.save_screenshot(errorImgName)
    return  errorImgName



