https://www.jb51.net/article/206578.htm

本文实例为大家分享了python实现控制台输出颜色的具体代码，供大家参考，具体内容如下

python控制台输出颜色，out()是基本方法，还封装了一些基本颜色方法，如red()，blue()，green()等  
out()方法的color参数表示颜色，bgcolor表示背景颜色，style表示样式  
其他方法的参数类似，三个参数的具体取值封装到Color类，BGColor类，Style类中。

**基本方法：**

``` python
out(content, color=Color.DEFAULT, bgcolor=BGColor.DEFAULT, style=Style.DEFAULT)

red (content [, bgcolor, [style]])
green (content [, bgcolor, [style]])
blue (content [, bgcolor, [style]])
yellow (content [, bgcolor, [style]])
bold (content [, color, [bgcolor]])
underline (content [, color, [bgcolor]])
italic (content [, color, [bgcolor]])
```

**具体代码：**

``` python
from functools import partial

class Style:
 DEFAULT = 0
 BOLD= 1
 ITALIC = 3
 UNDERLINE = 4
 ANTIWHITE = 7


class Color:
 DEFAULT = 39
 BLACK = 30
 RED = 31
 GREEN = 32
 YELLOW = 33
 BLUE = 34
 PURPLE = 35
 CYAN = 36
 WHITE = 37
 LIGHTBLACK_EX = 90
 LIGHTRED_EX = 91
 LIGHTGREEN_EX = 92
 LIGHTYELLOW_EX = 93
 LIGHTBLUE_EX = 94
 LIGHTMAGENTA_EX = 95
 LIGHTCYAN_EX = 96
 LIGHTWHITE_EX = 97


class BGColor:
 DEFAULT = 49
 BLACK = 40
 RED = 41
 GREEN = 42
 YELLOW = 43
 BLUE = 44
 PURPLE = 45
 CYAN = 46
 WHITE = 47
 LIGHTBLACK_EX = 100
 LIGHTRED_EX = 101
 LIGHTGREEN_EX = 102
 LIGHTYELLOW_EX = 103
 LIGHTBLUE_EX = 104
 LIGHTMAGENTA_EX = 105
 LIGHTCYAN_EX = 106
 LIGHTWHITE_EX = 107


def out(content, color=Color.DEFAULT, bgcolor=BGColor.DEFAULT, style=Style.DEFAULT):
 print("\033[{};{};{}m{}\033[0m".format(style, color, bgcolor, content))


red = partial(out, color=Color.RED)
green = partial(out, color=Color.GREEN)
blue = partial(out, color=Color.BLUE)
yellow = partial(out, color=Color.YELLOW)
bold = partial(out, style=Style.BOLD)
underline = partial(out, style=Style.UNDERLINE)
italic = partial(out, style=Style.ITALIC)
```

红绿灯事件输出颜色示例：

``` python
from multiprocessing import Event, Process
import time
import random

from basicPractice import outputscreen # 这里导入了上面写的模块


def car(event: Event, i: int):
 if not event.is_set():
 outputscreen.out('car{}等待'.format(i),
    bgcolor=outputscreen.BGColor.RED)
 event.wait()
 else:
 outputscreen.out('car{}通行'.format(i),
    bgcolor=outputscreen.BGColor.GREEN)


def light(event: Event):
 while True:
 if not event.is_set():
  outputscreen.red('红灯亮了', style=outputscreen.Style.BOLD)
  time.sleep(1)
  event.set()
 else:
  outputscreen.green('绿灯亮了', style=outputscreen.Style.BOLD)
  time.sleep(3)
  event.clear()


if __name__ == '__main__':
 event = Event()
 p = Process(target=light, args=(event,))
 p.start()
 for i in range(20):
 Process(target=car, args=(event, i)).start()
 time.sleep(random.random())
```

![](https://img.jbzj.com/file_images/article/202103/20213283150852.jpg)


