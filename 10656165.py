from tkinter import *
import random
import time;
import datetime
from tkinter import messagebox

root = Tk()
root.geometry("1250x650+0+0")
root.title("Billing Systems")

Tops = Frame(root, width = 1250, height = 100, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 440, height = 650, bd=8, relief="raise")
f2.pack(side=RIGHT)



f1a = Frame(f1, width = 800, height = 330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width = 800, height = 320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 400, height = 430, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 400, height = 430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width = 450, height = 330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width = 450, height = 330, bd=8, relief="raise")
f2ab.pack(side=RIGHT)

lblInfo= Label(Tops,font=('arial',60,'bold'),text="        Online Billing Systems      ", bd= 10, anchor= 'w')
lblInfo.grid(row=0,column=0)

#==========================================calculator============================================================================#
text_Input=StringVar()
operator=""
PaymentRef=StringVar()
PaidTax=StringVar()
HomeDelivery=StringVar()
Blinds=StringVar()
Fabric=StringVar()
Carpets=StringVar()
OrderDate=StringVar()
CostofCarpete=StringVar()
CostofFabric=StringVar()
CostofBlinds=StringVar()
CostOfDelivery=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

HomeDelivery.set(0)
Blinds.set(0)
Fabric.set(0)
Carpets.set(0)


def iExit():
    qExit = messagebox.askyesno("Billing system","Do you want to exit the sysyem")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    PaymentRef.set("")
    PaidTax.set("")
    HomeDelivery.set(0)
    Blinds.set(0)
    Fabric.set(0)
    Carpets.set(0)
    OrderDate.set("")
    CostofCarpete.set("")
    CostofFabric.set("")
    CostofBlinds.set("")
    CostOfDelivery.set("")
    SubTotal.set("")
    TotalCost.set("")


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =  str(eval(operator))
    text_Input.set(sumup)
    operator=""
    

txtDisply= Entry(f2,font=('arial',20,'bold'), textvariable=text_Input, bd= 40, insertwidth=6,
                 justify='right')
txtDisply.grid(columnspan=4)
btn7=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="7",
            command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="8",
            command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="9",
            command=lambda:btnClick(9)).grid(row=1,column=2)
btnplus=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="+",
               command=lambda:btnClick("+")).grid(row=1,column=3)
#-----------------------------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="4",
            command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="5",
            command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="6",
            command=lambda:btnClick(6)).grid(row=2,column=2)
btnminus=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="-",
                command=lambda:btnClick("-")).grid(row=2,column=3)
#-----------------------------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="1",
            command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="2",
            command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="3",
            command=lambda:btnClick(3)).grid(row=3,column=2)
btnMult=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="*",
               command=lambda:btnClick("*")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="0",
            command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="C",
                command=lambda:btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="=",
                 command=lambda:btnEqualsInput()).grid(row=4,column=2)
btnDiv=Button(f2,padx=16,bd=8,fg="black",font=("arial",20,'bold'),text="/",
              command=lambda:btnClick("/")).grid(row=4,column=3)

#-----------------------------------------------------------Order Information-----------------------------------------------------

lblRef = Label(f1aa,font=("arial",16,'bold'),text="sales referance",
               bd=16,justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=("arial",16,'bold'),textvariable=PaymentRef,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=0,column=1)

lblRef = Label(f1aa,font=("arial",16,'bold'),text="Carpets",bd=16,justify='left')
lblRef.grid(row=1,column=0)
txtRef=Entry(f1aa,font=("arial",16,'bold'),textvariable=Carpets,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=1,column=1)

lblRef = Label(f1aa,font=("arial",16,'bold'),
               text="Fabric",bd=16,justify='left')
lblRef.grid(row=2,column=0)
txtRef=Entry(f1aa,font=("arial",16,'bold'),textvariable=Fabric,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=2,column=1)

lblRef = Label(f1aa,font=("arial",16,'bold'),text="Blinds",bd=16,justify='left')
lblRef.grid(row=3,column=0)
txtRef=Entry(f1aa,font=("arial",16,'bold'),textvariable=Blinds,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=3,column=1)

lblRef = Label(f1aa,font=("arial",16,'bold'),text="Home Delivery",bd=16,justify='left')
lblRef.grid(row=4,column=0)
txtRef=Entry(f1aa,font=("arial",16,'bold'),textvariable=HomeDelivery,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=4,column=1)



#-----------------------------------------------------------Order Information-----------------------------------------------------

lblRef = Label(f1ab,font=("arial",16,'bold'),text="Order Date",bd=16,justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1ab,font=("arial",16,'bold'),textvariable=OrderDate,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=0,column=1)


lblRef = Label(f1ab,font=("arial",16,'bold'),text="Cost of Carpete",
               bd=16,justify='left')
lblRef.grid(row=1,column=0)
txtRef=Entry(f1ab,font=("arial",16,'bold'),textvariable=CostofCarpete,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=1,column=1)

lblRef = Label(f1ab,font=("arial",16,'bold'),text="Cost of Fabric",
               bd=16,justify='left')
lblRef.grid(row=2,column=0)
txtRef=Entry(f1ab,font=("arial",16,'bold'),textvariable=CostofFabric,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=2,column=1)

lblRef = Label(f1ab,font=("arial",16,'bold'),text="Cost of Blinds",bd=16,justify='left')
lblRef.grid(row=3,column=0)
txtRef=Entry(f1ab,font=("arial",16,'bold'),textvariable=CostofBlinds,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=3,column=1)

lblRef = Label(f1ab,font=("arial",16,'bold'),text="Cost Of Delivery",
               bd=16,justify='left')
lblRef.grid(row=4,column=0)
txtRef=Entry(f1ab,font=("arial",16,'bold'),textvariable=CostOfDelivery,
             bd=10,insertwidth=2,justify='left')
txtRef.grid(row=4,column=1)

#-----------------------------------------------------------Order Information f2aa-----------------------------------------------------

lblRef = Label(f2aa,font=("arial",16,'bold'),text="Paid Tax",
               bd=8,anchor='w')
lblRef.grid(row=2,column=0)
txtRef=Entry(f2aa,font=("arial",16,'bold'),textvariable=PaidTax,
             bd=8,insertwidth=2,justify='left')
txtRef.grid(row=2,column=1)

lblRef = Label(f2aa,font=("arial",16,'bold'),text="Sub Total",
               bd=8,anchor='w')
lblRef.grid(row=3,column=0)
txtRef=Entry(f2aa,font=("arial",16,'bold'),textvariable=SubTotal,
             bd=8,insertwidth=2,justify='left')
txtRef.grid(row=3,column=1)

lblRef = Label(f2aa,font=("arial",16,'bold'),text="Total Cost",
               bd=8,anchor='w')
lblRef.grid(row=4,column=0)
txtRef=Entry(f2aa,font=("arial",16,'bold'),textvariable=TotalCost,
             bd=8,insertwidth=2,justify='left')
txtRef.grid(row=4,column=1)


#-----------------------------------------------------------Order Information f2aa-----------------------------------------------------

btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=("arial",16,'bold'),
                width=15,text="Total Cost").grid(row=0,column=0)
btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=("arial",16,'bold'),
                width=15,text="Sales Referance").grid(row=0,column=1)
btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=("arial",16,'bold'),
                width=15,text="Reset",command=Reset).grid(row=1,column=0)
btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=("arial",16,'bold'),
                width=15,text="Exit",command=iExit).grid(row=1,column=1)

root.mainloop()
