# coding:utf-8

import string_manipulation


def username_add(input_content):

    if isinstance(input_content, float) or isinstance(input_content, int) or input_content == '':
        return input_content

    else:

        lens = len(input_content)-1
        if input_content[0:2] == '${' and input_content[lens] == '}':
            if input_content[2:5] == 'str':
                str_value = input_content[5:lens]
                int_value = eval(str_value)
                input_content = string_manipulation.get_now_time() + 'x' * int_value
                f = open('..\\config\\randomStr.txt', 'w')
                f.write(input_content)
                f.close()
                return input_content

            elif input_content[2:lens] == 'getStr':
                input_content = string_manipulation.read_txt()
                return input_content

            elif input_content[2:lens] == 'getSave':
                input_content = string_manipulation.get_save_value()
                return input_content
        else:
            return input_content
