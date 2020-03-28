import re
import os


# f7 is the function remove the duplicates of list, but perserve the order of items
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


# Get video id
with open('view-source_https___search.bilibili.com_all_keyword=动物之森&order=click&duration=1&tids_1=0.html', 'r') as file:
    data = file.read().replace('\n', '')
    print(data)
ids = re.findall('(?:video/)[0-9a-zA-Z]+', data)
print(ids)
ids = f7(ids)

# Get titles and write to file
titles = re.findall('"title">(.*?)</', data)
titles = f7(titles)
print (titles)
with open('Video_titles.txt', 'w') as f:
    for item in titles:
        f.write("%s\n" % item)



# to do： check the space of device is still large enough


#动物之森 #动物森友会 #任天堂 #switch #游戏 #2020游戏 #动森
"""
动物之森,动物森友会,任天堂,switch,游戏,2020游戏,动森
"""
# Download videos
for i in range(len(ids)): #
	print ("{} th vodeo, processing and downloading...".format(i))
	print ("*" * 30)
	url = "https://www.bilibili.com/" + ids[i]
	all_downloaded_files_txt = '-'.join(os.listdir('./downloads'))

	print ("   " + url)
	try:
		print ("   " + titles[i])
	except: 
		pass

	shell_script =  "you-get '"+ url +"' -o animal_crossing_downloads"
	os.system(shell_script)
	print ("downloaded!")
	print ("\n\n")

print ("we get {} videos and {} titles.".format(len(ids), len(titles)))
print ("Cheers, Completed !!!!!")



