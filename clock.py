import tkinter as tk
import time


window = tk.Tk()

window.title('Digital Clock')

clock_label = tk.Label(window, font=('Ariel', 80 ))
clock_label.pack()

clock_label.configure(fg='cyan', bg='black')


def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_time)


window.after(1000, update_time)


window.mainloop()
