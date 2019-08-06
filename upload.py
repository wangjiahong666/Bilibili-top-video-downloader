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

for f in files[:1]:
    #print(f)
    #print(type(f))

    title = f.replace('./downloads/', '').replace('.mp4', '')
    #print title


    tags = "B站, Bilibili"
    #print("Shepherd {} is years old.".format(tags))

    upload_script = 'youtube-upload --title="{}" --tags="{}" --description="{} #B站 #Bilibili" {}'.format(title, tags, title, f)
    print(upload_script)
    print
    print
    os.system(upload_script)
