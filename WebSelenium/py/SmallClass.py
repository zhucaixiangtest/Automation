#coding:utf-8

def Transformation(value):

    if isinstance(value,float):

        len_str=str(value)

        len_star=len(len_str)

        len_value=len_star-2

        get_value=len_str[len_value:]

        if get_value=='.0':

            value=int(value)
            return value
        else:
            return value
    else:
        return  value




