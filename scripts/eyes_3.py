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

		self.star  = time.time()


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

		self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.bg_images[self.num])


	def BackGround(self):
		self.canvas.itemconfig(self.image_on_canvas, image=self.bg_images[self.num])
		print(self.count, "before", self.dir, self.num)

		
		if self.mode == self.mode_new:
			if self.dir == 0:
				self.num += 1

				if self.num == 6:
					self.dir = 1
					self.num -= 2
			else :
				self.num -= 1

				if self.num == -1:
					self.dir = 0
					self.num += 2

		else:
			eye_ui.start()

		print(self.count, "after ", self.dir, self.num)
		self.count +=1

		if self.dir == 0 and self.num == 1:
			eye_ui.after(2000, eye_ui.BackGround)
			self.now = time.time()- self.star
			self.star += self.now
			print(self.now)
		elif self.dir == 1 and self.num ==4:	
			eye_ui.after(2000, eye_ui.BackGround)
			self.now = time.time()- self.star
			self.star += self.now
			print(self.now)
		else:
			eye_ui.after(200, eye_ui.BackGround)
			self.now = time.time()- self.star
			self.star += self.now
			print(self.now)

		
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
		print(self.mode+ "/" + self.mode_new)
		

	def start(self):
		print(self.mode_new + "start")

		self.mode = self.mode_new

		eye_ui.BackGroundSetting(self.mode)
		eye_ui.BackGround()


if __name__ == "__main__":

	eye_ui = eye_ui()
	rospy.Subscriber('gui_mode', Int32, eye_ui.callback)

	eye_ui.start()
	eye_ui.mainloop()
	
	
