from tkinter import *
from backend import *
t=Tk()
t.wm_title("Bookstore Management")

def get_selected_rows(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass

def view_command():
    list1.delete(0,END)
    for row in view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in search(t_val.get(),a_val.get(),y_val.get(),i_val.get()):
        list1.insert(END,row)
        
def insert_command():
    insert(t_val.get(),a_val.get(),y_val.get(),i_val.get())
    list1.delete(0,END)
    list1.insert(END,(t_val.get(),a_val.get(),y_val.get(),i_val.get()))

def delete_command():
    delete(selected_tuple[0])

def update_command():
    update(selected_tuple[0],t_val.get(),a_val.get(),y_val.get(),i_val.get())
    # print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])


l1=Label(t,text="Title")
l1.grid(row=0,column=0)

l2=Label(t,text="Author")
l2.grid(row=0,column=2)

l3=Label(t,text="Year")
l3.grid(row=1,column=0)

l4=Label(t,text="ISBN")
l4.grid(row=1,column=2)

t_val=StringVar()
e1=Entry(t,textvariable=t_val)
e1.grid(row=0,column=1)

a_val=StringVar()
e2=Entry(t,textvariable=a_val)
e2.grid(row=0,column=3)

y_val=StringVar()
e3=Entry(t,textvariable=y_val)
e3.grid(row=1,column=1)

i_val=StringVar()
e4=Entry(t,textvariable=i_val)
e4.grid(row=1,column=3)

list1=Listbox(t,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(t)
sb1.grid(row=2,column=2,rowspan=6)

list1.bind('<<ListboxSelect>>',get_selected_rows)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(t,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(t,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(t,text="Add Entry",width=12,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(t,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(t,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(t,text="Close",width=12,command=t.destroy)
b6.grid(row=7,column=3)

t.mainloop()