import re
import requests
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor
p = ThreadPoolExecutor(30)


def get_index(url):
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.text


def parse_index(res):
    res = res.result()
    urls = re.findall(r'class="item".*?href="(.*?)"',
                      res, re.S)  # re.S 把文本信息转为一行匹配
    for url in urls:
        p.submit(get_detail(url))


def get_detail(url):
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
        p.submit(get_index, 'http://www.xiaohuar.com/list-3-%s.html' %
                 i).add_done_callback(parse_index)


if __name__ == '__main__':
    main()
