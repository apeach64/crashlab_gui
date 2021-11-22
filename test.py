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
		i = 14

	def BackGroundSetting(self, bgname):
		self.backGroundImage=PhotoImage(file=pwd+bgname+".png")
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)

	def tem_but(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.tem_but_clk, border=0, cursor='heart')
		self.nextButton.place(x=450, y=550)

	def tem_but_clk(self):
		First.BackGroundSetting("background1")
		print('page2')
		First.Button2_Y()
		First.Button2_N()
	
	def Button2_Y(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.yesButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_Y=Button(self, image=self.yesButtonImage, command=self.Button2_Y_clk, border=0, cursor='heart')
		self.lab_Button_Y.place(x=450, y=550)

	def Button2_Y_clk(self):
		print('page3')
		First.BackGroundSetting("background1")
		First.Button3()

	def Button2_N(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.noButtonImage=ImageTk.PhotoImage(src)
		self.lab_Button_N=Button(self, image=self.noButtonImage, command=self.Button2_N_clk, border=0)
		self.lab_Button_N.place(x=750, y=550)

	def Button2_N_clk(self):
		print('page1')
		First.BackGroundSetting("background1")
		First.tem_but()

	def Button3(self):
		src=Image.open(pwd+"NextButton.png")
		src=src.resize((200, 200), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button3_clk, border=0, cursor='heart')
		self.nextButton.place(x=950, y=500)

	def Button3_clk(self):
		First.tracking()

	def tracking(self):
		print('tracking')
		#footprint background
		First.BackGroundSetting("background_gray")
		#footprint image
		src=Image.open(pwd+"footprint_noback.png")
		src=src.resize((30, 30), Image.ANTIALIAS)
		self.footprintImage=ImageTk.PhotoImage(src)
		self.lab_foot_L=Label(image =self.footprintImage, border = 0)
		self.lab_foot_R=Label(image =self.footprintImage, border = 0)
		#cat image
		src=Image.open(pwd+"cat_back.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.catImage=ImageTk.PhotoImage(src)
		self.lab_catImage=Label(image =self.catImage, border = 0)

		global fp_finish
		fp_finish =0
		First.footprint_choose()

	def footprint_choose(self):
		global i 
		global fp_finish
		if i == -1:
			i = 13
		if i % 2 == 0:
			i -= 1
			First.footprint_L()
		else:
			i -= 1
			First.footprint_R()
		if fp_finish == 0:
			threading.Timer(1, First.footprint_choose).start()

	def footprint_L(self):
		global i
		y_foot_L = i*30
		self.lab_catImage.place(x=650, y=y_foot_L-100)
		self.lab_foot_L.place(x=660, y=y_foot_L)
		
	def footprint_R(self):
		global i
		y_foot_R = i*30 
		self.lab_catImage.place(x=650, y=y_foot_R-100)
		self.lab_foot_R.place(x=700, y=y_foot_R)
	
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
	First.tem_but()
	First.mainloop()
