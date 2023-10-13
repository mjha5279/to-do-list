from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("To-Do List") 
root.geometry("500x500")
def addtask():
    if(e.get()!=""):
        listbox.insert(END,e.get())
        e.delete(0,END)
    else:
        messagebox.showwarning("Attention","Please write something")
def deletetask():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Attention","please select task")
f=Frame(root,bg="grey")
f.pack()
listbox=Listbox(f,height=17,width=45)
listbox.pack()
e=Entry(f,width=45)
e.pack()
Button(f,text="Click to Add task",bg="yellow",command=addtask,width=38).pack()
Button(f,text="click to delete task",bg="pink",command=deletetask,width=38).pack()
root.mainloop()