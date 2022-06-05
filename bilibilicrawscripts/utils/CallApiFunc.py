

import requests
from bilibilicrawscripts.utils import LogUtil
import json as JSON


class CallApiFunc:

    '''
    调用api包装类
    '''

    FunctionTitle = 'CallApiFunc'

    cookieFilePath = r'bilibilicrawscripts\setUp\cookie.txt'


    # 添加请求头
    # TODO 更换多种 agent
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    }

    def __init__(self):
        self.logger = LogUtil.LogUtil().getInstance(self.FunctionTitle)
        self.headers['Cookie'] = self.loadCookie();

    def apiRpc(self, url, postParm=None, cookie=False):
        
        self.logger.info(url)
        responseText = JSON.loads("{}")
        try:
            response = None
            if (postParm == None):
                response = requests.get(url, headers=self.headers)
            else:
                response = requests.post(url=url, data=postParm, headers=self.headers)
            responseText = JSON.loads(response.text)
        except: 
            self.logger.error(self.FunctionTitle + "craw url failed.", str(url))

        # no need log this response, cause it may be big
        return responseText

    

    def loadCookie(self):
        # TODO load cookie try catch
        # TODO load cookie by module

        cookie = None
        with open(self.cookieFilePath, 'r') as file:
            cookie = file.read()
            self.logger.debug(self.FunctionTitle + " cookie: %s", cookie)
        return cookie