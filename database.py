import pymysql
import time

class Database:

    ip = "localhost"
    port = 3306
    db_name = "ba"
    user = "bilibili"
    pawd = "u14YfU1YwLf12igVu14YfU1YwLf12igV"

    #保存视频数据
    def save_video_data(self,data):
        db = pymysql.connect(host=Database.ip,port=Database.port,user=Database.user,passwd=Database.pawd,db=Database.db_name,charset='utf8')
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "SELECT * FROM base_video_data WHERE bvid = '%s' order by id desc limit 1" % (data['bvid'])
        cursor.execute(sql)
        res = cursor.fetchone()
        if res is None or res['v_view'] != data['view']:
            sql = "INSERT INTO base_video_data(\
                  bvid, v_view, v_favorite, v_danmaku, v_reply, v_coin, v_share, v_now_rank, v_like) \
                  VALUES ('%s', %s, %s, %s, %s, %s,  %s,  %s,  %s)" % \
                  (data['bvid'],data['view'],data['favorite'],data['danmaku'],data['reply'],data['coin'],data['share'],data['now_rank'],data['like'])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        db.close()

    #获取捕获视频列表
    def get_video_list(self):
        db = pymysql.connect(host=Database.ip,port=Database.port,user=Database.user,passwd=Database.pawd,db=Database.db_name,charset='utf8')
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "SELECT * FROM get_video_list WHERE expiration_time > '%s'" % (time.strftime('%Y-%m-%d %H:%M:%S'))
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except:
            print ("Error: unable to fetch data")
