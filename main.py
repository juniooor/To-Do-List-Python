import tkinter  # noqa
from tkinter import *  # noqa

root = Tk()  # noqa
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask(): # noqa
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
        
def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
                
        listbox.delete( ANCHOR)      

def OpenTaskFile():  # noqa
    
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END , task)
    except:
        file =open('tasklist.txt', 'w')
        file.close()

Image_icon = PhotoImage(file='imagens/task.png')  # noqa
root.iconphoto(False, Image_icon)

Topimage = PhotoImage(file='imagens/topbar.png')   # noqa
Label(root, image=Topimage).pack()   # noqa

dockImage = PhotoImage(file='imagens/dock.png')   # noqa
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)  # noqa

noteImage = PhotoImage(file='imagens/task.png')  # noqa
Label(root, image=noteImage, bg="#32405b").place(x=320, y=18)  # noqa

heading = Label(root, text='Todas os Desafios',  # noqa
                font='arial 18 bold', fg="white", bg='#32405b')
heading.place(x=100, y=20)

frame = Frame(root, width=400, height=50, bg='white')  # noqa
frame.place(x=0, y=180)

task = StringVar()  # noqa
task_entry = Entry(frame, width=18, font="arial 20", bd=0)  # noqa
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text='ADD', font="arial 20 bold", width=6, bg="#4b7bd1",   # noqa
                fg='#fff', bd=0, command=addTask)
button.place(x=300, y=0)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")  # noqa
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16,  # noqa
                  bg="#32405b", fg="white",   # noqa
                  cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)  # noqa
scrollbar = Scrollbar(frame1)  # noqa
scrollbar.pack(side=RIGHT, fill= BOTH)  # noqa

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

OpenTaskFile()

delete_icon = PhotoImage(file='imagens/delete.png')  # noqa
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)  # noqa


root.mainloop()   # noqa