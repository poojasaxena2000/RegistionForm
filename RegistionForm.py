from tkinter import *
import pymysql as p

def fun():
    if(java.get() and  python.get()):
        tech='JAVA AND PYTHON'
    elif(java.get()):
        tech='JAVA'
    else:
        tech='PYTHON'
    if(gender_signal.get()==1):
        gender='male'
    else:
        gender='female'
        
    print(name_entry.get())
    print(email_entry.get())
    print(gender)
    print(c.get())
    print(tech)
    conn = p.connect(host="localhost",user="root",password="",database="pooja")

    myCursor = conn.cursor()

    myCursor.execute("INSERT INTO students(name,email,gender,country,programming) VALUES(%r,%r,%r,%r,%r)"%(name_entry.get(),email_entry.get(),gender,c.get(),tech)) 

    conn.commit()
    conn.close()

root = Tk()
root.geometry('500x500')
root.title('Registration Form')

label_0 = Label(root,text='Registration form',width=20,font=('bold',20))
label_0. place(x=90,y=53)

name_label = Label(root,text='FullName',width=20,font=('bold',10))
name_label.place(x=80,y=130)

name_entry= Entry(root)
name_entry.place(x=240,y=130)

email_label= Label(root,text='Email',width=20,font=('bold',10))
email_label.place(x=68,y=180)

email_entry = Entry(root)
email_entry.place(x=240,y=180)

gender_label = Label(root,text='Gender',width=20,font=('bold',10))
gender_label.place(x=70,y=230)
gender_signal= IntVar()
Radiobutton(root,text='male',padx= 5,variable=gender_signal,value=1).place(x=235,y=230)
Radiobutton(root,text='female',padx = 20,variable=gender_signal,value=2).place(x=290,y=230)


country_label = Label(root,text='country',width=20,font=('bold',10))
country_label.place(x=70,y=280)

list1 = ('Canada','India','Uk','Napal','Iceland','South Africa')
c=StringVar()
droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y=280)

programming_label= Label(root,text='programming',width=20,font=('bold',10))
programming_label.place(x=85,y=330)
java = IntVar()
Checkbutton(root,text='java',variable=java).place(x=235,y=330)
python= IntVar()
Checkbutton(root,text='python',variable=python).place(x=290,y=330)


a=Button(root,text='submit',width=20,bg='brown',command=fun)
a.place(x=180,y=350)




