#coding:utf-8

import pymysql
# import cx_Oracle
import ConfigParser
import os
# import cx_Oracle



class Database():

    def __init__(self):

        self.cf = ConfigParser.ConfigParser()
        paths=os.path.abspath('..')
        #mysql配置
        self.mysql_path=paths+'\\DBConfig\\'+'DataBase_mysql.ini'

        #oracle配置
        self.oracle_path=paths+'\\DBConfig\\'+'DataBase_oracle.ini'
        self.save_value_path=paths+'\\values\\'+'save_value.txt'




    def db_mysqls(self,Location,dblibrary,sqlmy):

         self.cf.read(self.mysql_path)

         db_host = self.cf.get(Location, "host")
         db_port = self.cf.getint(Location, "port")
         db_user = self.cf.get(Location, "user")
         db_pwd = self.cf.get(Location, "password")
         # print db_host,db_port,db_pwd,db_user
        #连接

         conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pwd, db=dblibrary, charset='utf8')
         #游标
         cursor = conn.cursor()

         rowNums = cursor.execute(sqlmy)
        # print('查询的行数为' + str(rowNums))
         selectResultList = cursor.fetchall()
         for i  in range(len(selectResultList)):
            print '查询出的数据'
            print selectResultList[i][0]
            sql_value=selectResultList[i][0]
            sql_value=str(sql_value)
            f = open(self.save_value_path,'wb')
            f.write(sql_value)
            f.close()


            return sql_value
         print '操作成功'

         conn.commit()

         cursor.close()

         conn.close()

    # def db_oracle(self,Location,element,sqlorc):
    #
    #     self.cf.read(self.oracle_path)
    #     db_host = self.cf.get(Location, "host")
    #     db_port = self.cf.getint(Location, "port")
    #     db_user = self.cf.get(Location, "user")
    #     db_pwd = self.cf.get(Location, "password")
    #     db_port=str(db_port)
    #     db_hosts=db_host+':'+db_port+'/setdb'
    #
    #     conn=cx_Oracle.connect(db_user,db_pwd,db_hosts)
    #     cursor=conn.cursor()
    #
    #     cursor.execute(sqlorc)
    #     if element=='select':
    #         data=cursor.fetchall()
    #         for i in data:
    #             print i
    #     else:
    #         pass
    #     print '操作成功'
    #
    #     cursor.close()
    #
    #     conn.commit()
    #
    #     conn.close()

# if __name__=='_main_':
#
#     pass
# else:
#     sql="DELETE FROM TBL_WILD_ERROR where file_date='20180226' and card_brand='VIS'"
#     Database().db_mysqls('base_178','mspcfg',sql)
#

