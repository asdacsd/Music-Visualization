from flask import Flask, render_template, url_for
import json
import pandas as pd
import pymysql
import re


app = Flask(__name__)

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456',
    port=3396,
    database = 'cloudmusic',
    charset = 'utf8'
)

df = pd.read_sql('select * from playlists2', con=conn)




def get_track_data():
    
    bins = [0, 50, 150, 500, 100000]
    cuts = pd.cut(df['tracks_num'], bins=bins, right=False, include_lowest=True)
    data_count = cuts.value_counts()
    print(data_count)
    data = dict(zip([str(x) for x in data_count.index.tolist()], data_count.tolist()))
    print(data)
    map_data = [{'name': name, 'value': value} for name, value in data.items()]
    track_value = {'t_v': map_data}

    return json.dumps(track_value, ensure_ascii=False)

if __name__ == '__main__':
    get_track_data()
# """语种类型歌单播放量"""
# @app.route('/get_type_data')
# def get_type_data():
#     playlist_type_df = df[['type', 'play_count']].groupby(df['type']).sum()
#     # 歌曲标签 播放量
#     playlist_type_df = playlist_type_df.loc[['华语','欧美','粤语', '日语', '韩语'], :]
#     data = dict(zip(playlist_type_df.index.tolist(), playlist_type_df['play_count'].tolist()))
#     map_data = [{'name': name, 'value': value} for name, value in data.items()]
#     type_sum = {'t_s': map_data}
#
#     return json.dumps(type_sum, ensure_ascii=False)
#
