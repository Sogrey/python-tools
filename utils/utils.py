# 去除字符串首尾空格
import re


def trim(s):
    flag = 0
    if s[:1] == ' ':
        s = s[1:]
        flag = 1
    if s[-1:] == ' ':
        s = s[:-1]
        flag = 1
    if flag == 1:
        return trim(s)
    else:
        return s
# print(trim('  Hello world!  '))
# Hello world!

def removeN(s):
    return s.replace("\n", "")

def getWebHost(url):
    webHostProtocol = 'http://'
    if(url.startswith('http://')):
        webHostProtocol = 'http://'
    elif(url.startswith('https://')):
        webHostProtocol = 'https://'
    url1 = re.sub(r'%s' % (webHostProtocol), '', url)
    # print(url1)
    # print(url1.find('/'))

    return r'%s%s' % (webHostProtocol, url1[0:url1.find('/')+1])

# print(getWebHost('http://www.soduso.cc/novel/57634/'))
# http://www.soduso.cc/


def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
    
# BaseConfig = {
#     'menuList': '#list a',  # 章节目录css选择器
#     'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
#     'bookName': '',  # 留空时 小说名从 meta 标签获取 <meta property="og:novel:book_name" content="天命王侯"> ，否则 在此天上 小说名的 css 选择器
#     'chapterTile': '.bookname h1',  # 章节页章节标题
#     'chapterContent': '#content',  # 章节页章节内容
#     'ads': [],
# }

# print(Merge(BaseConfig,{'ads': ['aaaaa']}))

