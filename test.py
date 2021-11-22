from tkinter import *
import PIL
from PIL import Image, ImageTk
import threading

class first(Tk):
	
	def __init__(self):
		super().__init__()
		self.geometry("1200x700")
		#self.geometry('%dx%d+%d+%d' %(w,h,x,y))
		self.resizable(False, False)
		#footprint routine
		global i
		i = 13

	def Page1(self):
		print('page1')
		self.backGroundImage=PhotoImage(file=r"C:\Users\Lee\anaconda3\envs\crashlab\Scripts\image\background1.png")
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)
	
	def Button1(self):
		src=Image.open("C:/Users/Lee/anaconda3/envs/crashlab/Scripts/image/NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button1_clk, border=0, cursor='heart')
		self.nextButton.place(x=450, y=400)

	def Button1_clk(self):
		#First.Page2()
		#First.Button2()
		First.tracking()

	def Page2(self):
		print('page2')
		self.backGroundImage=PhotoImage(file=r"C:\Users\Lee\anaconda3\envs\crashlab\Scripts\image\background1.png")
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)
	
	def Button2(self):
		src=Image.open("C:/Users/Lee/anaconda3/envs/crashlab/Scripts/image/NextButton.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.nextButtonImage=ImageTk.PhotoImage(src)
		self.nextButton=Button(self, image=self.nextButtonImage, command=self.Button2_clk, border=0, cursor='heart')
		self.nextButton.place(x=1000, y=600)

	def Button2_clk(self):
		print('button2 clk')
		#First.Page1()
		#First.Button1()
		global fp_finish
		fp_finish =1

	def tracking(self):
		print('tracking')
		#footprint background
		self.backGroundImage=PhotoImage(file=r"C:\Users\Lee\anaconda3\envs\crashlab\Scripts\image\background_gray.png")
		self.backGroundImageLabel=Label(self, image=self.backGroundImage)
		self.backGroundImageLabel.place(x=0, y=0)
		#footprint image
		src=Image.open("C:/Users/Lee/anaconda3/envs/crashlab/Scripts/image/footprint_noback.png")
		src=src.resize((100, 100), Image.ANTIALIAS)
		self.footprintImage=ImageTk.PhotoImage(src)
		self.lab_foot_L=Label(image =self.footprintImage, border = 0)
		self.lab_foot_R=Label(image =self.footprintImage, border = 0)

		First.Button2()
		print('out of button2')
		global fp_finish
		fp_finish =0
		First.footprint_choose()

	def footprint_choose(self):
		global i 
		global fp_finish
		if i == -1:
			i = 13
		if i % 2 == 1:
			i -= 1
			First.footprint_L()
		else:
			i -= 1
			First.footprint_R()
		if fp_finish == 0:
			threading.Timer(1, First.footprint_choose).start()

	def footprint_L(self):
		global i
		y_foot_L = i*50
		self.lab_foot_L.place(x=600, y=y_foot_L)
		
	
	def footprint_R(self):
		global i
		y_foot_R = i*50 + 40
		self.lab_foot_R.place(x=700, y=y_foot_R)

if __name__ == "__main__":
	First = first()
	First.Page1()
	First.Button1()
	First.mainloop()
