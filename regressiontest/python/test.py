# --***--coding:utf-8 -----***---
import os


def file_name(file_dir):
    for va1, va2, name in os.walk(file_dir):
        print(va1)
        print(va2)
        print name




file_name('F:\\testWeb\\UI\\regressiontest\\config')