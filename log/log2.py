#-*- coding:utf-8 -*-

"""

#############################################

StaticText 参数说明  --即 label

parent： -- 父窗口部件。

id： -- 标识符。使用-1可以自动创建一个唯一的标识。

label： -- 你想显示在静态控件中的文本。

pos： -- 一个wx.Point或一个Python元组，它是窗口部件的位置。

size： -- 一个wx.Size或一个Python元组，它是窗口部件的尺寸。

style： -- 样式标记。

name： -- 对象的名字，用于查找的需要。

----------------------------------------------

style -- 对齐参数

ALIGN_CENTER， ALIGN_LEFT， ALIGN_RIGHT，

ST_NO_AUTORESIZE： -- 静态文本控件不将自我调整尺寸

#############################################

创建一个字体

wx.Font(pointSize, family, style, weight, underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

family -- 参数说明

wx.DECORATIVE：一个正式的，老的英文样式字体。

wx.DEFAULT：系统默认字体。

wx.MODERN：一个单间隔(固定字符间距)字体。

wx.ROMAN：serif字体，通常类似于Times New Roman。

wx.SCRIPT：手写体或草写体

wx.SWISS：sans-serif字体，通常类似于Helvetica或Arial。

style -- 参数说明 wx.NORMAL, wx.SLANT, wx.ITALIC

weight -- 参数说明 wx.NORMAL, wx.LIGHT, wx.BOLD

#############################################

input与textArea 参数说明

单行样式

wx.TE_CENTER：控件中的文本居中。

wx.TE_LEFT：控件中的文本左对齐。默认行为。

wx.TE_NOHIDESEL：文本始终高亮显示，只适用于Windows。

wx.TE_PASSWORD：不显示所键入的文本，代替以星号显示。

wx.TE_PROCESS_ENTER：如果使用了这个样式，那么当用户在控件内按下回车键时，一个文本输入事件被触发。否则，按键事件内在的由该文本控件或该对话框管理。

wx.TE_PROCESS_TAB：如果指定了这个样式，那么通常的字符事件在Tab键按下时创建(一般意味一个制表符将被插入文本)。否则，tab由对话框来管理，通常是控件间的切换。

wx.TE_READONLY：文本控件为只读，用户不能修改其中的文本。

wx.TE_RIGHT：控件中的文本右对齐。

----------------------------------------------

多单行样式

wx.HSCROLL：如果文本控件是多行的，并且如果该样式被声明了，那么长的行将不会自动换行，并显示水平滚动条。该选项在GTK+中被忽略。

wx.TE_AUTO_URL：如果丰富文本选项被设置并且平台支持的话，那么当用户的鼠标位于文本中的一个URL上或在该URL上敲击时，这个样式将导致一个事件被生成。

wx.TE_DONTWRAP：wx.HSCROLL的别名。

wx.TE_LINEWRAP：对于太长的行，以字符为界换行。某些操作系统可能会忽略该样式。

wx.TE_MULTILINE：文本控件将显示多行。

wx.TE_RICH：用于Windows下，丰富文本控件用作基本的窗口部件。这允许样式文本的使用。

wx.TE_RICH2：用于Windows下，把最新版本的丰富文本控件用作基本的窗口部件。

wx.TE_WORDWRAP：对于太长的行，以单词为界换行。许多操作系统会忽略该样式。

----------------------------------------------

动态修改文本内容

AppendText(text)：在尾部添加文本。

Clear()：重置控件中的文本为“”。并且生成一个文本更新事件。

EmulateKeyPress(event)：产生一个按键事件，插入与事件相关联的控制符，就如同实际的按键发生了。

GetInsertionPoint() SetInsertionPoint(pos) SetInsertionPointEnd()：得到或设置插入点的位置，位置是整型的索引值。控件的开始位置是0。

GetRange(from, to)：返回控件中位置索引范围内的字符串。

GetSelection() GetStringSelection() SetSelection(from, to)：

GetSelection()以元组的形式返回当前所选择的文本的起始位置的索引值(开始，结束)。

GetStringSelection()得到所选择的字符串。

SetSelection(from, to)设置选择的文本。

GetValue() SetValue(value)：SetValue()改变控件中的全部文本。GetValue()返回控件中所有的字符串。

Remove(from, to)：删除指定范围的文本。

Replace(from, to, value)：用给定的值替换掉指定范围内的文本。这可以改变文本的长度。

WriteText(text)：类似于AppendText()，只是写入的文本被放置在当前的插入点。

"""

__author__ = 'pc'

import wx


class StaticTextFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, -1, u'这是Static Text Example', size=(400, 300))
        box_sizer = wx.WrapSizer()
        self.SetAutoLayout(True)
        self.SetSizer(box_sizer)

        ########## Label ##########

        static_text = wx.StaticText(self, -1, u'这是个Label', style=wx.ALIGN_CENTER)
        static_text.SetForegroundColour('red')  #颜色
        wx_font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        static_text.SetFont(wx_font)
        box_sizer.Add(static_text)

        ########## 单行文本框 ##########

        input_text = wx.TextCtrl(self, -1, u'input', size=(175, -1))
        input_text.SetInsertionPoint(0)
        box_sizer.Add(input_text)

        ########## 多行文本框 ##########

        self.area_text = wx.TextCtrl(self, -1, u'textArea多行文本，可Ctrl+A', size=(200, 100),
        style=(wx.TE_MULTILINE | wx.TE_DONTWRAP))
        self.area_text.SetInsertionPoint(0)
        self.area_text.Bind(wx.EVT_KEY_UP, self.OnSelectAll)
        box_sizer.Add(self.area_text)

        ########## 富文本框 ##########

        self.rich_text = wx.TextCtrl(self, -1, u'rich富文本', size=(200, 100),
        style=(wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH2))
        self.rich_text.SetInsertionPoint(0)

        #设置文本样式  len(rich_text.GetValue())

        f = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.BOLD, True)  #创建一个字体
        self.rich_text.SetStyle(0, self.rich_text.GetLastPosition(), wx.TextAttr("red", "green", f))
        box_sizer.Add(self.rich_text)

    #自定义 多行文本框  全选

    def OnSelectAll(self, event):

        if (event.GetKeyCode() == 65 and event.ControlDown()):

            self.area_text.SelectAll()

if __name__ == '__main__':

    root = wx.App()
    frame = StaticTextFrame()
    frame.Show()
    root.MainLoop()