import tkinter as Tk

class STSGui():
	def __init__(self):
		self.window = Tk.Tk()	
		self.greeting = Tk.Label(text="Hello World!")
		self.greeting.pack()	
		self.window.mainloop()
		




if __name__ == "__main__":
	STSGui()