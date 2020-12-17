from bilibili_api import user
from database import Database
import time

db = Database()
uplist = db.get_up_list()
for row in uplist:
    bmid = row['bmid']
    mid = row['mid']
    u = user.get_relation_info(uid=bmid)
    data = {
        'mid' : mid,
        'm_following' : u['following'], #关注数
        'm_follower' : u['follower'], #粉丝数
    }
    db.save_up_data(data)
    time.sleep(0.5)
