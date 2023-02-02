import wx

class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""
    
    def __init__(self, parent):
        """构造函数"""
        
        wx.Frame.__init__(self, parent, -1,style=wx.DEFAULT_FRAME_STYLE)
        
        self.SetTitle('最简的的应用程序')
        self.SetIcon(wx.Icon('logo.ico')) # 设置图标
        self.SetBackgroundColour((217, 228, 0)) # 设置窗口背景色
        self.SetSize((300, 80)) # 设置窗口大小
        self.Center() # 窗口在屏幕上居中
        
        st = wx.StaticText(self, -1, 'Hello World', style=wx.ALIGN_CENTER) # 生成静态文本控件，水平居中
        st.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Arial')) # 设置字体字号

if __name__ == '__main__':
    app = wx.App() # 创建一个应用程序
    frame = MainFrame(None) # 创建主窗口
    frame.Show() # 显示窗主口
    app.MainLoop() # 应用程序进入事件处理主循环