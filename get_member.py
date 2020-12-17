from bilibili_api import user
from database import Database
import time

db = Database()
#videolist = db.get_video_list()

u = user.get_videos(uid="177707419")
print(u)
