# --***--coding:utf-8 -----***---

import datetime


def write_log_txt(error_log):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    str_time = str(now_time)
    touch_txt = str_time[0:10]
    try:
        write_text = open('../error_log/log/' + touch_txt + '.txt', 'a')
        write_text.write(str_time + ':' + ' ' * 5 + error_log + '\n' + "" + '\n')
    except IOError:
        print("写入log错误")

    else:
        write_text.close()

    finally:
        pass


write_log_txt("你好")