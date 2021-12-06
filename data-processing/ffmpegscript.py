import os
import datetime


def ffscr(bigcount, prefix, path):
    i = 1
    while i < 1320:
        conversion = datetime.timedelta(seconds=i)
        cmd = "ffmpeg -ss " + str(conversion) + " -i " + path + " -vframes 1 -q:v 2 " + prefix + "/" + prefix + str(bigcount) + ".jpg"
        print(cmd)
        os.system(cmd)
        bigcount += 1
        i = i + 8
    return bigcount
    

#"F:\BaiduNetdiskDownload\anime\20150003\[CASO&SumiSora][150003][01][GB][720P].mp4"
i = 1

bc = 0
dd = "kpa"
#episodes = 13

dir = "F:\BaiduNetdiskDownload\\anime\\set3"

for filename in os.listdir(dir):
    if filename.endswith(".mp4"):
        vid = os.path.join(dir, filename)
        vid = '"' + vid + '"'
        #print(vid)
        bc = ffscr(bc, dd, vid)

'''
while i <= episodes:
    pstr = " "
    if i < 10:
        pstr = '"F:\BaiduNetdiskDownload\\anime\\20150003\[CASO&SumiSora][150003][0' + str(i) + '][GB][720P].mp4"'
    else:
        pstr = '"F:\BaiduNetdiskDownload\\anime\\20150003\[CASO&SumiSora][150003][' + str(i) + '][GB][720P].mp4"'
    bc = ffscr(bc, dd, pstr)
    i += 1
'''