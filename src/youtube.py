from typing import NamedTuple
from datetime import datetime, date
import csv
import statistics

Video = NamedTuple('Video', 
[('id_video', str),
 ('fecha_trending', date),
 ('titulo', str),
 ('canal', str),
 ('categoria', str),
 ('visitas', int),
 ('likes', int),
 ('dislikes', int)
])

def lee_trending_videos(file):
    with open(file, encoding="UTF-8") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        return [Video(id_video=str(id), fecha_trending=datetime.strptime(fecha_trending, "%d/%m/%Y"), titulo=str(titulo), \
                    canal=str(canal), categoria=str(categoria), visitas=int(visitas), likes=int(likes), dislikes=int(dislikes)) \
                    for id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes in reader]
                    
def media_visitas(videos, fecha):
    try: return statistics.mean(video.visitas for video in videos if video.fecha_trending == fecha)
    except: return 0

def video_mayor_ratio_dislikes(videos, cat=None):
    if not cat: return max(videos, key=lambda x: (x.likes / x.dislikes if x.dislikes != 0 else 0))
    return max(videos, key=lambda x: x.likes / x.dislikes if x.dislikes != 0 and x.categoria == cat else 0)