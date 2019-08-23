import re
import os

with open('result.txt', 'r') as file:
    data = file.read().replace('\n', '')

ids = re.findall('(?:av)[0-9]+', data)
print ids
for i in range(len(ids)):
	print "*" * 30
	url = "https://www.bilibili.com/video/" + ids[i]
	shell_script =  "you-get '"+url+"' -o downloads"
	os.system(shell_script)
