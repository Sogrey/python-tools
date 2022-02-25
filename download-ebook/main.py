
# coding:utf-8
from distutils import archive_util
import sys
import requests
from bs4 import BeautifulSoup
import multiprocessing
import re
import os
import time
from config import Config, Host, OutputDir
from utils import getWebHost, removeN, trim


# 通过章节的url下载内容，并返回下一页的url
def get_ChartTxt(baseUrl, url, title, num, totalNum, encoding):
    # print('本章节地址： ' + url, encoding)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res = requests.get(url, headers=headers)  # get方法中加入请求头
    # 查看下当前requests请求url抓去的数据编码,这里获取的是ISO-8859-1
    # print("原址编码：%s" % (requests.get(url).encoding))
    # 翻阅下要爬去的网站的编码是什么，这里看了下是utf-8，编码不一样会乱码，将requests获取的数据编码改为和目标网站相同，改为utf-8
    # res.encoding = 'utf-8'
    # res.encoding = 'gbk'
    res.encoding = encoding
    soup = BeautifulSoup(res.text, 'html.parser')  # 对返回的结果进行解析

    # 查找章节名
    # <div class="bookname">
    #             <h1>第1章 大康王朝</h1>
    #             ...
    # </div>

    chapterTile = soup.select(Config[baseUrl]['chapterTile'])[0].get_text()
    # [<h1>第1章 大康王朝</h1>]
    chapterTile = chapterTile.strip()

    numLength = len(str(totalNum))
    # # n = "123"
    # # s = n.zfill(5)
    # # assert s == '00123'
    numStr = str(num)
    numStr = numStr.zfill(numLength)

    print('正在下载 (%s/%s) %s %s' % (numStr, totalNum, chapterTile, url))

    # 开始计时
    start = time.time()

    # # 判断是否有感言
    # if re.search(r'.*?章', chapterTile) is None:
    #     return

    chapterTile = re.sub(r'\?', '_', chapterTile)
    chapterTile = re.sub(r'\/', '_', chapterTile)

    # 获取章节文本
    content = soup.select(Config[baseUrl]['chapterContent'])[0].text
    # 按照指定格式替换章节内容，运用正则表达式
    content = re.sub(r'\(.*?\)', '', content)
    content = re.sub(r'\r\n', '\n', content)
    content = re.sub(r'\n+', '\n', content)
    content = re.sub(r'<.*?>+', '\n', content)
    content = re.sub(r'&nbsp;+', ' ', content)

    ads = Config[baseUrl]['ads']
    if(len(ads) > 0):
        for ad in ads:
            content = re.sub(r'%s' % (ad), ' ', content)


    # 单独写入这一章
    try:
        with open(r'.\%s\%s\%s %s.txt' % (OutputDir, title, numStr, chapterTile), 'w', encoding='utf-8') as f:
            # print(content)
            f.write(chapterTile + '\n' + content)
        f.close()

        end = time.time()
        print('下载 %s %s  完成，运行时间  %0.2f s.' % (num, chapterTile, (end - start)))

    except Exception as e:
        print(e)
        print(chapterTile, '下载失败', url)
        errorPath = '.\Error\%s' % (title)
        # 创建错误文件夹
        try:
            os.makedirs(errorPath)
        except Exception as e:
            pass
        # 写入错误文件
        with open("%s\error_url.txt" % (errorPath), 'a', encoding='utf-8') as f:
            f.write(chapterTile+"下载失败 "+url+'\n')
        f.close()

    return

# 章节合并


def mergeFiles(title, encoding):
    dirPath = r".\%s\%s" % (OutputDir, title)  # 所有txt位于的文件夹路径
    files = os.listdir(dirPath)
    res = ""
    encoding = 'utf-8'
    i = 0
    for file in files:
        if file.endswith(".txt"):
            i += 1

            fileName = dirPath + "/" + file
            print(fileName)

            with open(fileName, "r", encoding=encoding) as file:
                content = file.read()
                file.close()

            append = "\n\n%s" % (content)
            res += append

    bookPath = r"%s\\%s.txt" % (dirPath, title)  # 文件路径
    if os.path.exists(bookPath):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(bookPath)
        # os.unlink(path)

    with open(bookPath, "w", encoding=encoding) as outFile:
        outFile.write(res)
        outFile.close()
    print('整书《%s》合并完成，总字数：%d' % (title, len(res)))
    return


