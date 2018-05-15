#coding:utf-8
try:
    import pymysql
    import cx_Oracle
except Exception as install_error:
    print install_error
else:
    import ConfigParser
    import os
    import StringManipulation



class Database():

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()

    #例 Positioning_mode=base_178 数据库地址    Location_element=mycng库  Input_content=sql语句
    def db_mysqls(self,Positioning_mode,Location_element,Input_content):
         mq =StringManipulation
         self._mysql_p=mq._mysql_path()
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

    # 操作oracle
    def db_oracle(self,Positioning_mode,Location_element,Input_content):
        oq = StringManipulation
        _oracle_p = oq._oracle_file()
        self.cf.read(_oracle_p)
        db_host = self.cf.get(Positioning_mode, "host")
        db_port = self.cf.getint(Positioning_mode, "port")
        db_user = self.cf.get(Positioning_mode, "user")
        db_pwd = self.cf.get(Positioning_mode, "password")
        db_source = self.cf.get(Positioning_mode,'source')
        db_port=str(db_port)
        db_hosts=db_host+':'+db_port+'/'+db_source
        conn=cx_Oracle.connect(db_user,db_pwd,db_hosts)
        cursor=conn.cursor()
        try:
            cursor.execute(Input_content)
            if Location_element=='select':
                data=cursor.fetchall()
                for i in data:
                    print i
        except Exception as db_error:
            print(db_error)

        else:
            print '操作成功'

        finally:
            cursor.close()
            conn.commit()
            conn.close()