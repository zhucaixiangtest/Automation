# coding:utf-8

import ConfigParser
import pymysql
# import cx_Oracle
from pymongo import MongoClient
import string_manipulation


class Database(object):

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.mq = string_manipulation

    # 例 positioning_mode=base_178 数据库地址
    #   location_element=my cng库  input_content=sql语句
    def db_mysql(self, positioning_mode, location_element, input_content):

        sqlmy_file = self.mq.mysql_path()
        self.cf.read(sqlmy_file)

        db_host = self.cf.get(positioning_mode, "host")
        db_port = self.cf.getint(positioning_mode, "port")
        db_user = self.cf.get(positioning_mode, "user")
        db_pwd = self.cf.get(positioning_mode, "password")
        conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pwd, db=location_element, charset='utf-8')
        cursor = conn.cursor()

        try:
            cursor.execute(input_content)
            mysql_result = cursor.fetchall()
            for i in range(len(mysql_result)):
                print '查询出的数据', mysql_result[i]
        except Exception as db_error:

            print("操作数据库存在问题", db_error)
        else:
            print("操作成功")
            print('')
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    # 操作mongodb
    def db_mongodb(self, positioning_mode, location_element, input_content):

        mongodb_file = self.mq.mongodb_path()
        self.cf.read(mongodb_file)

        db_host = self.cf.get(positioning_mode, "host")

        operation_mr = ['delete', 'select', 'update', 'insert']

        # get_mer = location_element[0:6]

        count_str = location_element.count('.')

        if location_element and count_str == 2:

            get_me_list = location_element.split('.')

            get_method = get_me_list[0]

            get_base = get_me_list[1]

            get_table = get_me_list[2]
            if get_method in operation_mr and get_method and get_base and get_table:

                print(get_method)
                print(get_base)
                print(get_table)

                # 连接mongodb 目前只写了集群的连接方法
                client = MongoClient(db_host)
                print(client)
                # 目标数据库
                db = eval("client."+get_base)
                print(db)
                # 指定表
                collection = eval("db."+get_table)
                # 需要select
                if input_content:
                    if get_method == 'select':
                        input_content = eval(input_content)
                        for get_select in collection.find(input_content):
                            print("查询的数据成功:")
                            print(get_select)

                    elif get_method == 'update':
                        input_content = eval(input_content)
                        get_find_dict = input_content[0]
                        get_set_dict = input_content[1]
                        collection.update(get_find_dict, {"$set": get_set_dict})
                        print("数据修改成功")

                    elif get_method == 'insert':
                        input_content = eval(input_content)
                        if isinstance(input_content, tuple):
                            print(type(input_content))
                            insert_list = []
                            for i in input_content:
                                insert_list.append(i)
                            collection.insert(insert_list)
                            print("插入数据成功")
                        else:
                            collection.insert(input_content)
                            print("插入数据成功")

                    elif get_method == 'delete':
                        input_content = eval(input_content)
                        if isinstance(input_content, tuple):
                            for get_del_data in input_content:
                                collection.remove(get_del_data)
                                print("数据已删除")

                        else:
                            collection.remove(input_content)
            else:
                print("操作关键字或数据库或表填写格式有误")
        else:
            print("操作关键字或数据库或表填写格式有误")

    # 操作oracle
    # def db_oracle(self, positioning_mode, location_element, input_content):
    #     oq = StringManipulation
    #     _oracle_p = oq._oracle_file()
    #     self.cf.read(_oracle_p)
    #     db_host = self.cf.get(positioning_mode, "host")
    #     db_port = self.cf.getint(positioning_mode, "port")
    #     db_user = self.cf.get(positioning_mode, "user")
    #     db_pwd = self.cf.get(positioning_mode, "password")
    #     db_source = self.cf.get(positioning_mode, 'source')
    #     db_port=str(db_port)
    #     db_hosts=db_host+':'+db_port+'/'+db_source
    #     conn=cx_Oracle.connect(db_user, db_pwd, db_hosts)
    #     cursor=conn.cursor()
    #     try:
    #         cursor.execute(input_content)
    #         if location_element=='select':
    #             data=cursor.fetchall()
    #             for i in data:
    #                 print i
    #     except Exception as db_error:
    #         print(db_error)
    #
    #     else:
    #         print '操作成功'
    #
    #     finally:
    #         cursor.close()
    #         conn.commit()
    #         conn.close()
