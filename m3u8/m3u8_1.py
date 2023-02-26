import m3u8

# 解析m3u8文件
m3u8_obj = m3u8.load('test/index.m3u8')

# 获取播放列表
playlist = m3u8_obj.data['playlists']

# 获取播放列表中的每个视频
for video in playlist:
    print(video['uri'])