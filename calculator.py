from tkinter import *
root = Tk()
root.geometry("400x250")
root.title("My Calculator")
root.configure(bg="black")
root.resizable(0,0)
# a should be string variable
a=StringVar()

def show(num):
    a.set(a.get()+num) #set the value of a to num
def clr():
    a.set(" ") #set the value of a to clear
def eql():
    a.set(eval(a.get())) # solve the function in the entry with the eval function

e1=Entry(font=("Times 20"),border=10,textvariable=a)
e1.place(x=0,y=0,width=400,height=60)

bt1=Button(root,bg="gray",text="7",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt1.place(x=0,y=50,width=100,height=50)
bt1.configure(command=lambda :show("7"))
bt1.configure(border=5)

bt2=Button(root,bg="gray",text="8",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt2.place(x=100,y=50,width=100,height=50)
bt2.configure(command=lambda :show("8"))
bt2.configure(border=5)

bt3=Button(root,bg="gray",text="9",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt3.place(x=200,y=50,width=100,height=50)
bt3.configure(command=lambda :show("9"))
bt3.configure(border=5)

bt4=Button(root,bg="gray",text="+",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt4.place(x=300,y=50,width=100,height=50)
bt4.configure(command=lambda :show("+"))
bt4.configure(border=5)

bt5=Button(root,bg="gray",text="4",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt5.place(x=0,y=100,width=100,height=50)
bt5.configure(command=lambda :show("4"))
bt5.configure(border=5)

bt6=Button(root,bg="gray",text="5",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt6.place(x=100,y=100,width=100,height=50)
bt6.configure(command=lambda :show("5"))
bt6.configure(border=5)

bt7=Button(root,bg="gray",text="6",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt7.place(x=200,y=100,width=100,height=50)
bt7.configure(command=lambda :show("6"))
bt7.configure(border=5)

bt8=Button(root,bg="gray",text="-",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt8.place(x=300,y=100,width=100,height=50)
bt8.configure(command=lambda :show("-"))
bt8.configure(border=5)

bt9=Button(root,bg="gray",text="1",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt9.place(x=0,y=150,width=100,height=50)
bt9.configure(command=lambda :show("1"))
bt9.configure(border=5)

bt10=Button(root,bg="gray",text="2",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt10.place(x=100,y=150,width=100,height=50)
bt10.configure(command=lambda :show("2"))
bt10.configure(border=5)

bt11=Button(root,bg="gray",text="3",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt11.place(x=200,y=150,width=100,height=50)
bt11.configure(command=lambda :show("3"))
bt11.configure(border=5)

bt12=Button(root,bg="gray",text="*",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt12.place(x=300,y=150,width=100,height=50)
bt12.configure(command=lambda :show("*"))
bt12.configure(border=5)

bt13=Button(root,bg="gray",text="C",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt13.place(x=0,y=200,width=100,height=50)
bt13.configure(command= clr)
bt13.configure(border=5)

bt14=Button(root,bg="gray",text="0",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt14.place(x=100,y=200,width=100,height=50)
bt14.configure(command=lambda :show("0"))
bt14.configure(border=5)

bt15=Button(root,bg="gray",text="=",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt15.place(x=200,y=200,width=100,height=50)
bt15.configure(command= eql)
bt15.configure(border=5)

bt16=Button(root,bg="gray",text="/",fg="white",font=("Times 20 bold"),activebackground="yellow",activeforeground="red")
bt16.place(x=300,y=200,width=100,height=50)
bt16.configure(command=lambda :show("/"))
bt16.configure(border=5)

root.mainloop()
