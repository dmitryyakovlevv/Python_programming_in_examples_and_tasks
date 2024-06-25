from tkinter import *

wnd = Tk()
wnd.geometry("600x400")
wnd.resizable(False, False)

lbl1 = Label(wnd, text="Окно с изображением", font=("Arial Bold", 20), fg="green")
lbl1.place(x=150, y=20)

img = PhotoImage(file="/Users/dmitrijiakovlev/Desktop/Program/pycharm/Chapter11/1/forest.png")
lbl2 = Label(wnd, image=img, relief=GROOVE)
lbl2.place(x=150, y=80, width=420, height=250)

btn = Button(wnd, text="Закрыть", font=("Courier New Bold", 13), command=wnd.destroy)
btn.place(x=150, y=350, width=170, height=30)

wnd.mainloop()