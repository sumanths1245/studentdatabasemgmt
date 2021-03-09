def studentadd():
    def submitadd():
        print('added')
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('420x500+220+160')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('studentdatabase.ico')
    addroot.resizable(False,False)
    #-------------------------------------------------- Add Student labels
    idlabel = Label(addroot,text='Enter ID : ',bg='gold2',anchor='w',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    idlabel.place(x=10,y=10  )

    namelabel = Label(addroot, text='Enter Name : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    namelabel.place(x=10, y=70)

    phonelabel = Label(addroot, text='Enter Phone : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    phonelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender: ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter DOB : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    doblabel.place(x=10, y=370)

    #-----------------------------------------------------------------Add student entries
    idval = StringVar()
    nameal = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman',14,'bold'),bd=5,textvariable='idval')
    identry.place(x=225,y=10)

    nameentry = Entry(addroot, font=('roman', 14, 'bold'), bd=5, textvariable='nameval')
    nameentry.place(x=225, y=70)

    phoneentry = Entry(addroot, font=('roman', 14, 'bold'), bd=5, textvariable='phoneval')
    phoneentry.place(x=225, y=130)

    emailentry = Entry(addroot, font=('roman', 14, 'bold'), bd=5, textvariable='emailval')
    emailentry.place(x=225, y=190)

    addressentry = Entry(addroot, font=('roman', 14, 'bold'), bd=5, textvariable='addressval')
    addressentry.place(x=225, y=250)

    genderentry = Entry(addroot, font=('roman', 14, 'bold'), bd=5, textvariable='genderval')
    genderentry.place(x=225, y=310)

    dobentry = Entry(addroot, font=('roman', 14, 'bold'), bd=5, textvariable='dobval')
    dobentry.place(x=225, y=370)

    #--------------------------------------------------------add button

    submitbtn = Button(addroot,text='Submit',font =('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                       bg='red',command=submitadd)
    submitbtn.place(x=130,y=430)
    addroot.mainloop()




def studentsearch():
    def search():
        print('searched')
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('420x550+220+160')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('studentdatabase.ico')
    searchroot.resizable(False,False)
    #-------------------------------------------------- Add Student labels
    idlabel = Label(searchroot,text='Enter ID : ',bg='gold2',anchor='w',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    idlabel.place(x=10,y=10  )

    namelabel = Label(searchroot, text='Enter Name : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    namelabel.place(x=10, y=70)

    phonelabel = Label(searchroot, text='Enter Phone : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    phonelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender: ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter DOB : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12)
    datelabel.place(x=10, y=430)
    #-----------------------------------------------------------------Add student entries
    idval = StringVar()
    nameal = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',14,'bold'),bd=5,textvariable='idval')
    identry.place(x=225,y=10)

    nameentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='nameval')
    nameentry.place(x=225, y=70)

    phoneentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='phoneval')
    phoneentry.place(x=225, y=130)

    emailentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='emailval')
    emailentry.place(x=225, y=190)

    addressentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='addressval')
    addressentry.place(x=225, y=250)

    genderentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='genderval')
    genderentry.place(x=225, y=310)

    dobentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='dobval')
    dobentry.place(x=225, y=370)

    dateentry = Entry(searchroot, font=('roman', 14, 'bold'), bd=5, textvariable='dateval')
    dateentry.place(x=225, y=430)

    #--------------------------------------------------------add button

    submitbtn = Button(searchroot,text='Submit',font =('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                       bg='red',command=search)
    submitbtn.place(x=130,y=490)
    searchroot.mainloop()




def studentdelete():
    print('Student Deleted')






def studentupdate():
    def update():
        print('updated')
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('420x600+220+100')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.iconbitmap('studentdatabase.ico')
    updateroot.resizable(False,False)
    #-------------------------------------------------- Add Student labels
    idlabel = Label(updateroot,text='Enter ID : ',bg='gold2',anchor='w',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    idlabel.place(x=10,y=10  )

    namelabel = Label(updateroot, text='Enter Name : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    namelabel.place(x=10, y=70)

    phonelabel = Label(updateroot, text='Enter Phone : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    phonelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender: ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter DOB : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12)
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12)
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time : ', bg='gold2', anchor='w', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12)
    timelabel.place(x=10, y=490)

    #-----------------------------------------------------------------Add student entries
    idval = StringVar()
    nameal = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',14,'bold'),bd=5,textvariable='idval')
    identry.place(x=225,y=10)

    nameentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='nameval')
    nameentry.place(x=225, y=70)

    phoneentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='phoneval')
    phoneentry.place(x=225, y=130)

    emailentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='emailval')
    emailentry.place(x=225, y=190)

    addressentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='addressval')
    addressentry.place(x=225, y=250)

    genderentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='genderval')
    genderentry.place(x=225, y=310)

    dobentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='dobval')
    dobentry.place(x=225, y=370)

    dateentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='dateval')
    dateentry.place(x=225, y=430)

    timeentry = Entry(updateroot, font=('roman', 14, 'bold'), bd=5, textvariable='timeval')
    timeentry.place(x=225, y=490)

    #--------------------------------------------------------add button

    submitbtn = Button(updateroot,text='Submit',font =('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                       bg='red',command=update)
    submitbtn.place(x=130,y=550)
    updateroot.mainloop()


def studentshow():
    print('Student Show')
def studentexport():
    print('Student Expport')
def studentexit():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()




############################################################## Slider Text
def IntroLabelTick():
    global count,text
    if(count >= len(ss)):   # if the entire string gets over
        count = 0           # restart again
        text = ''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]    # printing previous text + string ss[0] or ss[1] or ss[2] .....
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(150,IntroLabelTick)   # after 150 milliseconds text slides

################################################################## Random Color changing
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors) #(selects random color from colors)
    SliderLabel.config(fg=fg) #fore ground color(text color)
    SliderLabel.after(200,IntroLabelColorTick)    # changing color after every 200 milliseconds

