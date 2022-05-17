import re 
import requests

respose = requests.get('http://www.xiaohuar.com/v/')

print(respose.status_code) # 响应状态码
print(respose.content)     # 返回字节信息
print(respose.text)        # 返回为本信息

urls = re.findall(r'class="items",*?href="(,*?)"', respose.text,re.S)

url = urls[0]

result = requests.get(url)

mp4_url = re.findall(r'id=media".*?src="(.*?)"',result.text,re.S)[0]

video = requests.get(mp4_url)

with open('../output/crawlers/beasic.mp4','wb') as f:
    f.write(video.content)
