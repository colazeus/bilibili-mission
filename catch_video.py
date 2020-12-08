from catcher import Catcher

videoApi = 'http://api.bilibili.com/x/web-interface/view?aid='
aidlist = ["415066206","670085138"]
catcher = Catcher()

def getVideo(aid):
    url = videoApi+aid
    data = catcher.getRes(url)
    if data
        stat = data['stat']

        view = stat['view'] #播放数
        favorite = stat['favorite'] #收藏数
        danmaku = stat['danmaku'] #弹幕数
        reply = stat['reply'] #评论数
        coin = stat['coin'] #投币数
        share = stat['share'] #分享数
        now_rank = stat['now_rank'] #当前排名
        like = stat['like'] #点赞数

for i in aidlist:
    getVideo(i)
