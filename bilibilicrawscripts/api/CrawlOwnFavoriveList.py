
from bilibilicrawscripts.utils import CallApiFunc
from bilibilicrawscripts.utils import LogUtil

class CrawlOwnFavoriveList:

    '''
    爬取个人的所有收藏夹信息
    '''

    FunctionTitle = 'CrawlOwnFavoriveList'


    def __init__(self):
        self.logger = LogUtil.LogUtil().getInstance(self.FunctionTitle)



    def crawlOwnFavoriteList(self, uid):
        
        url = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=' + str(uid) + '&jsonp=jsonp'
        self.logger.info("url: %s", url)
        responseText = CallApiFunc.CallApiFunc().apiRpc(url=url, cookie=True)
        print(responseText)
