# coding:utf-8

import datetime


def get_now_time():

    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    value = str(now_time).replace(' ', '')
    value = value.replace(':', '')
    value = value.replace('-', '')
    get_time_value = open('..\\config\\randomStr.txt', 'w')
    get_time_value.write(value)
    get_time_value.close()
    return value


def read_txt():
    get_time_value = open('..\\config\\randomStr.txt', 'r')
    txt_f = get_time_value.readline()
    get_time_value.close()
    return txt_f


def filter_value(value):

    if value:
        if isinstance(value, float):
            len_str = str(value)
            len_star = len(len_str)
            len_value = len_star - 2
            get_value = len_str[len_value:]
            if get_value == '.0':
                value = int(value)
                value = str(value)
                return value
            else:
                value = str(value)
                return value
        else:
            return value
    else:
        pass


# def selenium_file():
#     _selenium_pa = os.path.abspath('..')
#     return _selenium_pa


def auto_it_file(file_name):

    # selenium_path= selenium_file()
    paths = '..\\third_tools\\auto_it\\' + file_name
    return paths


def push_file(file_name):

    # selenium_path = _selenium_file()
    paths = '..\\upload\\' + file_name
    return paths


def case_file(file_name):

    # selenium_path = _selenium_file()
    paths = '..\\cases\\' + file_name
    return paths


def _oracle_file():
    oracle_path = '..\\config\\' + 'DataBase_oracle.ini'
    return oracle_path


def mysql_path():
        # oracle_path = _selenium_file()
    oracle_path = '..\\config\\' + 'DataBase_mysql.ini'
    return oracle_path


def mongodb_path():
    # oracle_path = _selenium_file()
    mongodb_path = '..\\config\\' + 'DataBase_mongodb.ini'
    return mongodb_path


def pull_file():
    # pull_path = _selenium_file()
    path_file = '.\\download\\'
    return path_file


def save_img(driver):

    # _save_img_path = _selenium_file()
    _save_img_path = '..\\error_log\\image\\'
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    now_time = str(now_time).replace(' ', '-')
    now_time = now_time.replace(':', '-')
    error_img = (_save_img_path+now_time+".png").replace('\\', '/')
    driver.save_screenshot(error_img)
    return error_img


def write_log_txt(error_log):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    str_time = str(now_time)
    touch_txt = str_time[0:10]
    try:
        write_text = open('../error_log/log/' + touch_txt + '.txt', 'a')
        write_text.write(str_time + ':' + ' ' * 5 + error_log + '\n' + "" + '\n')
    except IOError:
        print("写入log错误,无此目录")

    else:
        write_text.close()

    finally:
        pass




