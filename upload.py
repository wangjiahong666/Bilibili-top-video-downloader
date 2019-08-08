# coding:utf-8

import re
import os


path = './'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.mp4' in file:
            files.append(os.path.join(r, file))

uploaded_videos = open("uploaded_videos.txt","a")


for f in files[5:7]:
    #print(f)
    #print(type(f))

    title = f.replace('./downloads/', '').replace('.mp4', '')
    #print title


    tags = "B站, Bilibili"
    #print("Shepherd {} is years old.".format(tags))

    upload_script = 'youtube-upload --title="#B站 #Bilibili {}" --tags="{}" --description="{} #B站 #Bilibili" {}'.format(title, tags, title, f)
    print(upload_script)
    print
    print
    print("{}.mp4".format(title))
    #os.system("'{}.mp4' >> uploaded_videos.txt".format(title))

    os.system(upload_script)

    uploaded_videos.write(title + "\n")
uploaded_videos.close()
