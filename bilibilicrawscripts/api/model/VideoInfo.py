from dataclasses import dataclass

@dataclass
class VideoInfo:

    '''
    一个视频的基本信息
    '''

    # 评论数
    comentNum: int = 0

    # 播放数
    playNum: int = 0

    # 封面url
    picUrl: str = ''

    # 视频简介
    desc: str = ''

    # 标题
    title: str = ''

    # 视频up的uid
    mid: int = 0

    # 发布时间
    createdTime: int = 0

    # 视频id(av号)
    aid: int = 0

    # 视频id(bv号)
    bvid: str = ''
