import wx

class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""
    
    def __init__(self, parent):
        """构造函数"""
        
        # 调用父类的构造函数，从默认风格中去除改变窗口大小
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        
        self.SetTitle('wxPython控件演示')
        self.SetIcon(wx.Icon('res/logo.ico'))
        self.SetSize((860, 450))
        self.Center()
        
        # 创建一个面板，用于放置控件
        panel = wx.Panel(self, -1)

        # 在x=20，y=20的位置，创建静态文本控件
        st = wx.StaticText(panel, -1, '我是静态文本控件', pos=(20, 20))

        # 在x=300，y=20的位置，创建静态图片
        bmp = wx.Bitmap('res/image.jpg')
        sb = wx.StaticBitmap(panel, -1, bmp, pos=(280, 10))

        # 在x=20, y=50的位置，创建文本输入框，指定输入框的宽度为260像素，高度默认
        tc1 = wx.TextCtrl(panel, -1, value='我是文本输入框', pos=(20, 50), size=(260, -1))

        # 在x=20, y=90的位置，创建文本输入框，指定样式为密码
        tc2 = wx.TextCtrl(panel, -1, value='我是密码', pos=(20, 90), style=wx.TE_PASSWORD)

        # 在x=20, y=130的位置，创建单选按钮，成组的单选按钮，第一个需要指定样式wx.RB_GROUP
        rb1 = wx.RadioButton(panel, -1, '单选按钮1', pos=(20, 130), style=wx.RB_GROUP, name='rb1')

        # 在x=100, y=130的位置，创建单选按钮，不再需要指定样式wx.RB_GROUP
        rb2 = wx.RadioButton(panel, -1, '单选按钮2', pos=(100, 130), name='rb2')

        # 在x=180, y=130的位置，创建单选按钮，不再需要指定样式wx.RB_GROUP
        rb3 = wx.RadioButton(panel, -1, '单选按钮3', pos=(180, 130), name='rb3')

        # 在x=20, y=160的位置，创建复选按钮
        cb1 = wx.CheckBox(panel, -1, '复选按钮', pos=(20, 160))

        # 在x=100, y=160的位置，创建复选按钮，指定其样式为wx.ALIGN_RIGHT
        cb2 = wx.CheckBox(panel, -1, '文字在左侧的复选按钮', pos=(100, 160), style=wx.ALIGN_RIGHT)

        # 在x=20，y=190的位置，创建按钮
        ch = wx.Choice(panel, -1, choices=['wxPython', 'PyQt', 'Tkinter'], pos=(20, 190), size=(100, -1))
        ch.SetSelection(0)
        
        # 在x=120，y=190的位置，创建按钮
        btn = wx.Button(panel, -1, '按钮', pos=(150, 190))

        # 在x=20，y=230的位置，创建文本框，指定大小为260*150，并指定其样式为多行和只读
        tc3 = wx.TextCtrl(panel, -1, value='我是多行文本输入框', pos=(20, 230), size=(260, 150), style=wx.TE_MULTILINE | wx.CB_READONLY)

if __name__ == '__main__':
    app = wx.App() # 创建一个应用程序
    frame = MainFrame(None) # 创建主窗口
    frame.Show() # 显示窗主口
    app.MainLoop() # 应用程序进入事件处理主循环