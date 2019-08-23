# coding:utf-8

import re
import os
import datetime


path = './'
files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.mp4' in file:
            files.append(os.path.join(r, file))

uploaded_videos = open("logs_uploaded_videos.txt","a")


for f in files[11:12]:
    title = f.replace('./downloads/', '').replace('.mp4', '')
    tags = "B站, Bilibili"
    upload_script = 'youtube-upload --title="#B站 #Bilibili {}" --tags="{}" --description="{} #B站 #Bilibili" {}'.format(title, tags, title, f)
    print(upload_script)
    print
    print
    print("{}.mp4".format(title))
    os.system(upload_script)

    # Save the title of uploaded videos to logs files
    datetime_now = str(datetime.datetime.now())
    uploaded_videos.write('{}, {}'.format(datetime_now, title)
    # Remove the uploaded video from local file
    # print('rm ./downloads/{}'.format(title))
    print(123)
    print
    print('removed uploaded video: {}'.format(title))

uploaded_videos.close()
