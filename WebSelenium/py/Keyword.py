#coding:utf-8
import os

class keywords():


     def __init__(self):

        #封装的常用动作
        self.clicks='click'
        self.inputs='input'

        #v常用的定位方式
        self.ids='id'
        self.names='name'
        self.xpaths='xpath'

        #输入内容
        self.text='text'

        #强制等待
        self.sleeps='sleep'
        #智能等待
        self.waits='wait'

        #悬浮操作
        self.floats='float'

        #解决js弹窗的方法
        self.prompts='prompt'

        #插件上传
        self.autoits='autoit'
        #input传
        self.input_push='push'


        #option下拉框
        self.options='option'

        #推出浏览器
        self.quits='quit'

        #iframe 切换
        self.iframe_intos='iframe_into'
        self.iframe_outs='iframe_out'

        #找元素 实际结果和预期结果对比
        self.finds='find'

       #键盘操作
        #回车键
        self.enter='enter'


      #数据库语句调用
        self.mysqls='mysql'
        self.oracles='oracle'


      #打开浏览器 excel可能也需要用到
        self.opens='opens'


      #支持的浏览器
        self.chromes='Chrome'
        self.fireFoxs='FireFox'

      #用例继承
        self.case='case'


      #判断下载的文件是否到本地
        self.find_excel='find_excel'

