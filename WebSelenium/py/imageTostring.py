#coding:utf-8
import time
import re
import urllib2
import urllib
from PIL import Image
from io import BytesIO




#后期再解决验证码识别问题，目前解决方式定位在 三方api处理
class CaptchaAPI:
    def __init__(self, timeout=60):
        self.api_key = '××××××××'
        self.timeout = timeout
        self.url = 'https://www.9kw.eu/index.cgi'

    def solve(self, img):
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        img_data = img_buffer.getvalue()
        captcha_id = self.send(img_data)
        start_time = time.time()
        while time.time() < start_time + self.timeout:
            try:
                text = self.get(captcha_id)
            except CaptchaError:
                pass  # CAPTCHA still not ready
            else:
                if text != 'NO DATA':
                    if text == 'ERROR NO USER':
                        raise CaptchaError('Error: no user available to solve CAPTCHA')
                    else:
                        print 'CAPTCHA solved!'
                        return text
            print 'Waiting for CAPTCHA ...'
        raise CaptchaError('Error: API timeout')

    def send(self, img_data):
        print 'submitting...'
        data = {
            'action': 'usercaptchaupload',
            'apikey': self.api_key,
            'file_upload_01': img_data.encode('base64'),
            'base64': '1',
            'selfsolve': '0',
            'maxtimeout': str(self.timeout)
        }
        encoded_data = urllib.urlencode(data)
        request = urllib2.Request(self.url, encoded_data)
        response = urllib2.urlopen(request)
        result = response.read()
        self.check(result)
        return result

    def get(self, captcha_id):
        data = {
            'action': 'usercaptchacorrectdata',
            'id': captcha_id,
            'apikey': self.api_key,
            'info': '1'
        }
        encoded_data = urllib.urlencode(data)
        response = urllib2.urlopen(self.url + '?' + encoded_data)
        result = response.read()
        self.check(result)
        return result

    def check(self, result):
        if re.match('00\d\d \w+', result):
            raise CaptchaError('API error:' + result)


class CaptchaError(Exception):
    pass

if __name__ == '__main__':
    captcha = CaptchaAPI()
    img = Image.open('x.PNG')
    text = captcha.solve(img)
    print text




#方式2  扯淡的库对于市场常用的验证码毫无用处，除非特简单的验证码
# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\\Tesseract-OCR\\tesseract'
# tessdata_dir = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\\tessdata"'
#
#
# img = Image.open('D:/WebSelenium/PullFile/captcha.jpg')
# time.sleep(3)
# aa=pytesseract.image_to_string(image=img, lang='eng', config=tessdata_dir)
# time.sleep(3)
# print aa
