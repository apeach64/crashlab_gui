#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Int32

from tkinter import *
import PIL
from PIL import Image, ImageTk
import time

global pwd
#window
#pwd = "C:/Users/Lee/anaconda3/envs/crashlab/Scripts/image/"
#ubuntu
pwd = "/home/jihwa/catkin_ws/src/crashlab_gui/image/"

class eye_ui(Tk):
	
	def __init__(self):
		super().__init__()
		self.geometry("900x550")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)

		#ros
		rospy.init_node('eyes_gui', anonymous=True)

	def BackGroundSetting(self, bgname):
		self.backGroundImage=PhotoImage(file=pwd+bgname+"1.png")
		self.backGroundImageLabel1=Label(self, image=self.backGroundImage)
		self.backGroundImage=PhotoImage(file=pwd+bgname+"2.png")
		self.backGroundImageLabel2=Label(self, image=self.backGroundImage)
		self.backGroundImage=PhotoImage(file=pwd+bgname+"3.png")
		self.backGroundImageLabel3=Label(self, image=self.backGroundImage)
		self.backGroundImage=PhotoImage(file=pwd+bgname+"4.png")
		self.backGroundImageLabel4=Label(self, image=self.backGroundImage)
		eye_ui.BackGround1()
		
	def BackGround1(self):
		try:
			self.backGroundImageLabel4.place_forget()
		self.backGroundImageLabel1.place(x=0, y=0)

		if self.mode == self.mode_new:
			eye_ui.after(500, eye_ui.BackGround2)
		else:
			eye_ui.main()
		
	def BackGround2(self):
		self.backGroundImageLabel1.place_forget()
		self.backGroundImageLabel2.place(x=0, y=0)

		if self.mode == self.mode_new:
			eye_ui.after(500, eye_ui.BackGround3)
		else:
			eye_ui.main()

	def BackGround3(self):
		self.backGroundImageLabel2.place_forget()
		self.backGroundImageLabel3.place(x=0, y=0)

		if self.mode == self.mode_new:
			eye_ui.after(500, eye_ui.BackGround4)
		else:
			eye_ui.main()

	def BackGround4(self):
		self.backGroundImageLabel3.place_forget()
		self.backGroundImageLabel4.place(x=0, y=0)

		if self.mode == self.mode_new:
			eye_ui.after(500, eye_ui.BackGround1)
		else:
			eye_ui.main()


	def main(self):
		if self.mode == 0:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(happy)
		elif self.mode ==1:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(sad)
		elif self.mode ==2:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(heart)
		else:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(twinker)
cd

		eye_ui.mainloop()

if __name__ == "__main__":
	eye_ui = eye_ui()
	eye_ui.main()
