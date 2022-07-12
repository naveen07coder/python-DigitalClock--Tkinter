from time import strftime
from tkinter import Label, Tk

#window config
border = Tk()
border.title("DIGITAL CLOCK")
#border.geometry("300x80")
border.configure(bg="black")
border.resizable(True,True)

#label config
clock_label = Label(border, bg = "black", fg = "white", font = ("Times", 30, "bold"), relief ="flat")
clock_label.place(x = 20, y = 20)

#update clock
def updating_label():
    curr_time = strftime("%H: %M: %S")
    clock_label.configure(text = curr_time)
    clock_label.after(80, updating_label) #80 milliseconds

updating_label()
border.mainloop()
