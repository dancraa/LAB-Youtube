import youtube
import datetime

fpath = r"data\MX_Youtube_2017_utf8.csv"

ylist = youtube.lee_trending_videos(fpath)
#print(ylist)
#print(youtube.media_visitas(ylist, datetime.datetime.strptime("15/11/2017", "%d/%m/%Y")))
print(youtube.video_mayor_ratio_dislikes(ylist, "Education"))