import wx
import time
import threading

class MainFrame(wx.Frame):
    """桌面程序主窗口类"""
    
    def __init__(self):
        """构造函数"""
        
        wx.Frame.__init__(self, parent=None, style=wx.CAPTION|wx.SYSTEM_MENU|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SIMPLE_BORDER)
        
        self.SetTitle('定时器和线程')
        self.SetIcon(wx.Icon('res/logo.ico', wx.BITMAP_TYPE_ICO))
        self.SetBackgroundColour((224, 224, 224))
        self.SetSize((320, 300))
        
        self._init_ui()
        self.Center()
    
    def _init_ui(self):
        """初始化界面"""
        
        font = wx.Font(30, wx.DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, 'Monaco')
        
        self.clock = wx.StaticText(self, -1, '08:00:00', pos=(50,50), size=(200,50), style=wx.TE_CENTER|wx.SUNKEN_BORDER)
        self.clock.SetForegroundColour(wx.Colour(0, 224, 32))
        self.clock.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.clock.SetFont(font)
        
        self.stopwatch = wx.StaticText(self, -1, '0:00:00.00', pos=(50,150), size=(200,50), style=wx.TE_CENTER|wx.SUNKEN_BORDER)
        self.stopwatch.SetForegroundColour(wx.Colour(0, 224, 32))
        self.stopwatch.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.stopwatch.SetFont(font)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(50)
        
        self.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        
        self.sec_last = None
        self.is_start = False
        self.t_start = None
        
        thread_sw = threading.Thread(target=self.StopWatchThread)
        thread_sw.setDaemon(True)
        thread_sw.start()
        
    def on_timer(self, evt):
        """定时器函数"""
        
        t = time.localtime()
        if t.tm_sec != self.sec_last:
            self.clock.SetLabel('%02d:%02d:%02d'%(t.tm_hour, t.tm_min, t.tm_sec))
            self.sec_last = t.tm_sec
        
    def on_key_down(self, evt):
        """键盘事件函数"""
        
        if evt.GetKeyCode() == wx.WXK_SPACE:
            self.is_start = not self.is_start
            self.t_start= time.time()
        elif evt.GetKeyCode() == wx.WXK_ESCAPE:
            self.is_start = False
            self.stopwatch.SetLabel('0:00:00.00')
        
    def StopWatchThread(self):
        """线程函数"""
        
        while True:
            if self.is_start:
                t = time.time() - self.t_start
                ti = int(t)
                wx.CallAfter(self.stopwatch.SetLabel, '%d:%02d:%02d.%.02d'%(ti//3600, ti//60, ti%60, int((t-ti)*100)))
            time.sleep(0.02)

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()