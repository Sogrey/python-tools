import numpy as np
import matplotlib
from matplotlib.backends import backend_wxagg   
from matplotlib.figure import Figure   
import wx

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['FangSong']
matplotlib.rcParams['axes.unicode_minus'] = False

class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""
    
    def __init__(self, parent):
        """构造函数"""
        
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE)
        
        self.SetTitle('集成Matplotlib')
        self.SetIcon(wx.Icon('res/logo.ico'))
        self.SetBackgroundColour((224, 224, 224)) # 设置窗口背景色
        self.SetSize((800, 600))
        
        self._init_ui() 
        self.Center()
    
    def _init_ui(self):
        """初始化界面"""
        
        self.fig = Figure()
        self.canvas = backend_wxagg.FigureCanvasWxAgg(self, -1, self.fig)
        
        btn_1 = wx.Button(self, -1, '散点图', size=(80, 30))
        btn_2 = wx.Button(self, -1, '等值线图', size=(80, 30))
        
        btn_1.Bind(wx.EVT_BUTTON, self.on_scatter)
        btn_2.Bind(wx.EVT_BUTTON, self.on_contour)
        
        sizer_btn = wx.BoxSizer()
        sizer_btn.Add(btn_1, 0, wx.RIGHT, 20)
        sizer_btn.Add(btn_2, 0, wx.LEFT, 20)
        
        sizer_max = wx.BoxSizer(wx.VERTICAL)
        sizer_max.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 10)
        sizer_max.Add(sizer_btn, 0, wx. ALIGN_CENTER | wx.BOTTOM, 20)
        
        self.SetSizer(sizer_max)
        self.Layout()
    
    def on_scatter(self, evt):
        """散点图"""
        
        x = np.random.randn(50) # 随机生成50个符合标准正态分布的点（x坐标）
        y = np.random.randn(50) # 随机生成50个符合标准正态分布的点（y坐标）
        color = 10 * np.random.rand(50) # 随即数，用于映射颜色
        area = np.square(30*np.random.rand(50)) # 随机数表示点的面积
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.scatter(x, y, c=color, s=area, cmap='hsv', marker='o', edgecolor='r', alpha=0.5)
        self.canvas.draw()
    
    def on_contour(self, evt):
        """等值线图"""
        
        y, x = np.mgrid[-3:3:60j, -4:4:80j]
        z = (1-y**5+x**5)*np.exp(-x**2-y**2)
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_title('有填充的等值线图')
        c = ax.contourf(x, y, z, levels=8, cmap='jet')
        self.fig.colorbar(c, ax=ax)
        self.canvas.draw()

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()