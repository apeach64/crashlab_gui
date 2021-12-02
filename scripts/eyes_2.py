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
		self.geometry("800x480")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)

		self.ui_page = 0
		self.dir = 0
		self.mode_new = "BLINK"

		#ros
		rospy.init_node('cat_eyes', anonymous=True)




	def BackGroundSetting(self, filename):
		src=Image.open(filename)
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage=ImageTk.PhotoImage(src)
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)		



	def callback(self, msg):
		print(msg.data)
		
		ui_page = int(msg.data)
		
		if ui_page == 1 or ui_page == 9 :
			self.mode_new = "LR"
		elif ui_page == 22:
			self.mode_new = "SAD"
		elif ui_page == 6:
			self.mode_new = "SMILE"
		elif ui_page == 4 or ui_page == 72 or ui_page == 76:
			self.mode_new = "LOVE"
		elif ui_page == 73 or ui_page == 75 or ui_page == 8:
			self.mode_new = "TWINK"
		else:
			self.mode_new = "BLINK"

		print(self.mode_new + "/" + self.mode)


	def filename_change1(self):

		filename = pwd+self.mode+"/"+self.mode+"1.PNG"
		eye_ui.BackGroundSetting(filename)


		if self.mode == self.mode_new:
			if self.dir == 1:
				self.dir = 0
			eye_ui.after(500, eye_ui.filename_change2)
		else:
			eye_ui.main()

	def filename_change2(self):

		filename = pwd+self.mode+"/"+self.mode+"2.PNG"
		eye_ui.BackGroundSetting(filename)

		if self.mode == self.mode_new:
			if self.dir == 1:
				eye_ui.after(300, eye_ui.filename_change1)
			else:
				eye_ui.after(300, eye_ui.filename_change3)
		else:
			eye_ui.main()
			
	def filename_change3(self):

		filename = pwd+self.mode+"/"+self.mode+"3.PNG"
		eye_ui.BackGroundSetting(filename)

		if self.mode == self.mode_new:
			if self.dir == 1:
				eye_ui.after(300, eye_ui.filename_change2)
			else:
				eye_ui.after(300, eye_ui.filename_change4)
		else:
			eye_ui.main()

	def filename_change4(self):

		filename = pwd+self.mode+"/"+self.mode+"4.PNG"
		eye_ui.BackGroundSetting(filename)

		if self.mode == self.mode_new:
			if self.dir == 1:
				eye_ui.after(300, eye_ui.filename_change3)
			else:
				eye_ui.after(300, eye_ui.filename_change5)
		else:
			eye_ui.main()

	def filename_change5(self):

		filename = pwd+self.mode+"/"+self.mode+"5.PNG"
		eye_ui.BackGroundSetting(filename)

		if self.mode == self.mode_new:
			if self.dir == 1:
				eye_ui.after(300, eye_ui.filename_change4)
			else:
				eye_ui.after(300, eye_ui.filename_change6)
		else:
			eye_ui.main()

	def filename_change6(self):

		filename = pwd+self.mode+"/"+self.mode+"6.PNG"
		eye_ui.BackGroundSetting(filename)

		if self.mode == self.mode_new:
			if self.dir == 0:
				self.dir = 1
			eye_ui.after(500, eye_ui.filename_change5)
			
		else:
			eye_ui.main()

			

	def main(self):
		print(self.mode_new + "main")

		self.mode = self.mode_new
		self.dir = 0
		eye_ui.filename_change1()
		

if __name__ == "__main__":

	eye_ui = eye_ui()
	rospy.Subscriber('gui_mode', Int32, eye_ui.callback)

	eye_ui.main()
	eye_ui.mainloop()
	
	