##################################################################### Connect To Database
def Connectdb():
    def submitdb():
        pass
    #    global con,mycursor
    #    host = hostval.get()
    #    user = userval.get()
    #    password = passwordval.get()
    #    try:
    #        con = pymysql.connect(host=host,useruser,password=password)
    #        mycursor = con.cursor()
    #    except:
    #        messagebox.showerror('Notifications','Data is incorrect Please try again!')
    #        return
    #    try:
    #        strr = 'create database studentmanagementsystem'
    #        mycursor.execute(strr)
    #        strr = 'use studentmanagementsystem'
    #        mycursor.execute(strr)
    #        strr = 'create table studentdata(id int,name varchar(20),mobile varchar(20),email varchar(20),address varchar(20),gender varchar(20),dob varchar(20),date varchar(20),time varchar(20)'
    #        mycursor.execute(strr)
    #    except:
    #        strr = 'use studentmanagementsystem'
    #        mycursor.execute(strr)
    dbroot = Toplevel()
    dbroot.grab_set()  #other options does not work until its done
    dbroot.iconbitmap('studentdatabase.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    dbroot.geometry('470x250+700+230')
    #----------------------------------------------connectdb labels
    hostlabel = Label(dbroot, text='Enter Host: ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text='Enter User: ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='Enter Password: ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=13, anchor='w')
    passwordlabel.place(x=10, y=130)


    #-----------------------------------------------------------connectdb entry

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    hostentry.place(x=250, y=70)

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    hostentry.place(x=250, y=130)

    #-----------------------Connectdb button

    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()


#################################################################### Time
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' +date_string+ '\n'+'Time : ' +time_string)
    clock.after(2,tick)        # after(milliseconds, fn_name) fn changes after given milliseconds




#########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('1000x600+200+50')   #widthxheight+left-padding+top-padding (positioning it properly)
root.iconbitmap('studentdatabase.ico')
root.resizable(False,False)     # not allowing to resize both horizontally and vertically

############################################################################################### FRAMES
# ---------------------------------------------------------------------------------------------DataEntry frame intro
DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)  #relief is style of frameborder
DataEntryFrame.place(x=20,y=80,width=380,height=500)
fontlabel = Label(DataEntryFrame,text='---------------Welcome----------------',width=30,font=('arial',22,'italic bold'),bg='gold2')
fontlabel.pack(side=TOP,expand=TRUE)

addbtn = Button(DataEntryFrame,command=studentadd,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
addbtn.pack(side=TOP,expand=TRUE)

searchbtn = Button(DataEntryFrame,text='2. Search Student',command=studentsearch,width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
searchbtn.pack(side=TOP,expand=TRUE)

delbtn = Button(DataEntryFrame,command=studentdelete,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
delbtn.pack(side=TOP,expand=TRUE)

updatebtn = Button(DataEntryFrame,command=studentupdate,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
updatebtn.pack(side=TOP,expand=TRUE)

showbtn = Button(DataEntryFrame,command=studentshow,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
showbtn.pack(side=TOP,expand=TRUE)

exportbtn = Button(DataEntryFrame,command=studentexport,text='6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
exportbtn.pack(side=TOP,expand=TRUE)

exitbtn = Button(DataEntryFrame,command=studentexit,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue',activebackground='blue',relief=RIDGE,activeforeground='white')
exitbtn.pack(side=TOP,expand=TRUE)
# ---------------------------------------------------------------------------showdata frame intro

ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5) #relief is style of frameborder
ShowDataFrame.place(x=470,y=80,width=520,height=500)

#--------------------------------------------------------------------showdataframe
style = ttk.Style()
style.configure('Treeview.heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.column('ID',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=400)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)

################################################################################################## SLIDERS label

ss = 'Welcome To Student Management System'
count = 0
text = ''
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=200,y=0)
IntroLabelTick()             # calling sliding text fn
IntroLabelColorTick()       #calling random changing color fn

#######################################################################################################  CLOCK label

clock = Label(root,font=('timer',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()

######################################################################################################### CoonectDatabaseButton
connectbutton = Button(root,text='Coonect To Database',width=20,font=('chiller',19,' bold'),relief=RIDGE,borderwidth=4,bg='green2',
                       activebackground='blue',activeforeground='white',command=Connectdb)  #to change color when button is clicked
connectbutton.place(x=800,y=0)


root.mainloop()