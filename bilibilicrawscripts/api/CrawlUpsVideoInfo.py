"""

    利用接口 ``https://api.bilibili.com/x/space/arc/search?mid=mid&ps=30&tid=0&pn=pn&keyword=&order=pubdate&jsonp=jsonp``
    来获取一个up（id为mid）的所有视频的av号
    其中用pn参数来获取每一页的视频信息，每一页的视频的个数最多为ps个，这里的ps的默认取值是30，我发现它貌似最大能取100，所以为了效率就去100来爬
    如爬取评论一样，利用总的视频数和当前爬到的视频数来控制爬虫的结束与否，一个up所投稿的总视频数在 ``json['data']['page']['count']``
    视频的详细信息在 ``json['data']['list']['vlist']``
    av号即aid，还有时长、描述、播放量、评论量以及视频封面链接等信息（提取视频的封面的方法应该就是直接访问的这个api，这样可以用js写一个请求就可以搞定）
    我这里只需要av号，根据使用情况来添加参数即可

"""


from .model import VideoInfo
# from ..utils import LogUtil
import requests
from bilibilicrawscripts.utils import LogUtil
import json as JSON
import time 

class CrawlUpsVideoInfo:

    FunctionTitle = 'CrawlUpsVideoInfo'

    # 单个up最大的爬取视频的个数
    maxVideoNum = 100

    def __init__(self):
        self.logger = LogUtil.LogUtil().getInstance(self.FunctionTitle)
        
    def CrawlAllVideosOfAUP(self, mid, ps = 100, maxVideoNum=100):
        """
            mid: 一个up的id，理论上发过视频的up都可以通过另一个api找到它的mid，这里假定手动获取到了mid
            ps: 一次爬取的视频的最大个数，不超过100
            return videos: 返回所有的投稿视频的信息（根据自己所需添加信息，我这里只有一串av号）
        """

        self.logger.info("Getting mid: %s 's all videos...", mid)
        

        videosCount = 1
        videosID = 0
        flag = True
        mid = str(mid)
        videos = []
        pn = 1
        if(ps > 50):
            ps = 50
        ps = str(ps)
        while(videosID < videosCount):
            if (videosCount > 10):
                # 防止被限流
                time.sleep(1)

            url = "https://api.bilibili.com/x/space/arc/search?mid=" + mid + "&ps=" + ps + "&tid=0&pn=" + str(pn) + "&keyword=&order=pubdate&jsonp=jsonp"
            self.logger.info(url)
            responseText = JSON.loads("{}")
            try:
                response = requests.get(url)
                responseText = JSON.loads(response.text)
            except: 
                self.logger.error(self.FunctionTitle + "craw mid=%s failed", str(mid))
            
            self.logger.info("request code: %d, msg: %s" % ((responseText['code']), str(responseText['message'])))
            data = responseText['data']
            if (None == data):
                self.logger.error(self.FunctionTitle + "craw mid=%s failed, data is null", str(mid))
                break

            if(flag):
                videosCount = data['page']['count']
                videosCount = min(videosCount, maxVideoNum)
                if (maxVideoNum == videosCount):
                    self.logger.info("this mid is a King of GAN.")
                flag = False
            
            pn += 1

            vlist = data['list']['vlist']
            vlistCount = len(vlist)
            for i in range(0, vlistCount):
                videosID += 1
                videoInfo = self.buildVideoInfo(vlist[i])
                videos.append((videoInfo.aid, videoInfo))
        
        self.logger.info("Got all " + mid + " 's videos")
        return videos

    def buildVideoInfo(self, viedo):
        ret = VideoInfo.VideoInfo()
        ret.comentNum = viedo['comment']
        ret.playNum = viedo['play']
        ret.picUrl = viedo['pic']
        ret.desc = viedo['description']
        ret.title = viedo['title']
        ret.mid = viedo['mid']
        ret.mid = viedo['mid']
        ret.createdTime = viedo['created']
        ret.createdTime = viedo['created']
        ret.aid = viedo['aid']
        ret.bvid = viedo['bvid']
        self.logger.info("video info: %s", ret)
        return ret
