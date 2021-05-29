from tkinter import *
root = Tk()
def getvals():
    print("Details Recieved")
    print(f"{namevalue.get(),Agevalue.get(),cityvalue.get(),Blood_groupvalue.get()}")
    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(),Agevalue.get(),cityvalue.get(),Blood_groupvalue.get()}\n ")

Label(root, text="Fill out the reapective details", font="Times 30 bold", pady=10,bg="green").grid(row=0, column=3)
name = Label(root, text="Name", font="Times 20 bold")
name.grid(row=1, column=0)
Age = Label(root, text="Age",font="Times 20 bold")
Age.grid(row=2,column=0)
Blood_group =Label(root, text="Blood_group", font="Times 20 bold")
Blood_group.grid(row=3,column=0)
city = Label(root, text="city",font="Times 20 bold")
city.grid(row=4,column=0)
namevalue = StringVar()
Agevalue = StringVar()
Blood_groupvalue =StringVar()
cityvalue = StringVar()
nameentry = Entry(root,textvariable=namevalue ,font ="Times 20 bold")
Ageentry = Entry(root,textvariable=Agevalue,font = "Times 20 bold")
Blood_groupentry = Entry(root,textvariable=Blood_groupvalue,font = "Times 20 bold")
cityentry = Entry(root,textvariable=cityvalue,font = "Times 20 bold")
nameentry.grid(row=1,column=3)
Ageentry.grid(row=2,column=3)
Blood_groupentry.grid(row=3,column=3)
cityentry.grid(row=4,column=3)

Button(text="SUBMIT",command=getvals).grid(row=5,column=2)








root.mainloop()