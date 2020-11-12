from tkinter import *
import random
from tkinter import messagebox
import lab_stp as main

class GUI:
	def __init__(self, master):
		self.master = master
		master.title('')
		self.d_width = root.winfo_screenwidth()
		self.d_height = root.winfo_screenheight()
		self.w_width = 1500#int(self.d_width / 2)
		self.w_height = 850#int(self.d_height / 2)
		self.w_x = int(self.d_width / 2 - self.w_width / 2)
		self.w_y = int(self.d_height / 2 - self.w_height / 2)
		master.geometry(f'{self.w_width}x{self.w_height}+{self.w_x}+{self.w_y}')

		self.font = ('Arial', 14)

		self.canvas = Canvas(master, bg='black', highlightthickness=0)
		self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.canvas1 = Canvas(self.canvas, bg='#90918B')
		self.canvas1.place(relx=0, rely=0, relwidth=.3, relheight=1)

		self.canvas2 = Canvas(self.canvas)
		self.canvas2.place(relx=.3, rely=0, relwidth=.4, relheight=1)

		self.canvas3 = Canvas(self.canvas, bg='#90918B')
		self.canvas3.place(relx=.7, rely=0, relwidth=.3, relheight=1)

		self.button1 = Button(self.canvas1, text='Ввести вручную', font=self.font, command=self.com1)
		self.button1.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		self.button2 = Button(self.canvas2, text='Случайный список', font=self.font, command=self.com2)
		self.button2.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		self.button3 = Button(self.canvas3, text='Считать из файла', font=self.font, command=self.com3)
		self.button3.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		master.bind('<Escape>', self.exit_func)

	def exit_func(self, event):
		root.destroy()

	def com1(self):
		self.new_window = Toplevel(root)
		self.canvas11 = Canvas(self.new_window, width=500, height=300, bg='#90918B')
		self.canvas11.pack()

	def com2(self):
		self.new_window = Toplevel(root)
		self.canvas22 = Canvas(self.new_window, width=500, height=300, bg='#90918B')
		self.canvas22.pack()

	def com3(self):
		self.new_window = Toplevel(root)
		self.canvas33 = Canvas(self.new_window, width=500, height=300, bg='#90918B')
		self.canvas33.pack()

root = Tk()
root.resizable(False, False)
my_gui = GUI(root)
root.mainloop()