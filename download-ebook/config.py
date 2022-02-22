Host = r'([http|https]+://[^\s]*[.com|.cn|.la|.net|.biz]/)'
OutputDir = 'books'


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


BaseConfig = {
    'menuList': '#list a',  # 章节目录css选择器
    'menuUrlIsFull': False,  # 目录页各章节url是否是全路径，不是则按照根域名相对路径
    'bookName': '',  # 留空时 小说名从 meta 标签获取 <meta property="og:novel:book_name" content="天命王侯"> ，否则 在此天上 小说名的 css 选择器
    'chapterTile': '.bookname h1',  # 章节页章节标题
    'chapterContent': '#content',  # 章节页章节内容
    'ads': [], # 过滤广告
}

Config = {
    'http://www.biquge001.com/': Merge(BaseConfig, {'ads': [
        '笔趣阁',
        'www.biquge001.com',
        '已启用最新域名：www.',        
        'biquge001',
        '.com ，请大家牢记最新域名并相互转告，谢谢！',
        '笔趣阁 最新永久域名：',
        ' ，请大家牢记本域名并相互转告，谢谢！',
        'www.399xs.com',
    ]}),
    'https://www.xbiquge.la/': Merge(BaseConfig, {'ads': [
        '亲,点击进去,给个好评呗,分数越高更新越快,据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦!', '手机站全新改版升级地址：https://wap.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！',
    ]}),
    'http://www.ibiqu.net/': BaseConfig,
    'https://www.biquge.biz/': BaseConfig,
    'https://www.biqugee.com/': BaseConfig,
    'https://biquge96.com/': {
        'menuList': '.mb20 .info-chapters a',
        'menuUrlIsFull': False,
        'bookName': '',
        'chapterTile': '.reader-main h1',
        'chapterContent': '#article',
        'ads': [],
    },
    'http://www.26ksw.cc/': {
        'menuList': '#list a',
        'menuUrlIsFull': False,
        'bookName': '',
        'chapterTile': '.bookname h1',
        'chapterContent': '#content',
        'ads': ['天才一秒记住本站地址：\\[爱豆看书\\]', 'http://www.26ksw.cc/最快更新！无广告！', '首发网址htTp://m.26w.ｃc'],
    },
    'http://www.b5200.net/': {
        'menuList': '#list a',
        'menuUrlIsFull': True,
        'bookName': '',
        'chapterTile': '.bookname h1',
        'chapterContent': '#content',
        'ads': [],
    },
    'https://www.bige7.com/': {
        'menuList': '.listmain a',
        'menuUrlIsFull': False,
        'bookName': '',
        'chapterTile': '.content h1',
        'chapterContent': '#chaptercontent',
        'ads': [],
    },
    'http://www.soduso.cc/': {
        'menuList': '.ml_list a',
        'menuUrlIsFull': False,
        'bookName': '.introduce h1',  # 小说名css选择器
        'chapterTile': '.nr_title h3',
        'chapterContent': '#articlecontent',
        'ads': ['搜读小说http://ｍ.soｄuso.ｃc'],
    },
    'http://www.399xs.com/':{
        'menuList': '.list a',
        'menuUrlIsFull': False,
        'bookName': '.info h2',  # 小说名css选择器
        'chapterTile': '.bookname h1',
        'chapterContent': '.centent',
        'ads': [
            '笔趣阁 最新永久域名：',
            '笔趣阁',
            'www.biquge001.com',
            '已启用最新域名：www.',        
            'biquge001',
            '.com ，请大家牢记最新域名并相互转告，谢谢！',
            ' ，请大家牢记本域名并相互转告，谢谢！',
            'www.399xs.com',
            '最新永久域名：'
        ],
    },
    'https://www.yousheng8.com/':{
        'menuList': '.listmain a',
        'menuUrlIsFull': False,
        'bookName': '#maininfo #info h1',  # 小说名css选择器
        'chapterTile': '#book .content h1',
        'chapterContent': 'div#content.showtxt',
        'ads': [],
    },
}

# print(Config['http://www.biquge001.com/'])
# print(Config['https://www.biqugee.com/'])
# print(len(Config['http://www.26ksw.cc/']['ads']))
