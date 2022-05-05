import tkinter

phonedict={}
phonefile=0
data=0

entry1=0
entry2=0
entry3=0
entry4=0
entry5=0

def showContact():
    try:
        phonefile=open("phonebook.txt","r")
        data=phonefile.read()
        phonefile.close()
        
        #create main window
        displayData=tkinter.Tk()
        displayData.title("phone numbers")
    
        #create message
        msg=tkinter.Message(displayData,text=data)
        msg.place(x=10,y=10)
        displayData.mainloop()
    except:
        None
    
    
def addContact():
    name=entry1.get()
    number=entry2.get()
    
    phonefile=open("phonebook.txt","a")
    phonefile.write(name)
    phonefile.write("\n")
    phonefile.write(number)
    phonefile.write("\n\n")
    
    phonefile.close()    
    
def updateContact():
    name=entry3.get() + "\n"
    number=entry4.get() + "\n"
    
    #serching
    phonefile=open("phonebook.txt","r")
    lines=phonefile.readlines()
    x=0
    while x<100:
        try:
            if lines[x]==name:
                lines[x+1]=number
                break
        except:
            break
        finally:
            x+=1
    
    phonefile=open("phonebook.txt","w")
    phonefile.writelines(lines)
    phonefile.close()
    
def deleteContact():
    name=entry5.get() + "\n"
    
    #serching
    phonefile=open("phonebook.txt","r")
    lines=phonefile.readlines()
    x=0
    while x<100:
        try:
            if lines[x]==name:
                lines[x]=""
                lines[x+1]=""
                break
        except:
            break
        finally:
            x+=1  
            
    phonefile=open("phonebook.txt","w")
    phonefile.writelines(lines)
    phonefile.close()
    
    
def deleteAll():
    phonefile=open("phonebook.txt","w")
    phonefile.write("")
    phonefile.close()  




def phonebook():
    m.destroy()
    phonebook=tkinter.Tk()
    phonebook.title("phonebook")
    phonebook.geometry("400x250+300+300")
    phonebook.resizable(False,False)
    
    #create label
    msg=tkinter.Label(phonebook,text="Welcome to my phone book :)\nmade by George Ghoubrial",font=10,fg="green")
    #show label
    msg.place(x=100,y=15)
    
    #create button
    btn1=tkinter.Button(phonebook,text="show contact",command=showContact)
    btn2=tkinter.Button(phonebook,text="add contact",command=addContact)
    btn3=tkinter.Button(phonebook,text="update contact",command=updateContact)
    btn4=tkinter.Button(phonebook,text="delete contact",command=deleteContact)
    btn5=tkinter.Button(phonebook,text="delete all",command=deleteAll)
    #show button
    btn1.place(x=20,y=80)
    btn2.place(x=20,y=110)
    btn3.place(x=20,y=140)
    btn4.place(x=20,y=170)
    btn5.place(x=20,y=200)
    
    #create Entry
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    
    
    entry1=tkinter.Entry(phonebook)
    entry2=tkinter.Entry(phonebook)
    entry3=tkinter.Entry(phonebook)
    entry4=tkinter.Entry(phonebook)
    entry5=tkinter.Entry(phonebook)
    #show entry
    entry1.place(x=120,y=115)
    entry2.place(x=240,y=115)
    entry3.place(x=120,y=140)
    entry4.place(x=240,y=140)
    entry5.place(x=120,y=170)
    
    phonebook.mainloop()

#create main window
m=tkinter.Tk()
m.title("login")
m.geometry("200x100+500+500")
m.resizable(False,False)

#create label
label1=tkinter.Label(m,text="user name")
label2=tkinter.Label(m,text="password")

label1.place(x=10,y=10)
label2.place(x=10,y=40)

#create entry
entry1=tkinter.Entry(m,width=15)
entry2=tkinter.Entry(m,width=15)

entry1.place(x=80,y=10)
entry2.place(x=80,y=40)

#create button
def func():
    user=entry1.get()
    pas=entry2.get()
    if user=="admin" and pas=="1234":
        phonebook()
    else:
        label3=tkinter.Label(m,text="wrong",fg="red")
        label3.place(x=80,y=70)
btn=tkinter.Button(m,text="enter",command=func)

btn.place(x=140,y=70)


m.mainloop()