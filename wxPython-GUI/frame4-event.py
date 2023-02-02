import wx

class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""
    
    def __init__(self, parent):
        """构造函数"""
        
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE)
        
        self.SetTitle('事件和事件函数的绑定')
        self.SetIcon(wx.Icon('res/logo.ico'))
        self.SetBackgroundColour((224, 224, 224)) # 设置窗口背景色
        self.SetSize((520, 220))
        
        self._init_ui() 
        self.Center()
    
    def _init_ui(self):
        """初始化界面"""
        
        wx.StaticText(self, -1, '第一行输入框：', pos=(40, 50), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, '第二行输入框：', pos=(40, 80), size=(100, -1), style=wx.ALIGN_RIGHT)
        self.tip = wx.StaticText(self, -1, u'', pos=(145, 110), size=(150, -1), style=wx.ST_NO_AUTORESIZE)
        
        self.tc1 = wx.TextCtrl(self, -1, '', pos=(145, 50), size=(150, -1), name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, -1, '', pos=(145, 80), size=(150, -1), name='TC02', style=wx.TE_PASSWORD|wx.ALIGN_RIGHT)
        
        btn_mea = wx.Button(self, -1, '鼠标左键事件', pos=(350, 50), size=(100, 25))
        btn_meb = wx.Button(self, -1, '鼠标所有事件', pos=(350, 80), size=(100, 25))
        btn_close = wx.Button(self, -1, '关闭窗口', pos=(350, 110), size=(100, 25))
        
        self.tc1.Bind(wx.EVT_TEXT, self.on_text) # 绑定文本内容改变事件
        self.tc2.Bind(wx.EVT_TEXT, self.on_text) # 绑定文本内容改变事件
        
        btn_close.Bind(wx.EVT_BUTTON, self.on_close, btn_close) # 绑定按键事件
        btn_close.Bind(wx.EVT_MOUSEWHEEL, self.on_wheel) # 绑定鼠标滚轮事件
        
        btn_mea.Bind(wx.EVT_LEFT_DOWN, self.on_left_down) # 绑定鼠标左键按下
        btn_mea.Bind(wx.EVT_LEFT_UP, self.on_left_up) # 绑定鼠标左键弹起
        btn_meb.Bind(wx.EVT_MOUSE_EVENTS, self.on_mouse) # 绑定所有鼠标事件
        
        self.Bind(wx.EVT_CLOSE, self.on_close) # 绑定窗口关闭事件
        self.Bind(wx.EVT_SIZE, self.on_size) # 绑定改变窗口大小事件
        self.Bind(wx.EVT_KEY_DOWN, self.on_key_down) # 绑定键盘事件
        
    def on_text(self, evt):
        """输入框事件函数"""
        
        obj = evt.GetEventObject()
        objName = obj.GetName()
        text = evt.GetString()
        
        if objName == 'TC01':
            self.tc2.SetValue(text)
        elif objName == 'TC02':
            self.tc1.SetValue(text)
    
    def on_size(self, evt):
        '''改变窗口大小事件函数'''
        
        print('你想改变窗口，但是事件被Skip了，所以没有任何改变')
        evt.Skip() # 注释掉此行（事件继续传递），窗口大小才会被改变
    
    def on_close(self, evt):
        """关闭窗口事件函数"""
        
        dlg = wx.MessageDialog(None, '确定要关闭本窗口？', '操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if(dlg.ShowModal() == wx.ID_YES):
            self.Destroy()
    
    def on_left_down(self, evt):
        """左键按下事件函数"""
        
        self.tip.SetLabel('左键按下')
    
    def on_left_up(self, evt):
        """左键弹起事件函数"""
        
        self.tip.SetLabel('左键弹起')
    
    def on_wheel(self, evt):
        """鼠标滚轮事件函数"""
        
        vector = evt.GetWheelRotation()
        self.tip.SetLabel(str(vector))
    
    def on_mouse(self, evt):
        """鼠标事件函数"""
        
        self.tip.SetLabel(str(evt.EventType))
    
    def on_key_down(self, evt):
        """键盘事件函数"""
        
        key = evt.GetKeyCode() 
        self.tip.SetLabel(str(key))

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()