#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import argparse
import requests
from bs4 import BeautifulSoup
import os
import re  # 正则
import urllib.parse

version = '1.0'

# 根据URL获取文件名
# 文件路径或web地址


def getFileNameFromUrl(url):
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    return filename


# 下载一张图片
# url ： 图片文本地址
# path ： 图片本地存储路径，不包括文件名
def get_pictures(url, path):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
    re = requests.get(url, headers=headers)
    # print(re.status_code)  # 查看请求状态，返回200说明正常
    print(re.status_code, "下载", url)  # 查看请求状态，返回200说明正常

    filePath = path+'/'+getFileNameFromUrl(url)
    if (not os.path.exists(path)):
        os.makedirs(path)

    with open(filePath, 'wb') as f:  # 把图片数据写入本地，wb表示二进制储存
        for chunk in re.iter_content(chunk_size=128):
            f.write(chunk)


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
    global_directory = 'download'  # 存放子目录

    # if (args.file != None): #
    #     global_markdownFile = args.file
    if (args.directory != None): # 指定下载目录
        global_directory = args.directory

    # print(global_markdownFile)
    print(global_directory)

    # markdown图片匹配       \!\[.*\]\(.+\)                 匹配结果如： ![描述](地址)
    # markdown图片链接提取   (?<=\!\[.*\]\()(.+)(?=\))       只匹配图片链接部分

    markdown_text = ''
    with open('markdown.md', 'r', encoding="utf-8") as file:
        markdown_text = file.read()

    ret = re.findall(r'(?=\!\[.*\]\()(.+)(?=\))', markdown_text)
    if (len(ret) > 0):

        for i in range(0, len(ret)):
            # ](  之前移除掉
            index = ret[i].index('](')
            filePath = ret[i][index+2:]
            # print(filePath)
            # 下载图片
            get_pictures(filePath, global_directory)


if __name__ == "__main__":
    main()
