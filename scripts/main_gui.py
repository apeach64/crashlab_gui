#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Int32

from tkinter import *
import PIL
from PIL import Image, ImageTk
import time
import random

global pwd
#window
#pwd = "C:/Users/Lee/anaconda3/envs/crashlab/Scripts/image/"
#ubuntu
pwd = "/home/jihwa/catkin_ws/src/crashlab_gui/image/"

class main_ui(Tk):
	
	def __init__(self):
		super().__init__()
		self.geometry("1024x600")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)

		#footprint routine
		global i
		i = 21

		#ros GUI_mode
		rospy.init_node('gui', anonymous=True)
		self.pub = rospy.Publisher('gui_mode', Int32, queue_size=10)
		self.mode_num = 1


	def BackGroundSetting(self, bgname):
		src=Image.open(pwd+bgname+".png")
		src=src.resize((1024, 600), Image.ANTIALIAS)
		self.backGroundImage=ImageTk.PhotoImage(src)
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)

		self.pub.publish(main_ui.mode_num)

	def Button1(self):
		src=Image.open(pwd+"button_start_big.png")
		src=src.resize((350, 150), Image.ANTIALIAS)
		self.gobigButtonImage=ImageTk.PhotoImage(src)
		self.gobigButton=Button(self, image=self.gobigButtonImage, command=self.Button1_clk, border=0)
		self.gobigButton.place(x=620, y=420)

	def Button1_clk(self):
		self.mode_num = 2
		main_ui.BackGroundSetting("background2")
		print('page2')
		main_ui.page2_cat_init()


	def page2_cat_init(self):
		#define cat image
		src=Image.open(pwd+"cat_normal.png")
		src=src.resize((120, 120), Image.ANTIALIAS)
		self.catnormalImage=ImageTk.PhotoImage(src)
		self.lab_cat_normal=Label(image =self.catnormalImage, border = 0)

		src=Image.open(pwd+"cat_sad.png")
		src=src.resize((120, 120), Image.ANTIALIAS)
		self.catsadImage=ImageTk.PhotoImage(src)
		self.lab_cat_sad=Label(image =self.catsadImage, border = 0)

		self.cycle =0
		main_ui.page2_cat()

	def page2_cat(self):
		second2 = 6
		second3 = 5
		
		if self.cycle == 0:
			self.mode_num = 21
			self.pub.publish(main_ui.mode_num)

			self.lab_cat_normal.place(x=680, y=500)
			self.cycle += 1

		elif self.cycle == 1:
			self.mode_num = 21
			self.pub.publish(main_ui.mode_num)

			self.lab_cat_normal.place(x=720, y=480)
			self.cycle += 1

		elif self.cycle == 2:
			self.mode_num = 21
			self.pub.publish(main_ui.mode_num)

			self.lab_cat_normal.place(x=770, y=460)
			self.cycle += 1
		
		elif self.cycle == 3:
			self.mode_num = 21
			self.pub.publish(main_ui.mode_num)
			
			self.lab_cat_normal.place(x=810, y=440)
			self.cycle += 1

		elif self.cycle == 4:
			self.mode_num = 22
			self.pub.publish(main_ui.mode_num)

			self.lab_cat_normal.place_forget()
			self.lab_cat_sad.place(x=785, y=450)
			self.cycle += 1

		elif self.cycle == 5:
			self.mode_num = 22
			self.pub.publish(main_ui.mode_num)

			self.lab_cat_sad.place(x=685, y=480)
			self.cycle += 1

		else:
			self.mode_num = 22
			self.pub.publish(main_ui.mode_num)

			self.lab_cat_sad.place(x=830, y=465)
			self.cycle += 1


		if self.cycle < 8:
			main_ui.after(int(second2/7*1000), main_ui.page2_cat)
		
		else:
			self.mode_num = 3

			main_ui.BackGroundSetting("background3")
			print('page3')
			main_ui.after(second3*1000, main_ui.page3)

	def page3(self):
		main_ui.Button3_Y()
		main_ui.Button3_N()

	def Button3_Y(self):
		src=Image.open(pwd+"button_good.png")
		src=src.resize((200, 100), Image.ANTIALIAS)
		self.yesButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_Y=Button(self, image=self.yesButtonImage, command=self.Button3_Y_clk, border=0)
		self.lab_Button_Y.place(x=290, y=450)

	def Button3_Y_clk(self):
		second4 = 5
		self.mode_num = 4

		print('page4')
		main_ui.BackGroundSetting("background4")
		main_ui.after(second4*1000, main_ui.page4)
		

	def Button3_N(self):
		src=Image.open(pwd+"button_busy.png")
		src=src.resize((200, 100), Image.ANTIALIAS)
		self.noButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_N=Button(self, image=self.noButtonImage, command=self.Button3_N_clk, border=0)
		self.lab_Button_N.place(x=530, y=450)

	def Button3_N_clk(self):
		self.mode_num = 1

		print('page1')
		main_ui.BackGroundSetting("background1")
		main_ui.Button1()

	def page4(self):
		main_ui.Button4()

	def Button4(self):
		self.gobigButton=Button(self, image=self.gobigButtonImage, command=self.Button4_clk, border=0)
		self.gobigButton.place(x=600, y=400)

	def Button4_clk(self):
		self.mode_num =5

		main_ui.BackGroundSetting("background5")
		print('page5')
		main_ui.tracking()



	def tracking(self):
		print('tracking')

		#footprint image
		src=Image.open(pwd+"footprint_0.png")
		src=src.resize((50, 50), Image.ANTIALIAS)
		self.footprintImage0=ImageTk.PhotoImage(src)
		src=Image.open(pwd+"footprint_50.png")
		src=src.resize((50, 50), Image.ANTIALIAS)
		self.footprintImage50=ImageTk.PhotoImage(src)
		src=Image.open(pwd+"footprint_80.png")
		src=src.resize((50, 50), Image.ANTIALIAS)
		self.footprintImage80=ImageTk.PhotoImage(src)

		#footprint image label
		self.lab_foot_L0=Label(image =self.footprintImage0, border = 0)
		self.lab_foot_R1=Label(image =self.footprintImage0, border = 0)
		self.lab_foot_L2=Label(image =self.footprintImage50, border = 0)
		self.lab_foot_R3=Label(image =self.footprintImage50, border = 0)
		self.lab_foot_L4=Label(image =self.footprintImage80, border = 0)
		self.lab_foot_R5=Label(image =self.footprintImage80, border = 0)

		main_ui.footprint_choose()

	def callback(self, msg):
		self.rfid = msg.data

	def footprint_choose(self):
		global i
		global max_i
		global fp_finish

		self.rfid = 0
		max_i = 21

		if i == 2:
			main_ui.footprint_reset()

		if i % 2 == 0:
			i -= 1
			main_ui.footprint_L(self.lab_foot_L0)
		else:
			i -= 1
			main_ui.footprint_R(self.lab_foot_R1)

		if self.rfid == 0:
			main_ui.after(500, main_ui.footprint_choose)

		else : 
			self.mode_num = 6

			main_ui.BackGroundSetting("background6")
			print('page6')
			#need to time change 
			main_ui.after(6000, main_ui.cheering_mode)
			

	def footprint_reset(self):
		global i 
		global max_i

		i = max_i

		self.lab_foot_L0.place_forget()
		self.lab_foot_L2.place_forget()
		self.lab_foot_L4.place_forget()
		self.lab_foot_R3.place_forget()
		self.lab_foot_R5.place_forget()

	def footprint_L(self, foot):
		global i
		
		y_foot_L = i*30
		foot.place(x=725, y=y_foot_L)
		if i < max_i-2:
			self.lab_foot_L2.place(x=725, y=y_foot_L+60)
		if i < max_i-4:
			self.lab_foot_L4.place(x=725, y=y_foot_L+120)

		rospy.Subscriber('finish', Int32, main_ui.callback)

	def footprint_R(self, foot):
		global i
		
		y_foot_R = i*30

		foot.place(x=775, y=y_foot_R)

		if i < max_i-2:
			self.lab_foot_R3.place(x=775, y=y_foot_R+60)

		if i < max_i-4:
			self.lab_foot_R5.place(x=775, y=y_foot_R+120)

		rospy.Subscriber('finish', Int32, main_ui.callback)



	def cheering_mode(self):
		cheer_mode = random.randrange(1, 7)
		print("page7")

		if cheer_mode == 1:
			self.mode_num = 71
			main_ui.BackGroundSetting("background7")

		elif cheer_mode == 2:
			self.mode_num = 72
			main_ui.BackGroundSetting("background8")

		elif cheer_mode == 3:
			self.mode_num = 73
			main_ui.BackGroundSetting("background9")

		elif cheer_mode == 4:
			self.mode_num = 74
			main_ui.BackGroundSetting("background10")

		elif cheer_mode == 5:
			self.mode_num = 75
			main_ui.BackGroundSetting("background11")

		else:
			self.mode_num = 76
			main_ui.BackGroundSetting("background12")

		main_ui.after(6000, main_ui.page8)


	def page8(self):
		self.mode_num = 8
		main_ui.BackGroundSetting("background13")
		print("page8")
		main_ui.page8_wait()

	def page8_wait(self):
		if self.rfid == 1:
			rospy.Subscriber('finish', Int32, main_ui.callback)
			main_ui.after(500, main_ui.page8_wait)
		if self.rfid == 2:
			main_ui.BackGroundSetting("background14")
			print("page9")
			main_ui.after(500, main_ui.page9)


	def page9(self):
		self.mode_num = 9
		if self.rfid == 2:
			rospy.Subscriber('finish', Int32, main_ui.callback)
			main_ui.after(500, main_ui.page9)
		if self.rfid == 3:
			main_ui.BackGroundSetting("background1")
			main_ui.Button1()


		


if __name__ == "__main__":
	main_ui = main_ui()
	print("main"+str(main_ui.mode_num))
	
	
	main_ui.BackGroundSetting("background1")
	main_ui.Button1()
	main_ui.mainloop()
