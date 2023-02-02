#coding:utf-8
 
import wx
import os
  
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (700,500))
		
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
		
      hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
 
      self.t3 = wx.TextCtrl(panel,size = (600,1000),style = wx.TE_MULTILINE) 
		
      hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      vbox.Add(hbox3) 
      self.t3.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)  
      self.t3.SetBackgroundColour('Black'), self.t3.SetForegroundColour('Steel Blue')	
      self.SetTransparent(200) #设置透明
      panel.SetSizer(vbox) 
        
      self.Centre() 
      self.Show() 
      self.Fit()  
		
   def OnKeyTyped(self, event): 
      print(event.GetString()) 
   
   def OnEnterPressed(self,event): 
      self.t3.AppendText(event.GetString())
      result = os.popen(event.GetString())
      res = result.read()
      for line in res.splitlines():
          print(line)
          self.t3.AppendText(line)
      
		
   def OnMaxLen(self,event): 
      print("Maximum length reached")
		
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = Mywin(None, title='MyCmd')
    frm.Show()
    app.MainLoop()
 