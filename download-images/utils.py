# 去除字符串首尾空格
import os
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

"""
'https://img.xxx.com/passimg/llt/TGOD/软妹子徐微微/01.jpg'

return :
('https://img.xxx.com/passimg/llt/TGOD/软妹子徐微微', '01', '.jpg')
"""
def get_filePath_fileName_fileExt(fileUrl):
    """
    获取文件路径， 文件名， 后缀名
    :param fileUrl:
    :return:
    """
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension
