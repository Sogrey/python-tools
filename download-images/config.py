OutputDir = 'output\\download-images\\'

regular_metaCharset = [
        r'meta http-equiv="Content-type" content="text/html;charset=(.*)"',
        r'meta http-equiv="content-type" content="text/html;charset=(.*)"',
        r'meta http-equiv="content-Type" content="text/html; charset=(.*)"',
        r'meta http-equiv="Content-Type" content="text/html; charset=(.*)"',
        r'meta charset="(.*)"'
    ]

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
    'https://www.xxxxx.com/':{
        'menuList':'.list ul li a', # 目录css选择器
        'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
        'title':'title',
        'imageContent':'.content img.videopic',
        'imgUrlAttr':'data-original'
    },
    'http://www.yyyyy.xyz/':{
        'menuList':'.classList ul li a', # 目录css选择器
        'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
        'title':'.contentList h1.content',
        'imageContent':'.contentList div.content img',
        'imgUrlAttr':'src'
    }
}
