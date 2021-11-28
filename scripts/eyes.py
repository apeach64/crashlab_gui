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
pwd = "/home/jihwa/catkin_ws/src/crashlab_gui/image/BLINK/"
#pwd = "/home/jihwa/catkin_ws/src/crashlab_gui/image/"

class eye_ui(Tk):
	
	def __init__(self):
		super().__init__()
		self.geometry("1210x760")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)

		self.mode = 0
		self.mode_new = 0
		self.direction = 0 

		#ros
		rospy.init_node('eyes_gui', anonymous=True)


	def BackGroundSetting(self, bgname):

		src=Image.open(pwd+bgname+"1.png")
		src=src.resize((1210, 760), Image.ANTIALIAS)
		self.backGroundImage1=ImageTk.PhotoImage(src)
		self.backGroundImageLabel1=Label(self, image=self.backGroundImage1)

		src=Image.open(pwd+bgname+"2.png")
		src=src.resize((1210, 760), Image.ANTIALIAS)
		self.backGroundImage2=ImageTk.PhotoImage(src)
		self.backGroundImageLabel2=Label(self, image=self.backGroundImage2)

		src=Image.open(pwd+bgname+"3.png")
		src=src.resize((1210, 760), Image.ANTIALIAS)
		self.backGroundImage3=ImageTk.PhotoImage(src)
		self.backGroundImageLabel3=Label(self, image=self.backGroundImage3)

		src=Image.open(pwd+bgname+"4.png")
		src=src.resize((1210, 760), Image.ANTIALIAS)
		self.backGroundImage4=ImageTk.PhotoImage(src)
		self.backGroundImageLabel4=Label(self, image=self.backGroundImage4)

		src=Image.open(pwd+bgname+"5.png")
		src=src.resize((1210, 760), Image.ANTIALIAS)
		self.backGroundImage5=ImageTk.PhotoImage(src)
		self.backGroundImageLabel5=Label(self, image=self.backGroundImage5)

		src=Image.open(pwd+bgname+"6.png")
		src=src.resize((1210, 760), Image.ANTIALIAS)
		self.backGroundImage6=ImageTk.PhotoImage(src)
		self.backGroundImageLabel6=Label(self, image=self.backGroundImage6)



	def BackGround1(self):
		print(str(self.mode) + "page1")
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
		print(str(self.mode)+ "page2")

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
		print(str(self.mode) + "page3")

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
		print(str(self.mode) + "page4")

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
		print(str(self.mode)+ "page5")

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
		print(str(self.mode) + "page6")
		self.backGroundImageLabel5.place_forget()
		self.backGroundImageLabel6.place(x=0, y=0)

		if self.mode == self.mode_new:
			if self.direction ==0:
				eye_ui.after(100, eye_ui.BackGround5)
				self.direction = 1
		else:
			eye_ui.main()



	def main(self):
		print(str(self.mode) + "main")
		if self.mode == 0:
			self.mode = self.mode_new
			print("in")
			eye_ui.BackGroundSetting("blink")
			eye_ui.BackGround1()
		elif self.mode ==1:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(sad)
		elif self.mode ==2:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(heart)
		else:
			self.mode = self.mode_new
			eye_ui.BackGroundSetting(twinker)

		

if __name__ == "__main__":

	eye_ui = eye_ui()
	eye_ui.main()
	eye_ui.mainloop()
	
	
