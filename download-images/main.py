import urllib.request
import sys
import re
import os
import urllib
import multiprocessing
import requests
from bs4 import BeautifulSoup

from config import Config, OutputDir
from utils import getWebHost, removeN, trim

def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')

def get_img(html):
    atlasName = ''
    reg = r'https://[^\s]*?\.jpg'
    imgre = re.compile(reg)  # 转换成一个正则对象
    imglist = imgre.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    x = 0        # 声明一个变量赋值
    this_output =  OutputDir+atlasName  # 设置图片的保存地址
    if not os.path.isdir(this_output):
        os.makedirs(this_output)  # 判断没有此路径则创建
    paths = this_output + '\\'  # 保存在test路径下
    for imgurl in imglist:
        imgFileName = '{0}{1}.jpg'.format(paths, x)
        urllib.request.urlretrieve(imgurl, imgFileName)  # 打开imgList,下载图片到本地
        x = x+1
    #     print(imgFileName)
    #     print('图片开始下载，注意查看文件夹')
    # return imglist



def thread_getOneHtml(url, encoding):
    # html_b = get_html(url)  # 获取该网页的详细信息
    # print(html_b.title())
    # print(get_img(html_b))  # 从网页源代码中分析下载保存图片

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res = requests.get(url, headers=headers)  # get方法中加入请求头

    if(encoding.isspace()):
        res.encoding = requests.get(url).encoding
    else:
        res.encoding = encoding

    html = res.text

    soup = BeautifulSoup(html, 'html.parser')  # 对返回的结果进行解析

    # 先检查下网页编码
    # <meta http-equiv="Content-Type" content="text/html; charset=gbk">
    # <meta charset="utf-8">

    rmetaCharset = [
        r'meta http-equiv="Content-Type" content="text/html; charset=(.*)"',
        r'meta charset="(.*)"'
    ]

    encoding1 = 'gbk'
    for r in rmetaCharset:
        regular = re.compile(r)
        encodingContent = re.findall(regular, html)
        if(encodingContent != None and len(encodingContent) > 0):
            encoding1 = encodingContent[0]
            break

    if(encoding1 != encoding):
        thread_getOneHtml(url, encoding1)
        return

    print('页面地址： ' + url)
    print("原址编码：%s" % (encoding))

    baseUrl = getWebHost(url)
    if(baseUrl.strip() == ''):
        print('未正确匹配出根域名地址')
        return

    # print(baseUrl)
    titleCss = Config[baseUrl]['title']
    title = soup.select(titleCss)[0].get_text()
    title = title.strip()

    imageContentCss = Config[baseUrl]['imageContent']
    imgList = soup.select(imageContentCss)

    title += "(" + str(len(imgList)) + "p)"
    print('正在下载 《%s》' % (title))

    imgUrlAttrCss = Config[baseUrl]['imgUrlAttr']

    index = 0        # 声明一个变量赋值
    this_output =  OutputDir+title  # 设置图片的保存地址
    if not os.path.isdir(this_output):
        os.makedirs(this_output)  # 判断没有此路径则创建
    paths = this_output + '\\'  # 保存在test路径下
    for img in imgList:
        imgFileName = '{0}{1}.jpg'.format(paths, index)

        imgurl = img[imgUrlAttrCss]
        print(imgurl)
        urllib.request.urlretrieve(imgurl, imgFileName)  # 打开imgList,下载图片到本地
        index = index+1
 
def process_getImages(urls):
    # 输入你要下载的书的首页地址
    print('主程序的PID：%s' % os.getpid())

    print("-------------------开始下载-------------------")
    p = []
    for i in urls:
        p.append(multiprocessing.Process(
            target=thread_getOneHtml, args=(i, 'utf-8')))
    print("等待所有的主进程加载完成........")
    for i in p:
        i.start()
    for i in p:
        i.join()
    print("-------------------全部下载完成-------------------")

    return

def process_getGroupList(url,encoding):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res = requests.get(url, headers=headers)  # get方法中加入请求头

    if(encoding.isspace()):
        res.encoding = requests.get(url).encoding
    else:
        res.encoding = encoding

    html = res.text

    soup = BeautifulSoup(html, 'html.parser')  # 对返回的结果进行解析

    # 先检查下网页编码
    # <meta http-equiv="Content-Type" content="text/html; charset=gbk">
    # <meta charset="utf-8">

    rmetaCharset = [
        r'meta http-equiv="Content-Type" content="text/html; charset=(.*)"',
        r'meta charset="(.*)"'
    ]

    encoding1 = 'gbk'
    for r in rmetaCharset:
        regular = re.compile(r)
        encodingContent = re.findall(regular, html)
        if(encodingContent != None and len(encodingContent) > 0):
            encoding1 = encodingContent[0]
            break

    if(encoding1 != encoding):
        process_getGroupList(url, encoding1)
        return

    print('列表地址： ' + url)
    print("原址编码：%s" % (encoding))

    baseUrl = getWebHost(url)
    if(baseUrl.strip() == ''):
        print('未正确匹配出根域名地址')
        return

    # print(baseUrl)

    imageGroupListCss = Config[baseUrl]['menuList']
    imgGrpList = soup.select(imageGroupListCss)

    imgGrps = []
    for imgGrp in imgGrpList:
        imgGrpUrl = imgGrp['href']        
        print(imgGrpUrl)
        imgGrps.append(imgGrpUrl)

    # 创建下载这本书的进程
    p = multiprocessing.Pool()
    for i in imgGrps:
        url = i
        if(False == Config[baseUrl]['menuUrlIsFull']):  # 目录url是相对于根域名
            baseUrl1 = baseUrl
            if (baseUrl.endswith('/') and i.startswith('/')):
                baseUrl1 = baseUrl.rstrip('/')
            url = baseUrl1+i
        else:  # 目录url是全路径
            url = i

        p.apply_async(thread_getOneHtml, args=(url, encoding))

    p.close()
    p.join()
    return

group = 'https://www.xxx.com/tupian/list-2.html'

urls = [
    # 'https://www.xxx.com/tupian/126069.html',
    'https://www.xxx.com/tupian/126068.html',
]

if __name__ == "__main__":

    argvNum = len(sys.argv)
    if(argvNum >= 2):  # 参数1是本文件名 参数2为小说目录页地址
        print('参数个数为:', argvNum, '个参数。')
        print('参数列表:', str(sys.argv))

        urls = [
            sys.argv[1]
        ]

    # 下载指定的书
   
    process_getGroupList(group,'utf-8')
    # process_getImages(urls)  # 如果下载完出现卡的话，请单独执行如下命令
