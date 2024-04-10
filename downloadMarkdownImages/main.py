#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import os
import re  # 正则
import shutil
import urllib.parse

import requests
from bs4 import BeautifulSoup

version = '1.0'


def is_contained(string, substring):
    return string.find(substring) != -1

# 根据URL获取文件名
# 文件路径或web地址


def getFileNameFromUrl(url):
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)

    suffix = "jpg"
    if (is_contained(filename, ".")):
        suffix = filename.split(".")[1]  # 取后缀名

    if (is_contained(filename, ":")):
        if (filename.index(":") > 0):
            print("注意：文件名中存在特殊字符 ':'")
            filename = filename[:filename.index(":")]

    if (suffix == 'awebp'):
        filename = os.path.splitext(filename)[0]+'.webp'
    else:
        filename = os.path.splitext(filename)[0]+'.'+suffix

    return filename


# 下载一张图片
# url ： 图片文本地址
# path ： 图片本地存储路径，不包括文件名
def get_pictures(url, path):
    if (url.startswith('data:image/')):  # base64图片 和 svg不用下载
        return
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
    if (url.startswith('//')):  # 补全协议头
        url = 'http:'+url

    re = requests.get(url, headers=headers)
    # print(re.status_code)  # 查看请求状态，返回200说明正常
    print(re.status_code, "下载", url)  # 查看请求状态，返回200说明正常

    filePath = path+'/'+getFileNameFromUrl(url)
    if (not os.path.exists(path)):
        os.makedirs(path)

    with open(filePath, 'wb') as f:  # 把图片数据写入本地，wb表示二进制储存
        for chunk in re.iter_content(chunk_size=128):
            f.write(chunk)

    return filePath


def parserParams():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="Show the current version.",
                        action="store_true")

    parser.add_argument("-f", "--file", help="The markdown file.")

    parser.add_argument("-d", "--directory", help="Image storage directory.")
    args = parser.parse_args()
    if args.version:
        print("The current version is v%s" % (version))
        return True

    return args


def main():
    args = parserParams()
    if args == True:
        return

    # global_markdownFile = ''
    # global_path = './'  # 文件储存根目录
    global_directory = './download'  # 存放子目录

    if (os.path.exists(global_directory)):
        shutil.rmtree(global_directory)

    # if (args.file != None): #
    #     global_markdownFile = args.file
    if (args.directory != None):  # 指定下载目录
        global_directory = args.directory

    # print(global_markdownFile)
    print(global_directory)

    # markdown图片匹配       \!\[.*\]\(.+\)                 匹配结果如： ![描述](地址)
    # markdown图片链接提取   (?<=\!\[.*\]\()(.+)(?=\))       只匹配图片链接部分

    # 知乎安全外链   https\:\/\/link\.zhihu\.com\/\?target=.*\)  https://link.zhihu.com/?target=xxx

    markdown_text = ''
    with open('markdown.md', 'r', encoding="utf-8") as file:
        markdown_text = file.read()

    retZhihuTarge = re.findall(
        r'https\:\/\/link\.zhihu\.com\/\?target=.*\)', markdown_text)
    retJianshuTarge = re.findall(
        r'https\:\/\/links\.jianshu\.com\/go\?to=.*\)', markdown_text)
    retJuejinTarge = re.findall(
        r'https\:\/\/link\.juejin\.cn\/\?target=.*\)', markdown_text)
    if (len(retZhihuTarge) > 0):
        for i in range(0, len(retZhihuTarge)):
            urlNew = retZhihuTarge[i][:-1]
            # print(urlNew)
            zhihuTargeUrl = urlNew
            urlNew = urlNew[len('https://link.zhihu.com/?target='):]

            if (is_contained(urlNew, " ")):
                if (urlNew.index(' ') > -1):
                    urlNew = urlNew[:urlNew.index(' ')]

            zhihuTargeUrl = 'https://link.zhihu.com/?target='+urlNew
            # print(urlNew)
            urlNew = urllib.parse.unquote(urlNew)
            # print(urlNew)

            # 替换字符，字符串直接调用replace方法
            markdown_text = markdown_text.replace(zhihuTargeUrl, urlNew)

    if (len(retJianshuTarge) > 0):
        for i in range(0, len(retJianshuTarge)):
            urlNew = retJianshuTarge[i][:-1]
            # print(urlNew)
            jianshuTargeUrl = urlNew
            urlNew = urlNew[len('https://links.jianshu.com/go?to='):]

            if (is_contained(urlNew, " ")):
                if (urlNew.index(' ') > -1):
                    urlNew = urlNew[:urlNew.index(' ')]

            jianshuTargeUrl = 'https://links.jianshu.com/go?to='+urlNew
            # print(urlNew)
            urlNew = urllib.parse.unquote(urlNew)
            # print(urlNew)

            # 替换字符，字符串直接调用replace方法
            markdown_text = markdown_text.replace(jianshuTargeUrl, urlNew)

    if (len(retJuejinTarge) > 0):
        for i in range(0, len(retJuejinTarge)):
            urlNew = retJuejinTarge[i][:-1]
            # print(urlNew)
            urlNew = urlNew[len('https://link.juejin.cn/?target='):]

            if (urlNew.index(' ') > -1):
                urlNew = urlNew[:urlNew.index(' ')]

            juejinTargeUrl = 'https://link.juejin.cn/?target='+urlNew
            # print(urlNew)
            urlNew = urllib.parse.unquote(urlNew)
            # print(urlNew)

            # 替换字符，字符串直接调用replace方法
            markdown_text = markdown_text.replace(juejinTargeUrl, urlNew)

    ret = re.findall(r'(?=\!\[.*\]\()(.+)(?=\))', markdown_text)
    if (len(ret) > 0):

        for i in range(0, len(ret)):
            # ](  之前移除掉
            index = ret[i].index('](')
            filePath = ret[i][index+2:]
            # print(filePath)
            # 下载图片
            newPath = get_pictures(filePath, global_directory)

            if (newPath != None):
                # 替换字符，字符串直接调用replace方法
                markdown_text = markdown_text.replace(filePath, newPath)

    with open('markdown.md', 'w', encoding="utf-8") as file:
        file.write(markdown_text)


if __name__ == "__main__":
    main()
