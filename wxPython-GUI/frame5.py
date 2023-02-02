import wx

class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""
    
    id_open = wx.NewIdRef()
    id_save = wx.NewIdRef()
    id_quit = wx.NewIdRef()
    
    id_help = wx.NewIdRef()
    id_about = wx.NewIdRef()
    
    def __init__(self, parent):
        """构造函数"""
        
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE)
        
        self.SetTitle('菜单、工具栏、状态栏')
        self.SetIcon(wx.Icon('res/logo.ico'))
        self.SetBackgroundColour((224, 224, 224)) # 设置窗口背景色
        self.SetSize((360, 180))
        
        self._create_menubar()      # 菜单栏
        self._create_toolbar()      # 工具栏
        self._create_statusbar()    # 状态栏
        
        self.Center()
    
    def _create_menubar(self):
        """创建菜单栏"""
        
        self.mb = wx.MenuBar()
        
        # 文件菜单
        m = wx.Menu()
        m.Append(self.id_open, '打开文件')
        m.Append(self.id_save, '保存文件')
        m.AppendSeparator()
        m.Append(self.id_quit, '退出系统')
        self.mb.Append(m, '文件')
        
        self.Bind(wx.EVT_MENU, self.on_open, id=self.id_open)
        self.Bind(wx.EVT_MENU, self.on_save, id=self.id_save)
        self.Bind(wx.EVT_MENU, self.on_quit, id=self.id_quit)
        
        # 帮助菜单
        m = wx.Menu()
        m.Append(self.id_help, '帮助主题')
        m.Append(self.id_about, '关于...')
        self.mb.Append(m, '帮助')
        
        self.Bind(wx.EVT_MENU, self.on_help,id=self.id_help)
        self.Bind(wx.EVT_MENU, self.on_about,id=self.id_about)
        
        self.SetMenuBar(self.mb)
    
    def _create_toolbar(self):
        """创建工具栏"""

        pass
        
        # bmp_open = wx.Bitmap('res/open_mso.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        # bmp_save = wx.Bitmap('res/save_mso.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        # bmp_help = wx.Bitmap('res/help_mso.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        # bmp_about = wx.Bitmap('res/info_mso.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        
        # self.tb = wx.ToolBar(self)
        # self.tb.SetToolBitmapSize((16,16))
        
        # self.tb.AddTool(self.id_open, '打开文件', bmp_open, shortHelp='打开', kind=wx.ITEM_NORMAL)
        # self.tb.AddTool(self.id_save, '保存文件', bmp_save, shortHelp='保存', kind=wx.ITEM_NORMAL)
        # self.tb.AddSeparator()
        # self.tb.AddTool(self.id_help, '帮助', bmp_help, shortHelp='帮助', kind=wx.ITEM_NORMAL)
        # self.tb.AddTool(self.id_about, '关于', bmp_about, shortHelp='关于', kind=wx.ITEM_NORMAL)
        
        # self.tb.Realize()
    
    def _create_statusbar(self):
        """创建状态栏"""
        
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-2, -1, -1])
        self.sb.SetStatusStyles([wx.SB_RAISED, wx.SB_RAISED, wx.SB_RAISED])
        
        self.sb.SetStatusText('状态信息0', 0)
        self.sb.SetStatusText('', 1)
        self.sb.SetStatusText('状态信息2', 2)
    
    def on_open(self, evt):
        """打开文件"""
        
        self.sb.SetStatusText(u'打开文件', 1)
    
    def on_save(self, evt):
        """保存文件"""
        
        self.sb.SetStatusText(u'保存文件', 1)
    
    def on_quit(self, evt):
        """退出系统"""
        
        self.sb.SetStatusText(u'退出系统', 1)
        self.Destroy()
    
    def on_help(self, evt):
        """帮助"""
        
        self.sb.SetStatusText(u'帮助', 1)
    
    def on_about(self, evt):
        """关于"""
        
        self.sb.SetStatusText(u'关于', 1)

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()