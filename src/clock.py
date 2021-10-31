from tkinter import *
import time


def counter():
	current_time = time.strftime("%H : %M : %S")
	clock.config(text = current_time)
	clock.after(200, counter)


window = Tk()
window.config(background='black')
window.title("Часы")
window.geometry("600x100")
clock = Label(window, font = ('comic sans',60,'bold'), bg = 'black', fg="green")
clock.grid(column = 0, row = 0, padx = 100)
counter()


window.mainloop()