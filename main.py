import tkinter
from tkinter import *  # noqa

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

Image_icon = PhotoImage(file='imagens/task.png') # noqa
root.iconphoto(False, Image_icon)

Topimage = PhotoImage(file='imagens/topbar.png')
Label(root, image=Topimage).pack()

dockImage = PhotoImage(file='imagens/dock.png')
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file='imagens/task.png')
Label(root, image=noteImage, bg="#32405b").place(x=320, y=18)

heading = Label(root, text='Todas os Desafios', font='arial 18 bold', fg = "white", bg = '#32405b')
heading.place(x=100, y=20)
root.mainloop()  