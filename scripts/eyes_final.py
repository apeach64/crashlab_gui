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
		self.canvas = Canvas(self, width = 800, height = 480)
		self.canvas.grid(row=0, column=0)

		self.ui_page = 0
		self.mode_new = "BLINK"
		self.direction = 0 


		#ros
		rospy.init_node('cat_eyes', anonymous=True)


	def BackGroundSetting(self, bgname):

		self.bg_images = []
		self.dir = 0
		self.num = 0

		self.count = 0

		for i in range(1,7):
			src=Image.open(pwd+bgname+"/"+bgname+str(i)+".PNG")
			src=src.resize((800, 480), Image.ANTIALIAS)
			self.bg_images.append(ImageTk.PhotoImage(src))

		self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.bg_images[1])

	def BackGround1(self):
		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[0])
		
		if self.mode == self.mode_new:

			eye_ui.after(1000, eye_ui.BackGround2)
			
			if self.direction == 1:
				self.direction = 0	
		else:
			eye_ui.main()
		
	def BackGround2(self):

		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[1])

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround3)
			else : 
				eye_ui.after(100, eye_ui.BackGround1)
		else:
			eye_ui.main()

	def BackGround3(self):

		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[2])
		
		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround4)
			else : 
				eye_ui.after(100, eye_ui.BackGround2)
		else:
			eye_ui.main()

	def BackGround4(self):
		
		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[3])

		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround5)
			else : 
				eye_ui.after(100, eye_ui.BackGround3)
		else:
			eye_ui.main()

	def BackGround5(self):

		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[4])
		
		if self.mode == self.mode_new:
			if self.direction == 0:
				eye_ui.after(100, eye_ui.BackGround6)
			else : 
				eye_ui.after(100, eye_ui.BackGround4)
		else:
			eye_ui.main()

	def BackGround6(self):
		
		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[5])

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
	
	
