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

class main_ui(Tk):
	
	def __init__(self):
		super().__init__()
		self.geometry("1200x700")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)

		#footprint routine
		global i
		i = 21

		#ros
		rospy.init_node('rfid_gui', anonymous=True)

	def BackGroundSetting(self, bgname):
		self.backGroundImage=PhotoImage(file=pwd+bgname+".png")
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)

	def Button1(self):
		src=Image.open(pwd+"button_go_big.png")
		src=src.resize((350, 150), Image.ANTIALIAS)
		self.gobigButtonImage=ImageTk.PhotoImage(src)
		self.gobigButton=Button(self, image=self.gobigButtonImage, command=self.Button1_clk, border=0)
		self.gobigButton.place(x=800, y=500)

	def Button1_clk(self):
		main_ui.BackGroundSetting("background2")
		print('page2')
		main_ui.page2_cat_init()


	def page2_cat_init(self):
		#define cat image
		src=Image.open(pwd+"cat_normal.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.catnormalImage=ImageTk.PhotoImage(src)
		self.lab_cat_normal=Label(image =self.catnormalImage, border = 0)

		src=Image.open(pwd+"cat_sad.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.catsadImage=ImageTk.PhotoImage(src)
		self.lab_cat_sad=Label(image =self.catsadImage, border = 0)

		self.cycle =0
		main_ui.page2_cat()

	def page2_cat(self):
		second = 6
		
		if self.cycle < 3:
			self.lab_cat_normal.place(x=100+100*self.cycle, y=500)
			self.cycle += 1
		
		else:
			self.lab_cat_normal.place_forget()
			self.lab_cat_sad.place(x=100+100*self.cycle, y=600)
			self.cycle += 1

		if self.cycle < 7:
			main_ui.after(int(second/6*1000), main_ui.page2_cat)
		
		else:
			main_ui.BackGroundSetting("background3")
			print('page3')
			main_ui.Button3_Y()
			main_ui.Button3_N()



	def Button3_Y(self):
		src=Image.open(pwd+"button_go.png")
		src=src.resize((250, 125), Image.ANTIALIAS)
		self.yesButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_Y=Button(self, image=self.yesButtonImage, command=self.Button3_Y_clk, border=0)
		self.lab_Button_Y.place(x=330, y=450)

	def Button3_Y_clk(self):
		print('page4')
		main_ui.BackGroundSetting("background4")
		main_ui.Button4()

	def Button3_N(self):
		src=Image.open(pwd+"button_busy.png")
		src=src.resize((250, 125), Image.ANTIALIAS)
		self.noButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_N=Button(self, image=self.noButtonImage, command=self.Button3_N_clk, border=0)
		self.lab_Button_N.place(x=620, y=450)

	def Button3_N_clk(self):
		print('page1')
		main_ui.BackGroundSetting("background1")
		main_ui.Button1()



	def Button4(self):
		self.gobigButton=Button(self, image=self.gobigButtonImage, command=self.Button4_clk, border=0)
		self.gobigButton.place(x=730, y=500)

	def Button4_clk(self):
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
		#rospy.loginfo(rospy.get_caller_id(), msg.data)
		#print(msg.data)

		if msg.data == 1:
			self.rfid = 1

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
			main_ui.BackGroundSetting("background6")
			main_ui.Button6_Y()
			print('page6')

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
		rospy.Subscriber('finish', Int32, self.callback)

		y_foot_L = i*30
		foot.place(x=875, y=y_foot_L)
		if i < max_i-2:
			self.lab_foot_L2.place(x=875, y=y_foot_L+60)
		if i < max_i-4:
			self.lab_foot_L4.place(x=875, y=y_foot_L+120)

	def footprint_R(self, foot):
		global i
		rospy.Subscriber('finish', Int32, self.callback)
		
		y_foot_R = i*30 
		foot.place(x=925, y=y_foot_R)

		if i < max_i-2:
			self.lab_foot_R3.place(x=925, y=y_foot_R+60)

		if i < max_i-4:
			self.lab_foot_R5.place(x=925, y=y_foot_R+120)



	def Button6_Y(self):
		src=Image.open(pwd+"button_okay.png")
		src=src.resize((300, 150), Image.ANTIALIAS)
		self.okayButtonImage=ImageTk.PhotoImage(src)
		self.okayButton=Button(self, image=self.okayButtonImage, command=self.Button6_Y_clk, border=0)
		self.okayButton.place(x=500, y=550)

	def Button6_Y_clk(self):
		print("page7")
		#main_ui.BackGroundSetting("background7")
		#main_ui.Button7()
'''
	def Button6_N(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button6_N_clk, border=0)
		self.nextButton.place(x=450, y=400)

	def Button6_N_clk(self):
		print("page1")
		main_ui.BackGroundSetting("background1")
		main_ui.Button1()



	def Button7(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button7_clk, border=0)
		self.nextButton.place(x=450, y=400)

	def Button7_clk(self):
		main_ui.BackGroundSetting("background1")
	
	#back home
	def Page7(self):
		print('page1')
		main_ui.BackGroundSetting("background1")
		main_ui.Button1()
	
'''


if __name__ == "__main__":
	main_ui = main_ui()
	main_ui.BackGroundSetting("background1")
	main_ui.Button1()
	main_ui.mainloop()
