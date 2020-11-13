from tkinter import *
import random
from tkinter import messagebox
import lab_stp_v3 as main
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import pylab as plb
import matplotlib.ticker as ticker

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

		self.canvas = Canvas(master, bg='#B5F3D7', highlightthickness=0)
		self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.canvas1 = Canvas(self.canvas, bg='#5C2A47')
		self.canvas1.place(relx=0, rely=0, relwidth=.3, relheight=1)

		self.canvas2 = Canvas(self.canvas, bg='#5C2A47')
		self.canvas2.place(relx=.3, rely=0, relwidth=.4, relheight=1)

		self.canvas3 = Canvas(self.canvas, bg='#5C2A47')
		self.canvas3.place(relx=.7, rely=0, relwidth=.3, relheight=1)

		self.button1 = Button(self.canvas1, text='Ввести вручную', font=self.font, command=self.com1, bg='#A3B262')
		self.button1.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		self.button2 = Button(self.canvas2, text='Случайный список', font=self.font, command=self.com2, bg='#A3B262')
		self.button2.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		self.button3 = Button(self.canvas3, text='Считать из файла', font=self.font, command=self.com3, bg='#A3B262')
		self.button3.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		master.bind('<Escape>', self.exit_func)

	def exit_func(self, event):
		# root.destroy()
		exit()

	def com1(self):
		self.new_window = Toplevel(root)
		self.new_window.geometry('500x300')
		self.new_window.resizable(False, False)
		self.canvas11 = Canvas(self.new_window, bg='#5C2A47')
		self.canvas11.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.text3 = Text(self.canvas11, font=self.font, wrap=WORD)
		self.text3.place(relx=0.01, rely=0.01, relwidth=.98, relheight=.49)
		self.scr = Scrollbar(self.canvas11, command=self.text3.yview)
		self.text3.configure(yscrollcommand=self.scr.set)
		self.button11 = Button(self.canvas11, text='Посчитать время', font=self.font, command=self.sortirovka, bg='#A3B262')
		self.button11.place(relx=.05, rely=.7, relwidth=.9, relheight=.1)
		self.scr.place(relx=.98, rely=.01, relwidth=.02, relheight=.49)
		self.new_window.bind('<Escape>', self.close_win)

	def com2(self):
		self.new_window = Toplevel(root)
		self.new_window.geometry('500x300')
		self.new_window.resizable(False, False)
		self.canvas22 = Canvas(self.new_window, bg='#5C2A47')
		self.canvas22.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.random_list_of_nums = []
		self.labell = Label(self.canvas22, font=self.font, text='Размер массива: ', bg='#5C2A47', fg='white')
		self.labell.place(relx=.05, rely=.55, relwidth=.45, relheight=.1)
		self.microentry = Entry(self.canvas22, font=self.font)
		self.microentry.place(relx=.5, rely=.55, relwidth=.2, relheight=.1)
		self.microentry.bind('<Return>', self.new_array)
		for i in range(5000):
			self.a = random.randint(-2500, 2500)
			self.random_list_of_nums.append(self.a)
		self.text3 = Text(self.canvas22, font=self.font, wrap=WORD)
		self.text3.place(relx=0.01, rely=0.01, relwidth=.98, relheight=.49)
		self.scr = Scrollbar(self.canvas22, command=self.text3.yview)
		self.text3.configure(yscrollcommand=self.scr.set)
		self.button22 = Button(self.canvas22, text='Посчитать время', font=self.font, command=self.sortirovka, bg='#A3B262')
		self.button22.place(relx=.05, rely=.7, relwidth=.9, relheight=.1)
		self.scr.place(relx=.98, rely=.01, relwidth=.02, relheight=.49)
		self.text3.delete('0.0', END)
		self.text3.insert('0.0', str(self.random_list_of_nums))
		self.new_window.bind('<Escape>', self.close_win)

	def com3(self):
		self.new_window = Toplevel(root)
		self.new_window.geometry('500x300')
		self.new_window.resizable(False, False)
		self.canvas33 = Canvas(self.new_window, width=500, height=300, bg='#5C2A47')
		self.canvas33.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.entry3 = Entry(self.canvas33, font=self.font)
		self.entry3.place(relx=.01, rely=.01, relwidth=.49, relheight=.1)
		self.entry3.insert(0, 'message.txt')
		self.entry3.configure(state=DISABLED)
		self.button33 = Button(self.canvas33, text='Считать файл', font=self.font, command=self.open_file)
		self.button33.place(relx=.5, rely=.01, relwidth=.49, relheight=.1)
		self.text3 = Text(self.canvas33, font=self.font, wrap=WORD)
		self.text3.place(relx=0.01, rely=0.12, relwidth=.98, relheight=.49)
		self.scr = Scrollbar(self.canvas33, command=self.text3.yview)
		self.text3.configure(yscrollcommand=self.scr.set)
		self.button33 = Button(self.canvas33, text='Посчитать время', font=self.font, command=self.sortirovka, bg='#A3B262')
		self.button33.place(relx=.05, rely=.7, relwidth=.9, relheight=.1)
		self.scr.place(relx=.98, rely=.12, relwidth=.02, relheight=.49)
		self.on_click_id = self.entry3.bind('<Button-1>', self.on_click)
		self.new_window.bind('<Escape>', self.close_win)

	def on_click(self, event):
		self.entry3.configure(state=NORMAL)
		self.entry3.delete(0, END)

		self.my_entry.unbind('<Button-1>', self.on_click_id)

	def open_file(self):
		try:
			self.f = open(self.entry3.get(), encoding='utf-8')
			self.text3.delete('0.0', END)
			for line in self.f:
				self.text3.insert('0.0', line)
		except FileNotFoundError:
			messagebox.showerror('Ошибка', 'Файл не найден')

	def sortirovka(self):
		self.new_text = self.text3.get("0.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		# print(self.new_text)
		self.bubble = main.bubble_sort(self.new_text)
		# print(self.bubble)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		self.selection = main.selection_sort(self.new_text)
		# print(self.selection)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		self.insertion = main.insertion_sort(self.new_text)
		# print(self.insertion)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		self.quick = main.quick_sort(self.new_text)
		# print(self.quick)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		self.heap = main.heap_sort(self.new_text)
		# print(self.heap)
		# print(self.new_text)
		plb.rcParams['figure.figsize'] = 12, 6
		plb.rcParams.update({'figure.autolayout': True})
		plb.rcParams['lines.linewidth'] = 1
		self.x = np.arange(1, 6)
		self.y = (self.bubble, self.selection, self.insertion, self.quick, self.heap)
		self.fig, self.ax = plt.subplots()
		self.ax.bar(self.x, self.y, width=0.5, facecolor='#5C2A47', edgecolor='black', )
		# self.ax.set_facecolor('seashell')
		# self.fig.set_facecolor('floralwhite')
		# self.ax.grid(which='major', color='k')
		plt.xticks(self.x, ('Пузырьковая сортировка', 'Сортировка выборкой', 'Сортировка вставками', 'Быстрая сортировка', 'Сортировка кучей'))
		for i, v in enumerate(self.y):
			self.ax.text(i+0.81, v+0.05, str(v) + ' с', color='black', fontweight='bold')
		self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
		if self.bubble < 0.1:
			self.ax.yaxis.set_major_locator(ticker.MultipleLocator(0.01))
			self.ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.005))
		if self.bubble >= 0.1:
			self.ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
			self.ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
		if self.bubble > 5:
			self.ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
			self.ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
		plt.savefig('figure.png')
		self.img = Image.open('figure.png')
		self.render = ImageTk.PhotoImage(self.img)
		# plt.show()
		self.new_plot = Toplevel(root)
		self.new_plot.geometry('1700x600')
		self.new_plot.resizable(False, False)
		self.canv = Canvas(self.new_plot)
		self.canv.place(relx=0, rely=0, relwidth=.3, relheight=1)
		self.finale = Text(self.canv, font=self.font, wrap=WORD)
		self.finale.place(relx=0, rely=0, relwidth=.95, relheight=1)
		self.scr = Scrollbar(self.canv, command=self.finale.yview)
		self.finale.configure(yscrollcommand=self.scr.set)
		self.scr.place(relx=.95, rely=0, relwidth=.05, relheight=1)
		self.finale.delete('0.0', END)
		self.finale.insert('0.0', self.new_text)
		self.canvas44 = Canvas(self.new_plot, bg='#90918B')
		self.canvas44.place(relx=.3, rely=0, relwidth=.7, relheight=1)
		self.bglabel = Label(self.canvas44, image=self.render)
		self.bglabel.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.new_plot.bind('<Escape>', self.close_fig)

	def close_fig(self, event):
		self.new_plot.destroy()

	def close_win(self, event):
		self.new_window.destroy()

	def new_array(self, event):
		# try:
		# 	self.my_size = int(self.microentry.get())
		# 	self.random_list_of_nums = []
		# 	for i in range(self.my_size):
		# 		self.a = random.randint(int(self.my_size/2)*(-1), int(self.my_size/2))
		# 		self.random_list_of_nums.append(self.a)
		# except:
		# 	messagebox.showerror('Ошибка', 'Введите целое число!')
		if self.microentry.get() != '':
			self.my_size = int(self.microentry.get())
		if self.microentry.get() == '':
			self.my_size = 5000
		self.random_list_of_nums = []
		for i in range(self.my_size):
			self.a = random.randint(int(self.my_size/2)*(-1), int(self.my_size/2))
			self.random_list_of_nums.append(self.a)
		self.text3.delete('0.0', END)
		self.text3.insert('0.0', str(self.random_list_of_nums))

root = Tk()
root.resizable(False, False)
root.iconbitmap('icon.ico')
my_gui = GUI(root)
root.mainloop()