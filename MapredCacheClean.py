#-*-coding:UTF-8 -*-
import os
import time

local_dir = ["/opt/data/hadoop/mapred/mrlocal","/opt/data/hadoop1/mapred/mrlocal","/opt/data/hadoop2/mapred/mrlocal",\
             "/opt/data/hadoop3/mapred/mrlocal","/opt/data/hadoop4/mapred/mrlocal"]

def Clean(path,tolerable_time):
    clean_dir = []
    real_path = path + '/taskTracker'
    clean_dir.append(real_path + "/distcache")
    for f in os.listdir(real_path):
        if f != "distcache":
            clean_dir.append(real_path + '/' + f + "/distcache")
            
    for c_dir in clean_dir:
        for f in os.listdir(c_dir):
            last_mtime = os.stat("%s/%s" % (c_dir,f)).st_mtime
            if last_mtime < tolerable_time:
                print c_dir,f
                os.system("rm -rf %s/%s" % (c_dir,f))
                
if __name__=="__main__":
    cur_time = int(time.time())
    tolerable_time = cur_time - 3*24*3600
    for path in local_dir:
        try:
            Clean(path,tolerable_time)
        except:
            continue
