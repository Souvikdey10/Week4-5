import sqlite3
from tkinter import *
import tkinter  as tk
from tkinter import messagebox
root=Tk()
root.configure(bg='cyan')
#title
root.title("Week-5(076)")
def insert():
    d1 = e1.get()
    d2 =e2.get()
    d3 = e3.get()
    d4 = e4.get()
    d5 = e5.get()
    d6 = e6.get()
    d7 = e7.get()
    d8 = e8.get()
    d9 = e9.get()
    d10=e10.get()
    d11=e11.get()
    d12=e12.get()
    d13=e13.get()
    d14=e14.get()
    d15 = e15.get()
    d16 = e16.get()
    d17 = e17.get()
    d18 = e18.get()
    d19 = e19.get()
    d20 = e20.get()
    d21 =e21.get()
    d22 = e22.get()
    d23= e23.get()
    d24=e24.get()
    d25=e25.get()
    d26=e26.get()
    d27=e27.get()
    conn = sqlite3.connect('register.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Comp (data1 TEXT,data2 TEXT,data3 TEXT,data4 TEXT,data5 TEXT, data6 TEXT,data7 TEXT,data8 TEXT,data9 TEXT,data10 TEXT,data11 TEXT, data12 TEXT, data13 TEXT,data14 TEXT,data15 TEXT,data16 TEXT,data17 TEXT, data18 TEXT, data19 TEXT,data20 TEXT,data21 TEXT,data22 TEXT,data23 TEXT, data24 TEXT, data25 TEXT,data26 TEXT,data27 TEXT)')
        cursor.execute('INSERT INTO Comp (data1, data2, data3, data4, data5, data6, data7 ,data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26, data27) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,))
    conn.commit()
    msg = messagebox.showinfo( "DB Demo","One Row Inserted")
    
def dele():
    conn = sqlite3.connect('register076.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('DELETE FROM Comp')
        msg = messagebox.showinfo( "Delete Record","All Row Deleted") 
        
def disp():
    conn = sqlite3.connect('register076.db')
    with conn:
        cursor=conn.cursor()
        my_w = tk.Tk()
        my_w.geometry("400x250") 

        r_set=cursor.execute('''SELECT * from Comp ''');
        i=0 # row value inside the loop 
        for Comp in r_set: 
            for j in range(len(Comp)):
                e = Entry(my_w, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, Comp[j])
            i=i+1  
#MAIN HEADING
Label(root,text="REGISTRATION INFORMATION",bg="white",fg="black",font=("Comic Sans MS Bold",25)).pack(fill=X)

#Setting window size
root.geometry("500x500")

l1=Label(root,text="Registration Period: (check one)",bg="cyan",fg="black",font=("Arial Bold",15))
l1.place(x=0,y=52)

#Adding checkbutton
ch1=Checkbutton(root,text="One Year",bg="cyan",fg="black",font=10)
ch1.place(x=350,y=52)

ch2=Checkbutton(root,text="Two Years($2 discount applies)",bg="cyan",fg="black",font=10)
ch2.place(x=500,y=52)

ch3=Checkbutton(root,text="Three Years($3 discount applies)",bg="cyan",fg="black",font=10)
ch3.place(x=850,y=52)
l2=Label(root,text="(not available for vehicles subject to emissions testing)",bg="cyan",font=10)
l2.place(x=850,y=80)
l3=Label(root,text="Registration Type:",bg="cyan",fg="black",font=("Arial Bold",15))
l3.place(x=0,y=120)
ch4=Checkbutton(root,text="Original",bg="cyan",fg="black",font=10)
ch4.place(x=350,y=120)
ch5=Checkbutton(root,text="Renewal",bg="cyan",fg="black",font=10)
ch5.place(x=510,y=120)
ch6=Checkbutton(root,text="Private",bg="cyan",fg="black",font=10)
ch6.place(x=840,y=120)
ch7=Checkbutton(root,text="Reissue(Plates and Decals)",bg="cyan",fg="black",font=10)
ch7.place(x=980,y=120)
Label(root,text="See Reissue Plates below under plate information",bg="cyan",fg="black",font=10).place(x=980,y=150)
ch8=Checkbutton(root,text="Reissue(Decals Only)",bg="cyan",fg="black",font=10)
ch8.place(x=0,y=155)
ch9=Checkbutton(root,text="Rental Vehicle",bg="cyan",fg="black",font=10)
ch9.place(x=350,y=155)

ch10=Checkbutton(root,text="Transfer Plate Number:",bg="cyan",fg="black",font=10)
ch10.place(x=510,y=155)
entry = Entry(root,width=25)
entry.place(x=760,y=165)
l4=Label(root,text="ENTER PLATE NUM",bg="cyan",fg="black",font=("Arial Bold",10))
l4.place(x=760,y=185)
ch11=Checkbutton(root,text='For Hire(complete "For Hire Information")',bg="cyan",fg="black",font=10)
ch11.place(x=0,y=210)
ch12=Checkbutton(root,text='Ridesharing(Cannot excced 16 passengers including driver)',bg="cyan",fg="black",font=5)
ch12.place(x=510,y=210)
l5=Label(root,text="Seating Capacity:",bg="cyan",fg="black",font=("Arial Bold",15))
l5.place(x=1100,y=210)
e2=Entry(root)
e2.place(x=1290,y=210)

ch13=Checkbutton(root,text='Amateur Radio Operator call letters-Specify letters:',bg="cyan",fg="black",font=10)
ch13.place(x=0,y=250)
e3=Entry(root)
e3.place(x=495,y=260)
ch14=Checkbutton(root,text='Other:',bg="cyan",fg="black",font=10)
ch14.place(x=805,y=250)
e4=Entry(root,width=35)
e4.place(x=910,y=260)
#SECOND PART
l7=Label(root,text="OWNER INFORMATION",font=("Comic Sans MS Bold",25),bg="white",fg="black").place(x=550,y=295)

l8=Label(root,text="OWNERS FULL NAME(last,first,mid,suffix) OR BUSINESS NAME(if owned business) ",font=("Arial Bold",10),bg="cyan",fg="black",)
l8.place(x=0,y=350)
l9=Label(root,text="TELEPHONE NUMBER",font=("Arial Bold",10),bg="cyan",fg="black",)
l9.place(x=690,y=350)
l10=Label(root,text="DMV CUSTOMER NUMBER/FEIN/SSN",font=("Arial Bold",10),bg="cyan",fg="black",)
l10.place(x=1050,y=350)
e5=Entry(root,width=35)
e5.place(x=5,y=370)
e6=Entry(root,width=35)
e6.place(x=690,y=370)
e7=Entry(root,width=35)
e7.place(x=1050,y=370)
l11=Label(root,text="CO-OWNERS FULL LEGAL NAME(last,first,mid,suffix)",font=("Arial Bold",10),bg="cyan",fg="black",)
l11.place(x=5,y=400)
l12=Label(root,text="TELEPHONE NUMBER",font=("Arial Bold",10),bg="cyan",fg="black",)
l12.place(x=690,y=400)
l13=Label(root,text="DMV CUSTOMER NUMBER/FEIN/SSN",font=("Arial Bold",10),bg="cyan",fg="black",)
l13.place(x=1050,y=400)
e8=Entry(root,width=35)
e8.place(x=5,y=420)
e9=Entry(root,width=35)
e9.place(x=690,y=420)
e10=Entry(root,width=35)
e10.place(x=1050,y=420)

l14=Label(root,text="Owners (and Lesses if applicable)Must provide their residence/home/business address where requested,this address",font=("Arial Bold",10),bg="cyan",fg="black",)
l14.place(x=0,y=450)
l15=Label(root,text="can not be a P.O box.You Must complete form ISO-01 if you would like your address(es) updated",font=("Arial Bold",10),bg="cyan",fg="black",)
l15.place(x=0,y=470)
ll6=Label(root,text="RESIDENCE/BUSINESS JURISDICTION",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=1050,y=450)
e11=Entry(root,width=35)
e11.place(x=1050,y=470)

l17=Label(root,text="OWNER'S RESIDENCE/BUSINESS JURISDICTION(Apt #if applicable)",font=("Arial Bold",10),bg="cyan",fg="black",)
l17.place(x=5,y=490)
l18=Label(root,text="QTY",font=("Arial Bold",10),bg="cyan",fg="black",)
l18.place(x=600,y=490)
l19=Label(root,text="STATE",font=("Arial Bold",10),bg="cyan",fg="black",)
l19.place(x=990,y=490)
l20=Label(root,text="PIN CODE",font=("Arial Bold",10),bg="cyan",fg="black",)
l20.place(x=1250,y=490)
e11=Entry(root,width=35)
e11.place(x=5,y=510)
e12=Entry(root,width=35)
e12.place(x=600,y=510)
e13=Entry(root,width=35)
e13.place(x=990,y=510)
e14=Entry(root,width=17).place(x=1250,y=510)


l21=Label(root,text="OWNER'S RESIDENCE/BUSINESS JURISDICTION(Apt #if applicable)",font=("Arial Bold",10),bg="cyan",fg="black",)
l21.place(x=5,y=530)
l22=Label(font=("Arial Bold",10),bg="cyan",fg="black",)
l22.place(x=600,y=530)
l23=Label(font=("Arial Bold",10),bg="cyan",fg="black",)
l23.place(x=990,y=530)
l24=Label(font=("Arial Bold",10),bg="cyan",fg="black",)
l24.place(x=1100,y=530)
e11=Entry(root,width=35)
e11.place(x=5,y=550)
e12=Entry(root,width=35)
e12.place(x=600,y=550)
e13=Entry(root,width=35)
e13.place(x=990,y=550)
e14=Entry(root,width=17).place(x=1250,y=550)

#SECOND PART
l25=Label(root,text="OWNER EMAIL ADDRESS",font=("Arial Bold",10),bg="cyan",fg="black",)
l25.place(x=0,y=580)
l26=Label(root,text="CO-OWNERS EMAIL ADDRESS",font=("Arial Bold",10),bg="cyan",fg="black",)
l26.place(x=790,y=580)
e15=Entry(root,width=35)
e15.place(x=5,y=600)
e15=Entry(root,width=40).place(x=790,y=600)

#THIRD PART
l27=Label(root,text="ADDITIONAL INFORMATION",font=("Comic Sans MS Bold",25),bg="white",fg="black",).place(x=550,y=625)
L28=Label(root,text="LOCALITY WHERE VEHICLE IS PRINCIPALLY CHANGED",font=("Arial Bold",10),bg="cyan",fg="black").place(x=0,y=670)
L29=Label(root,text="IF NEW LOCATION ENTER THE DATE CHANGED",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=640,y=680)
L30=Label(root,text="Are any of the owners/lesses on active military duty or service?",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=1110,y=680)
c1 = Checkbutton(root,text="CITY",font=("Arial Bold",10),bg="cyan",fg="black").place(x=0,y=700)
c2 = Checkbutton(root,text="COUNTRY",font=("Arial Bold",10),bg="cyan",fg="black").place(x=55,y=700)
c3 = Checkbutton(root,text="TOWN OF",font=("Arial Bold",10),bg="cyan",fg="black").place(x=140,y=700)
e16=Entry(root,width=30).place(x=230,y=700)
e17=Entry(root,width=50).place(x=640,y=700)
c4 = Checkbutton(root,text="YES",font=("Arial Bold",10),bg="cyan",fg="black").place(x=1200,y=700)
c5 = Checkbutton(root,text="NO",font=("Arial Bold",10),bg="cyan",fg="black").place(x=1255,y=700)


L31=Label(root,text="IF YOU WOULD LIKE YOUR REGISTRATION RENEWALS SENT TO AN ADDRESS OTHER THAN RESDIDENCE/BUSINESS ADRESS ENTER IN TBELOW? ",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=0,y=725)
L32=Label(root,text="REGISTRATION MAILING ADDRESS-OPTIONAL",font=("Arial Bold",10),bg="cyan",fg="black").place(x=0,y=745)
L33=Label(root,text="CITY",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=600,y=745)
L34=Label(root,text="STATE",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=990,y=745)
L35=Label(root,text="PIN CODE",font=("Arial Bold",10),bg="cyan",fg="black",).place(x=1250,y=745)
e16=Entry(root,width=40).place(x=5,y=775)
e17=Entry(root,width=40).place(x=600,y=775)
e18=Entry(root,width=40).place(x=990,y=775)
e19=Entry(root,width=17).place(x=1250,y=775)


btn = Button(root,text="SUBMIT",font=("Arial Bold",15),fg="black",bg="red").place(x=730,y=800)
root.mainloop()
