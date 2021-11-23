from tkinter import *
import PIL
from PIL import Image, ImageTk
import threading

global pwd
#window
pwd = "C:/Users/Lee/anaconda3/envs/crashlab/Scripts/image/"
#ubuntu
#pwd = 

class first(Tk):
	
	def __init__(self):
		super().__init__()
		self.geometry("1200x700")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)
		#footprint routine
		global i
		i = 21

	def BackGroundSetting(self, bgname):
		self.backGroundImage=PhotoImage(file=pwd+bgname+".png")
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)

	def Button1(self):
		src=Image.open(pwd+"button1.png")
		src=src.resize((350, 150), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button1_clk, border=0, cursor='heart')
		self.nextButton.place(x=450, y=480)

	def Button1_clk(self):
		First.BackGroundSetting("background2")
		print('page2')
		First.Button2_Y()
		First.Button2_N()
	
	def Button2_Y(self):
		src=Image.open(pwd+"button2_Y.png")
		src=src.resize((200, 100), Image.ANTIALIAS)
		self.yesButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_Y=Button(self, image=self.yesButtonImage, command=self.Button2_Y_clk, border=0, cursor='heart')
		self.lab_Button_Y.place(x=700, y=450)

	def Button2_Y_clk(self):
		print('page3')
		First.BackGroundSetting("background3")
		First.tracking()

	def Button2_N(self):
		src=Image.open(pwd+"button2_N.png")
		src=src.resize((200, 100), Image.ANTIALIAS)
		self.noButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_N=Button(self, image=self.noButtonImage, command=self.Button2_N_clk, border=0)
		self.lab_Button_N.place(x=950, y=450)

	def Button2_N_clk(self):
		print('page1')
		First.BackGroundSetting("background1")
		First.Button1()

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
		self.lab_foot_L0=Label(image =self.footprintImage0, border = 0)
		self.lab_foot_R1=Label(image =self.footprintImage0, border = 0)
		self.lab_foot_L2=Label(image =self.footprintImage50, border = 0)
		self.lab_foot_R3=Label(image =self.footprintImage50, border = 0)
		self.lab_foot_L4=Label(image =self.footprintImage80, border = 0)
		self.lab_foot_R5=Label(image =self.footprintImage80, border = 0)


		global fp_finish
		fp_finish =0
		First.footprint_choose()

	def footprint_choose(self):
		global i 
		global fp_finish
		if i == 1:
			i = 21
		if i % 2 == 0:
			i -= 1
			First.footprint_L(self.lab_foot_L0)
		else:
			i -= 1
			First.footprint_R(self.lab_foot_R1)

		if fp_finish == 0:
			threading.Timer(1, First.footprint_choose).start()

	def footprint_L(self, foot):
		global i
		y_foot_L = i*30
		foot.place(x=955, y=y_foot_L)
		if y_foot_L <570:
			self.lab_foot_L2.place(x=955, y=y_foot_L+60)
		if y_foot_L <510:
			self.lab_foot_L4.place(x=955, y=y_foot_L+120)
	def footprint_R(self, foot):
		global i
		y_foot_R = i*30 
		foot.place(x=1000, y=y_foot_R)
		if y_foot_R <570:
			self.lab_foot_R3.place(x=1000, y=y_foot_R+60)
		if y_foot_R <510:
			self.lab_foot_R5.place(x=1000, y=y_foot_R+120)
	
	def Button5(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button5_clk, border=0, cursor='heart')
		self.nextButton.place(x=450, y=400)

	def Button5_clk(self):
		print("page6")
		First.BackGroundSetting("background1")
		First.Button6()

	def Button6(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button6_clk, border=0, cursor='heart')
		self.nextButton.place(x=450, y=400)

	def Button6_clk(self):
		First.BackGroundSetting("background1")
	
	#back home
	def Page7(self):
		print('page1로 가기 위한 조건')
		

if __name__ == "__main__":
	First = first()
	First.BackGroundSetting("background1")
	First.Button1()
	First.mainloop()
