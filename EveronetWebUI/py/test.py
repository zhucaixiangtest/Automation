# coding:utf-8

import time
from pymongo import MongoReplicaSetClient
from pymongo import MongoClient



# 连接集群
client = MongoClient("mongodb://quickpay:quickpay@test.ipay.so:27017,test.ipay.so:27018,test.ipay.so:27019/quickpay?")

# 连接目标数据库
db = client.quickpay

# 指定表
collection=db.email

# 查找集合中所有数据
for item in collection.find():
    print item

# #查找集合中单条数据
# print collection.find_one()
#
#
# # # 用户名密码
# db.authenticate("quickpay", "quickpay")
import re
m = re.search('Multi', 'multI1', re.IGNORECASE)
print bool(m)


# from selenium import webdriver
#
#
# br=webdriver.PhantomJS()
# br.maximize_window()
# br.get("https://www.cnblogs.com/Jack-cx/p/9383990.html")
#
#
# br.save_screenshot("e:/app1.png")


a={"q":"q"},{"a":"a"}

print(a[0])