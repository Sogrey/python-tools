OutputDir = 'output\\download-images\\'

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


BaseConfig = {
    'menuList': '#list a',  # 章节目录css选择器
    'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
    'title':'title',
    'imageContent':'.content img',
    'imgUrlAttr':'src'
}

Config = {
    'https://mp.weixin.qq.com/':{
        'menuList': '#list a',  # 章节目录css选择器
        'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
        'title':'#activity-name',
        'imageContent':'#js_content img',
        'imgUrlAttr':'data-src'
    },
    'https://www.xxx.com/':{
        'menuList':'.list ul li a', # 目录css选择器
        'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
        'title':'title',
        'imageContent':'.content img.videopic',
        'imgUrlAttr':'data-original'
    }
}
