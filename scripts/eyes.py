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
		self.mode_new = "BLINK"
		self.direction = 0 

		#ros
		rospy.init_node('cat_eyes', anonymous=True)


	def BackGroundSetting(self, bgname):

		src=Image.open(pwd+bgname+"/"+bgname+"1.PNG")
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage1=ImageTk.PhotoImage(src)
		self.backGroundImageLabel1=Label(self, image=self.backGroundImage1)

		src=Image.open(pwd+bgname+"/"+bgname+"2.PNG")
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage2=ImageTk.PhotoImage(src)
		self.backGroundImageLabel2=Label(self, image=self.backGroundImage2)

		src=Image.open(pwd+bgname+"/"+bgname+"3.PNG")
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage3=ImageTk.PhotoImage(src)
		self.backGroundImageLabel3=Label(self, image=self.backGroundImage3)

		src=Image.open(pwd+bgname+"/"+bgname+"4.PNG")
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage4=ImageTk.PhotoImage(src)
		self.backGroundImageLabel4=Label(self, image=self.backGroundImage4)

		src=Image.open(pwd+bgname+"/"+bgname+"5.PNG")
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage5=ImageTk.PhotoImage(src)
		self.backGroundImageLabel5=Label(self, image=self.backGroundImage5)

		src=Image.open(pwd+bgname+"/"+bgname+"6.PNG")
		src=src.resize((800, 480), Image.ANTIALIAS)
		self.backGroundImage6=ImageTk.PhotoImage(src)
		self.backGroundImageLabel6=Label(self, image=self.backGroundImage6)
		"""
		self.backGroundImageLabel1.place(x=0, y=0)
		self.backGroundImageLabel2.place(x=0, y=0)
		self.backGroundImageLabel3.place(x=0, y=0)
		self.backGroundImageLabel4.place(x=0, y=0)
		self.backGroundImageLabel5.place(x=0, y=0)
		self.backGroundImageLabel6.place(x=0, y=0)
		

		self.backGroundImageLabel1.place_forget()
		self.backGroundImageLabel2.place_forget()
		self.backGroundImageLabel3.place_forget()
		self.backGroundImageLabel4.place_forget()
		self.backGroundImageLabel5.place_forget()
		self.backGroundImageLabel6.place_forget()
		"""

	def BackGround1(self):
		#print(str(self.mode) + "page1")
		try:
			self.backGroundImageLabel2.place_forget()
		except:
			pass
		
		self.backGroundImageLabel1.place(x=0, y=0)
		
		if self.mode == self.mode_new:

			eye_ui.after(1000, eye_ui.BackGround2)
			
			if self.direction == 1:
				self.direction = 0	
		else:
			eye_ui.main()
		
	def BackGround2(self):
		#print(str(self.mode)+ "page2")

		if self.direction == 0:
			self.backGroundImageLabel1.place_forget()
		else : 
			self.backGroundImageLabel3.place_forget()

		self.backGroundImageLabel2.place(x=0, y=0)

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround3)
			else : 
				eye_ui.after(100, eye_ui.BackGround1)
		else:
			eye_ui.main()

	def BackGround3(self):
		#print(str(self.mode) + "page3")

		if self.direction == 0:
			self.backGroundImageLabel2.place_forget()
		else : 
			self.backGroundImageLabel4.place_forget()

		self.backGroundImageLabel3.place(x=0, y=0)

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround4)
			else : 
				eye_ui.after(100, eye_ui.BackGround2)
		else:
			eye_ui.main()

	def BackGround4(self):
		#print(str(self.mode) + "page4")

		if self.direction == 0:
			self.backGroundImageLabel3.place_forget()
		else : 
			self.backGroundImageLabel5.place_forget()

		self.backGroundImageLabel4.place(x=0, y=0)

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround5)
			else : 
				eye_ui.after(100, eye_ui.BackGround3)
		else:
			eye_ui.main()

	def BackGround5(self):
		#print(str(self.mode)+ "page5")

		if self.direction == 0:
			self.backGroundImageLabel4.place_forget()
		else : 
			self.backGroundImageLabel6.place_forget()

		self.backGroundImageLabel5.place(x=0, y=0)

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround6)
			else : 
				eye_ui.after(100, eye_ui.BackGround4)
		else:
			eye_ui.main()

	def BackGround6(self):
		#print(str(self.mode) + "page6")
		self.backGroundImageLabel5.place_forget()
		self.backGroundImageLabel6.place(x=0, y=0)

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(1000, eye_ui.BackGround5)
				self.direction = 1
		else:
			eye_ui.main()

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
		

	def main(self):
		print(self.mode_new + "main")

		self.mode = self.mode_new

		eye_ui.BackGroundSetting(self.mode)
		eye_ui.BackGround1()

		

if __name__ == "__main__":

	eye_ui = eye_ui()
	rospy.Subscriber('gui_mode', Int32, eye_ui.callback)

	eye_ui.main()
	eye_ui.mainloop()
	
	
