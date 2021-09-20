import csv
import pymysql
import time
import re
import logging
logging.basicConfig(level=logging.DEBUG)
conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456',
    port=3306,
    database = 'cloudmusic',
    charset = 'utf8'
)
cursor = conn.cursor()
def main():
    with open(r'F:..\Data\playlists3.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            time.sleep(0.1)
        # print(re.sub('[\r\n\t]', '', row))

            playlistID = row[0]
            name = row[1]
            playlistType = row[2]
            tags = row[3]
            createTime = row[4]
            updateTime = row[5]
            tracks_num = row[6]
            playCount = row[7]
            subscribedCount = row[8]
            shareCount = row[9]
            commentCount = row[10]
            nickname = row[11]
            gender = row[12]
            userType = row[13]
            vipType = row[14]
            province = row[15]
            city = row[16]
            playlist = [playlistID, name, playlistType, tags, createTime, updateTime,
                    tracks_num, playCount, subscribedCount, shareCount, commentCount,
                    nickname, gender, userType, vipType, province, city]

            play = [createTime, updateTime, playlistType, gender, province, city, name, tags]
            logging.debug(play)
            # save_to_playlists(playlist)

        # 歌单ID、歌单名、歌单类型、标签、创建时间、最后更新时间、歌曲数目，播放量、收藏量、转发量、评论数
        # 用户名、性别、用户类型、VIP类型、省份、城市


def save_to_playlists(l):
    sql = """insert into playlists(id, name, type, tags, create_time, update_time,
                tracks_num, play_count, subscribed_count, share_count, comment_count, nickname,
                gender, user_type, vip_type, province, city)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.execute(sql, (
        l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16]))
        conn.commit()
    except Exception as error:
        conn.rollback()

if __name__ == '__main__':
    main()
