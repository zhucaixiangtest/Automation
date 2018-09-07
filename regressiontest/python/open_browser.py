# coding:utf-8

from selenium import webdriver


class BrowserOpen(object):

    def __init__(self):

        self.chromes = 'Chrome'
        self.fire_fox = 'FireFox'
        self.phantom_js = 'PhantomJS'
        self.ies = 'Ie'
        self.edges = 'Edge'
        self.home_http = 'http'

    def run_browser(self, browsers, website):
        # 调用谷歌浏览器并配置下载路径，下载用例需要这样的方法
        if browsers == self.chromes and self.home_http in website:
            options = webdriver.ChromeOptions()
            # path = os.path.abspath("..")
            file_path = "..\\download"

            pre_fs = {'profile.default_content_settings.popups': 0,
                      'download.default_directory': file_path}
            options.add_experimental_option('prefs', pre_fs)
            if website != '':
                br_driver = webdriver.Chrome(chrome_options=options)
                br_driver.maximize_window()
                br_driver.get(website)
                return br_driver

        # 调用ie11浏览器
        elif browsers == self.ies and self.home_http in website:
            br_driver = webdriver.Ie()
            br_driver.maximize_window()
            br_driver.get(website)
            return br_driver

        #  调用win10自带edge浏览器
        elif browsers == self.edges and self.home_http in website:
            br_driver = webdriver.Edge()
            br_driver.maximize_window()
            br_driver.get(website)
            return br_driver

        # 调用火狐浏览器
        elif browsers == self.phantom_js and self.home_http in website:
            br_driver = webdriver.Firefox()
            br_driver.maximize_window()
            br_driver.get(website)
            return br_driver

        elif browsers == self.phantom_js and self.home_http in website:
            br_driver = webdriver.PhantomJS()
            br_driver.maximize_window()
            br_driver.get(website)
            return br_driver

        elif browsers[0] == 'c' or browsers[0] == 'f':
            print ("填写浏览器名时首字母请大写")

        elif self.home_http not in website:
            print ("注意填写网址是需要加上http://...")

        else:
            print ('暂时不支持其他浏览器，可在browser class中添加')
