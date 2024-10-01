from tkinter import *

root=Tk()
root.geometry("1200x700")
root.title("Vijayalaxshmi traders")
root.resizable(False,False)

def Reset():
    entry_friedpeanut1.delete(0,END)
    entry_friedpeanut2.delete(0,END)
    entry_friedpeanut3.delete(0,END)
    entry_peanut1.delete(0,END)
    entry_peanut2.delete(0,END)
    entry_peanut3.delete(0,END)
    entry_pottuKadalai.delete(0,END)
    entry_uppuKadalai.delete(0,END)
    entry_Pori.delete(0,END)



def Total():
    try:a1=int(Fried_peanut1.get())
    except:a1=0
    try:a2=int(Fried_peanut2.get())
    except:a2=0
    try:a3=int(Fried_peanut3.get())
    except:a3=0
    try:a4=int(Peanut1.get())
    except:a4=0
    try:a5=int(Peanut2.get())
    except:a5=0
    try:a6=int(Peanut3.get())
    except:a6=0
    try:a7=int(Pottu_kadalai.get())
    except:a7=0
    try:a8=int(Uppu_kadalai.get())
    except:a8=0
    try:a9=int(pori.get())
    except:a9=0

#define cost of each item per quality

    c1=160*a1
    c2=80*a2
    c3=40*a3
    c4=140*a4
    c5=70*a5
    c6=35*a6
    c7=90*a7
    c8= 140* a8
    c9=15*a9

    lbl_total=Label(f2,font=("aria",20,'bold'),text="Total",width=20,fg="lightyellow",bg="black")
    lbl_total.place(x=60,y=60)


    entry_total=Entry(f2,font=("aria",20,'bold'),textvariable=Total_bill,bd=6,width=20,bg="lightgreen")
    entry_total.place(x=30,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8+c9
    string_bill="Rs.", str('%0.2f' %totalcost)
    Total_bill.set(string_bill)


Label(text="VIJAYALAXSHMI TRADERS",bg="yellow",fg="blue",font=("calibri",35),width="300",height="2").pack()

#Menu card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=350,height=600)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida calligraphy",15,"bold"),text="Fried peanut.....Rs.160/1Kg",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Fried peanut.....Rs.80/1/2Kg",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Fried peanut.....Rs.40/1/4Kg",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Peanut...........Rs.140/1Kg",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Peanut...........Rs.70/1/2Kg",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Peanut...........Rs.35/1/4Kg",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Pottu kadalai....Rs.90/1Kg",fg="black",bg="lightgreen").place(x=10,y=260)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Uppu kadalai.....Rs.140/1Kg",fg="black",bg="lightgreen").place(x=10,y=290)
Label(f,font=("Lucida calligraphy",15,"bold"),text="Pori.............Rs.15/packet",fg="black",bg="lightgreen").place(x=10,y=320)

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=600)
f2.place(x=850,y=118)

Bill=Label(f2,text="Bill",font=("calibri",30),bg='lightyellow',fg="blue")
Bill.place(x=110,y=10)


#Entry work
f1=Frame(root,bd=5,height=700,width=90,relief=RAISED)
f1.pack()

Fried_peanut1=StringVar()
Fried_peanut2=StringVar()
Fried_peanut3=StringVar()
Peanut1=StringVar()
Peanut2=StringVar()
Peanut3=StringVar()
Pottu_kadalai=StringVar()
Uppu_kadalai=StringVar()
pori=StringVar()
Total_bill=StringVar()

#Label
lbl_FriedPeanut1=Label(f1,font=('aria',20,'bold'),text="Fried peanut-1Kg",width=20,fg="#FFAD60")
lbl_FriedPeanut2=Label(f1,font=('aria',20,'bold'),text="Fried peanut-1/2Kg",width=20,fg="blue4")
lbl_FriedPeanut3=Label(f1,font=('aria',20,'bold'),text="Fried peanut-1/4kg",width=20,fg="blue4")
lbl_peanut1=Label(f1,font=('aria',20,'bold'),text="Peanut-1Kg",width=20,fg="blue4")
lbl_peanut2=Label(f1,font=('aria',20,'bold'),text="Peanut-1/2Kg",width=20,fg="blue4")
lbl_peanut3=Label(f1,font=('aria',20,'bold'),text="Peanut-1/4Kg",width=20,fg="blue4")
lbl_Pottu_kadalai=Label(f1,font=('aria',20,'bold'),text="Pottu_kadalai-1Kg",width=20,fg="blue4")
lbl_Uppu_kadalai=Label(f1,font=('aria',20,'bold'),text="Uppu_kadalai-1Kg",width=20,fg="blue4")
lbl_Pori=Label(f1,font=('aria',20,'bold'),text="Pori-Packet",width=20,fg="blue4")

lbl_FriedPeanut1.grid(row=1,column=0)
lbl_FriedPeanut2.grid(row=2,column=0)
lbl_FriedPeanut3.grid(row=3,column=0)
lbl_peanut1.grid(row=4,column=0)
lbl_peanut2.grid(row=5,column=0)
lbl_peanut3.grid(row=6,column=0)
lbl_Pottu_kadalai.grid(row=7,column=0)
lbl_Uppu_kadalai.grid(row=8,column=0)
lbl_Pori.grid(row=9,column=0)

#Entry
entry_friedpeanut1=Entry(f1,font=("aria",20,'bold'),textvariable=Fried_peanut1,bd=6,width=8,bg="lightpink")
entry_friedpeanut2=Entry(f1,font=("aria",20,'bold'),textvariable=Fried_peanut2,bd=6,width=8,bg="lightpink")
entry_friedpeanut3=Entry(f1,font=("aria",20,'bold'),textvariable=Fried_peanut3,bd=6,width=8,bg="lightpink")
entry_peanut1=Entry(f1,font=("aria",20,'bold'),textvariable=Peanut1,bd=6,width=8,bg="lightpink")
entry_peanut2=Entry(f1,font=("aria",20,'bold'),textvariable=Peanut2,bd=6,width=8,bg="lightpink")
entry_peanut3=Entry(f1,font=("aria",20,'bold'),textvariable=Peanut3,bd=6,width=8,bg="lightpink")
entry_pottuKadalai=Entry(f1,font=("aria",20,'bold'),textvariable=Pottu_kadalai,bd=6,width=8,bg="lightpink")
entry_uppuKadalai=Entry(f1,font=("aria",20,'bold'),textvariable=Uppu_kadalai,bd=6,width=8,bg="lightpink")
entry_Pori=Entry(f1,font=("aria",20,'bold'),textvariable=pori,bd=6,width=8,bg="lightpink")

entry_friedpeanut1.grid(row=1,column=1)
entry_friedpeanut2.grid(row=2,column=1)
entry_friedpeanut3.grid(row=3,column=1)
entry_peanut1.grid(row=4,column=1)
entry_peanut2.grid(row=5,column=1)
entry_peanut3.grid(row=6,column=1)
entry_pottuKadalai.grid(row=7,column=1)
entry_uppuKadalai.grid(row=8,column=1)
entry_Pori.grid(row=9,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="green",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=11,column=0)

btn_total=Button(f1,bd=5,fg="Green",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=11,column=1)

root.mainloop()
