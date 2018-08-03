#coding:utf-8

import pymysql
# import cx_Oracle
import ConfigParser
import os
import StringManipulation
from pymongo import MongoReplicaSetClient
from pymongo import MongoClient


class Database():

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.mq = StringManipulation

    #例 Positioning_mode=base_178 数据库地址    Location_element=mycng库  Input_content=sql语句
    def db_mysqls(self,Positioning_mode,Location_element,Input_content):
         # mq =StringManipulation
         self._mysql_p=self.mq._mysql_path()
         self.cf.read(self._mysql_p)

         db_host = self.cf.get(Positioning_mode, "host")
         db_port = self.cf.getint(Positioning_mode, "port")
         db_user = self.cf.get(Positioning_mode, "user")
         db_pwd = self.cf.get(Positioning_mode, "password")
         # print db_host,db_port,db_pwd,db_user
        #连接
         conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pwd, db=Location_element, charset='utf8')
         #游标
         cursor = conn.cursor()
         try:
             cursor.execute(Input_content)
            # print('查询的行数为' + str(rowNums))
             selectResultList = cursor.fetchall()
             for i  in range(len(selectResultList)):
                print '查询出的数据',selectResultList[i]

         except Exception as db_error:
             print("操作数据库存在问题",db_error)

         else:
             print("操作成功")
             print('')
                # sql_value=selectResultList[i]
         finally:
                 conn.commit()
                 cursor.close()
                 conn.close()

    # 操作mongodb
    def db_mongo(self,Positioning_mode,Location_element,Input_content):

        self._mongo_p= self.mq._mongo_path()
        self.cf.read(self._mongo_p)

        db_host = self.cf.get(Positioning_mode, "host")

        operation_mr=['delete','select','update','insert']

        get_mer=Location_element[0:6]

        count_str=Location_element.count('.')

        if Location_element and count_str == 2:

            get_me_list = Location_element.split('.')

            get_method=get_me_list[0]

            get_base=get_me_list[1]

            get_table=get_me_list[2]
            if get_method in operation_mr and get_method and get_base and  get_table:

                print(get_method)
                print(get_base)
                print(get_table)

                # 连接mongodb 目前只写了集群的连接方法
                client = MongoClient(db_host)

                # 目标数据库
                db=eval("client."+get_base)

                # 指定表
                collection = eval("db."+get_table)
                # 需要select
                # Input_content=eval(Input_content)
                if Input_content:
                    if get_method == 'select':
                        Input_content = eval(Input_content)
                        for get_select in collection.find(Input_content):
                            print("查询的数据成功:")
                            print(get_select)

                    elif get_method == 'update':
                        Input_content=eval(Input_content)
                        # print(Input_content)

                        get_find_dict=Input_content[0]
                        get_set_dict=Input_content[1]
                        collection.update(get_find_dict, {"$set":get_set_dict})

                        print("数据修改成功")

                        # collection.update({"userName":"45852488@qq.com"},{"$set":{"code":"1783558010"}})

                    elif get_method =='insert':

                        Input_content=eval(Input_content)
                        if isinstance(Input_content,tuple):
                            print(type(Input_content))
                            insert_list=[]
                            for i in Input_content:
                                insert_list.append(i)
                            collection.insert(insert_list)
                            # print(insert_list)
                            print("插入数据成功")
                        else:
                            collection.insert(Input_content)
                            print("插入数据成功")

                    elif  get_method =='delete':
                        print('delete')
                        Input_content=eval(Input_content)
                        if isinstance(Input_content,tuple):
                            for get_del_data in Input_content:
                                collection.remove(get_del_data)
                                print("数据已删除")

                        else:
                            print("非t")
                            collection.remove(Input_content)
            else:
                print("操作关键字或数据库或表填写格式有误")
        else:
            print("操作关键字或数据库或表填写格式有误")

    # # 操作oracle
    # def db_oracle(self,Positioning_mode,Location_element,Input_content):
    #     oq = StringManipulation
    #     _oracle_p = oq._oracle_file()
    #     self.cf.read(_oracle_p)
    #     db_host = self.cf.get(Positioning_mode, "host")
    #     db_port = self.cf.getint(Positioning_mode, "port")
    #     db_user = self.cf.get(Positioning_mode, "user")
    #     db_pwd = self.cf.get(Positioning_mode, "password")
    #     db_source = self.cf.get(Positioning_mode,'source')
    #     db_port=str(db_port)
    #     db_hosts=db_host+':'+db_port+'/'+db_source
    #     conn=cx_Oracle.connect(db_user,db_pwd,db_hosts)
    #     cursor=conn.cursor()
    #     try:
    #         cursor.execute(Input_content)
    #         if Location_element=='select':
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


"""
#mongodb方法参数解释
Positioning_mode 对应配置文件[base_test],连接指定的mongodb
Location_element  参数格式: 操作方法.数据库.表    
Input_content   增删该查的条件，mongo都是以字典的形式
"""


# 删除数据
# Database().db_mongo('base_test','delete.mydb.email','{"userName" : "1435117266@qq.com"},{"userName" : "1435117288@qq.com"}')
#
# 插数据，多个或单个
# Database().db_mongo('base_test','insert.mydb.email','{"userName":"1435117288@qq.com","code" : "9999999999"},{"userName":"1435117266@qq.com","code" : "99999999999"}')
#
# 查询
# Database().db_mongo('base_test','select.mydb.email','{"userName":"45852488@qq.com"}')
#
#
# 修改
# Database().db_mongo('base_test','update.mydb.email','{"userName":"45852488@qq.com"},{"code":"1783558010","success":True}')
#
# {"code":"9999999999"}
#


