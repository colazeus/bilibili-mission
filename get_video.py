from bilibili_api import video
from database import Database
import time

db = Database()
videolist = db.get_video_list()

for row in videolist:
    bvid = row['bvid']
    vid = row['vid']
    v = video.get_video_info(bvid=bvid)
    stat = v["stat"]
    data = {
        'vid' : vid,
        'view' : stat['view'], #播放数
        'favorite' : stat['favorite'], #收藏数
        'danmaku' : stat['danmaku'], #弹幕数
        'reply' : stat['reply'], #评论数
        'coin' : stat['coin'], #投币数
        'share' : stat['share'], #分享数
        'now_rank' : stat['now_rank'], #当前排名
        'like' : stat['like'] #点赞数
    }
    db.save_video_data(data)
    time.sleep(0.5)
