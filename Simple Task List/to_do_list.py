#import the basic Libraries...!!!

import tkinter
import tkinter.messagebox
import pickle


#creating the Working Area using Graphic Thinker...!!!

root = tkinter.Tk()

#Title of the Project...!!!
root.title("To-Do List by Application")

#Max and Min Size of the window...!!!
root.minsize(150,300)

#Addding Function to add the tasks....!!!
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

#Delete Function to add the tasks....!!!
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

#Loading  Function to add the tasks....!!!
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.csv", "rb+"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.txt")

#Loading Function to add the tasks....!!!
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.csv","wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=68)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=70)
entry_task.pack(pady=7,ipady=10)

button_add_task = tkinter.Button(root, text="Add task", width=48,height= 2,background="cyan", command=add_task)
button_add_task.pack(pady=3)

button_delete_task = tkinter.Button(root, text="Delete task", width=48,height= 2,background="red", command=delete_task)
button_delete_task.pack(pady=3)

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, height= 2,background="yellow", command=load_tasks)
button_load_tasks.pack(pady=3)

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48,height= 2,background="blue", command=save_tasks)
button_save_tasks.pack(pady=3)

root.mainloop()

#.............................................END.......................................................#