# 通过首页获得该小说的所有章节链接后下载这本书
def thread_getOneBook(url, encoding):

    # url = 'http://www.cnplugins.com/'
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
        thread_getOneBook(url, encoding1)
        return

    print('小说首页地址： ' + url)
    print("原址编码：%s" % (encoding))

    # baseUrl = ''
    # try:
    #     # 提取出书的每章节不变的url
    #     regular = re.compile(Host)
    #     baseUrl = re.findall(regular, url)[0]
    # except Exception as e:
    #     baseUrl = getWebHost(url)

    baseUrl = getWebHost(url)
    # print(baseUrl)
    # return

    if(baseUrl.strip() == ''):
        print('未正确匹配出根域名地址')
        return

    bookNameCss = Config[baseUrl]['bookName'].strip()
    if(bookNameCss == ''):
        # 查找小书名
        # <meta property="og:novel:book_name" content="天命王侯">
        # meta property="og:novel:book_name" content="(.*?)"
        title = soup.find(attrs={"property": "og:novel:book_name"})['content']
    else:
        title = soup.select(bookNameCss)[0].get_text()
        title = title.strip()

    print('正在下载 《%s》' % (title))

    # 开始计时
    start = time.time()

    # 根据书名创建文件夹
    if OutputDir not in os.listdir('.'):
        os.mkdir(r".\%s" % (OutputDir))
    if title not in os.listdir(r'.\%s' % (OutputDir)):
        os.mkdir(r".\%s\%s" % (OutputDir, title))
        print(title, "文件夹创建成功")

    # 获取这本书的所有章节
    charts_url = []
    url_chartTitle = dict()

    print('顶级域名：%s' % (baseUrl))

    index = 0

    # print (soup.select('body > section > div.wrapbox > div:nth-child(1) > div > ul > li:nth-child(6)'))
    # nth-child 在python中运行会报错，需改为 nth-of-type
    # print (soup.select('body > section > div.wrapbox > div:nth-of-type(1) > div > ul > li:nth-of-type(6)'))
    # textlist = soup.select('#list a')

    textlist = soup.select(Config[baseUrl]['menuList'])

    for t in textlist:
        # print(type(t))
        # <a href="/book/10258/53450024.html">
        #             第475章 五百人足矣
        #         </a>
        # print (t) #获取单条html信息
        try:
            chart_title = trim(removeN(t.get_text()))
            chart_url = t['href']

            if(chart_url.strip() == ''):
                print('章节url未找到')
                continue

            # # 判断是否有感言
            # if re.findall(r'.*?章', chart_title) is None:
            #     print('抓到作者感言，跳过...')
            #     continue

            url_chartTitle[chart_url] = chart_title

            if chart_url in charts_url:
                charts_url.remove(chart_url)  # 移除之前已有的重复项
                charts_url.append(chart_url)
            else:
                index += 1
                charts_url.append(chart_url)

            # print('%d %s %s' % (index, chart_title, chart_url))  # 获取中间文字信息
        except Exception as e:
            print('[ERROR] ' + str(e))
            continue

    totalNum = len(charts_url)
    print('总共找到 %d 章' % (totalNum))

    # 创建下载这本书的进程
    p = multiprocessing.Pool()
    # 自己在下载的文件前加上编号，防止有的文章有上，中，下三卷导致有3个第一章
    num = 1

    for i in charts_url:

        if(False == Config[baseUrl]['menuUrlIsFull']):  # 目录url是相对于根域名
            baseUrl1 = baseUrl
            if (baseUrl.endswith('/') and i.startswith('/')):
                baseUrl1 = baseUrl.rstrip('/')
            url = baseUrl1+i
        else:  # 目录url是全路径
            url = i

        p.apply_async(get_ChartTxt, args=(
            baseUrl, url, title, num, totalNum, encoding))
        num += 1

        # 测试用
        # if(num >= 10):
        #     break

    print('等待 %s 所有的章节被加载......' % (title))
    p.close()
    p.join()
    end = time.time()
    print('下载 %s  完成，运行时间  %0.2f s.' % (title, (end - start)))
    print('开始生成 %s ................' % title)
    # sort_allCharts(r'.',"%s.txt"%title)

    mergeFiles(title, encoding)

    return

# 创建下载多本书书的进程


def process_getAllBook(urls):
    # 输入你要下载的书的首页地址
    print('主程序的PID：%s' % os.getpid())

    print("-------------------开始下载-------------------")
    p = []
    for i in urls:
        p.append(multiprocessing.Process(
            target=thread_getOneBook, args=(i, 'utf-8')))
    print("等待所有的主进程加载完成........")
    for i in p:
        i.start()
    for i in p:
        i.join()
    print("-------------------全部下载完成-------------------")

    return


urls = [
    # 'http://www.26ksw.cc/book/10258/',
    # 'http://www.biquge001.com/Book/17/17605/',
    # 'http://www.biquge001.com/Book/17/17605/',
    # 'http://www.biquge001.com/Book/8/8460/',
    # 'https://www.xbiquge.la/7/7877/',
    # 'http://www.ibiqu.net/book/7/',
    # 'https://www.biquge.biz/22_22780/',
    # 'https://www.biqugee.com/book/1366/',
    # 'https://www.bige7.com/book/11742/'
    # 'http://www.b5200.net/50_50537/',
    # 'https://biquge96.com/30_30171/',
    # 'http://www.b5200.net/52_52542/',
    # 'https://www.bige7.com/book/2749/',
    # 'http://www.soduso.cc/novel/57634/',
    # 'http://www.soduso.cc/novel/57634/'
    # 'http://www.biquge001.com/Book/2/2321/'
    # 'https://www.xbiquge.la/0/745/'
    # 'http://www.biquge001.com/Book/18/18632/'
    # 'http://www.399xs.com/book/0/611/'
    'https://www.yousheng8.com/yousheng/704/'
]

# 原址编码：gbk" src="https://www.baidu.com/js/opensug.js

if __name__ == "__main__":

    argvNum = len(sys.argv)
    if(argvNum >= 2):  # 参数1是本文件名 参数2为小说目录页地址
        print('参数个数为:', argvNum, '个参数。')
        print('参数列表:', str(sys.argv))

        urls = [
            sys.argv[1]
        ]

    # 下载指定的书
    process_getAllBook(urls)  # 如果下载完出现卡的话，请单独执行如下命令
    # sort_allCharts(r'.\龙血战神',"龙血战神.txt")

    # mergeFiles('明朝败家子', 'gbk')
    # get_ChartTxt('https://biquge96.com/','https://biquge96.com/30_30171/17240253.html', '重生之金融巨头', 1, 1, 'utf-8')
