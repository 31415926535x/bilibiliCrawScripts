

import sys
import logging
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import *
from api.model import *
from api import *
from api.CrawlOwnFavoriveList import *



# 获取mid下的所有视频信息
# CrawlUpsVideoInfo().CrawlAllVideosOfAUP(mid=928123)


# 获取个人的收藏夹信息

CrawlOwnFavoriveList().crawlOwnFavoriteList(uid=10330740)