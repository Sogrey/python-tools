from fileinput import filename
import re
from unittest import result
import requests
import hashlib
import time


def get_index(url):
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.text


def parse_index(res):
    urls = re.findall(r'class="item".*?href="(.*?)"',
                      res, re.S)  # re.S 把文本信息转为一行匹配
    return urls


def get_detail(urls):
    for url in urls:
        if not url.startswith('http'):
            url = 'http://www.xiaohuar.com%s' % url

        result = requests.get(url)
        if result.status_code == 200:
            mp4_url_list = re.findall(
                r'id="media".?src="(.*?)"', result.text, re.S)
            if mp4_url_list:
                mp4_url = mp4_url_list[0]
                print(mp4_url)
                # save(mp4_url)


def save(url):
    video = requests.get(url)
    if video.status_code == 200:
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        m.update(str(time.time()).encode('utf-8'))
        filename = r'%s.mp4' % m.hexdigest()
        filepath = r'd:\\%s' % filename
        with open(filepath, 'wb') as f:
            f.write(video.content)


def main():
    for i in range(5):
        res1 = get_index('http://www.xiaohuar.com/list-3-%s.html' % i)
        res2 = parse_index(res1)
        get_detail(res2)


if __name__ == '__main__':
    main()
