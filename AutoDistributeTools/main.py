import wx
 
# from ui.MainFrame import MyFrame1
from UIFrame import UiFrame
 
if __name__ == '__main__':
    app = wx.App()
    frm = UiFrame(None)
    frm.Show()
    app.MainLoop()
 

 # pyinstaller -F -w -i logo.ico --version-file=version.txt -n Setup  main.py