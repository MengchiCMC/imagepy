# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 03:57:53 2016
@author: yxl
"""
import threading, wx, os, wx.lib.agw.aui as aui
from imagepy import IPy, root_dir
from ..manager import WidgetsManager

class Widget():
	def __init__(self, panel):
		self.pan = panel
		self.title = panel.title

	def __call__(self):return self

	def start(self):
		#if not WidgetsManager.getref(self.title) is None: return
		pan = self.pan(IPy.curapp)
		#WidgetsManager.addref(pan)
		IPy.curapp.auimgr.AddPane(pan, aui.AuiPaneInfo().Caption(self.title).Left().Layer( 15 ).PinButton( True )
			.Float().Resizable().FloatingSize( wx.DefaultSize ).Dockable(IPy.uimode()=='ipy').DestroyOnClose())

		IPy.curapp.Layout()
		IPy.curapp.auimgr.Update()
		'''
		frame = wx.Frame(IPy.curapp)
		frame.SetTitle(self.title)
		logopath = os.path.join(root_dir, 'data/logo.ico')
		frame.SetIcon(wx.Icon(logopath, wx.BITMAP_TYPE_ICO))
		self.pan(frame)
		frame.Fit()
		frame.Show()
		'''
