使用Python解析m3u8文件需要使用m3u8库，它是一个用于解析和写入m3u8文件的Python库。

安装：
```
pip install m3u8
```
使用：
``` python
import m3u8

# 解析m3u8文件
m3u8_obj = m3u8.load('example.m3u8')

# 获取播放列表
playlist = m3u8_obj.data['playlists']

# 获取播放列表中的每个视频
for video in playlist:
    print(video['uri'])
```

----

python 解析和下载m3u8视频



使用Python解析和下载m3u8视频，需要安装ffmpeg库。

1. 安装ffmpeg库：

使用pip安装ffmpeg库：

```
pip install ffmpeg
```

2. 使用Python解析m3u8文件：

使用Python的requests库获取m3u8文件：

```
import requests

url = 'http://example.com/video.m3u8'
r = requests.get(url)
m3u8_content = r.text
```

然后使用正则表达式解析m3u8文件：

```
import re

ts_urls = re.findall(r'(http.*?\.ts)', m3u8_content)
```

3. 使用ffmpeg下载ts文件：

使用ffmpeg下载ts文件：

```
import subprocess

for ts_url in ts_urls:
    subprocess.call(['ffmpeg', '-i', ts_url, '-c', 'copy', 'video.ts'])
```

4. 合并ts文件：

使用ffmpeg合并ts文件：

```
subprocess.call(['ffmpeg', '-i', 'concat:video1.ts|video2.ts|video3.ts', '-c', 'copy', 'video.mp4'])
```
