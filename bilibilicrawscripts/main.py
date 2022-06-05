

import sys
import logging
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import *
from api.model import *
from api.CrawlUpsVideoInfo import *

CrawlUpsVideoInfo().CrawlAllVideosOfAUP(mid=928123)