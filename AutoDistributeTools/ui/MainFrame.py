# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"自动分发程序", pos = wx.DefaultPosition, size = wx.Size( 522,342 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

		root = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"发件人邮箱", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( 1 )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"408270653@qq.com", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"邮箱授权码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( 1 )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"nimdvxdtsbvhbgbd", wx.DefaultPosition, wx.Size( 193,-1 ), 0 )
		self.m_textCtrl2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer1, 1, wx.ALL|wx.EXPAND|wx.SHAPED, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"验证邮箱", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		root.Add( bSizer3, 1, wx.EXPAND|wx.SHAPED, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a Excel file", u"*.xlsx*", wx.DefaultPosition, wx.Size( 500,-1 ), wx.FLP_DEFAULT_STYLE )
		self.m_filePicker1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_filePicker1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.m_filePicker1.SetToolTip( u"选择Excel文件" )

		bSizer1.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"绩效表Sheet名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer2.Add( self.m_staticText5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"绩效表", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"表头行数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"工资表Sheet名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer2.Add( self.m_staticText6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"工资表", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"表头行数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"邮件标题", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer4.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 440,-1 ), 0 )
		fgSizer4.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"开始分发", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer1.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 500,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer1.Add( self.m_gauge1, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		root.Add( bSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( root )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnVerifyEmailEvent )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnStartDistributeEvent )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnVerifyEmailEvent( self, event ):
		event.Skip()

	def OnStartDistributeEvent( self, event ):
		event.Skip()


