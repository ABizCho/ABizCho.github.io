from tkinter import *

def calculate():
    a1 = float(e1.get())
    b1 = float(e2.get())
    c1 = float(e3.get())
    d1 = float(e4.get())

    a2 = float(e5.get())
    b2 = float(e6.get())
    c2 = float(e7.get())
    d2 = float(e8.get())

    A= a1-(300*a2/100)
    B= b1-(300*b2/100)
    C= c1-(300*c2/100)
    D= d1-(300*d2/100)

    if A>=0:
        A=0
    else:
        A=a1-(300*a2/100)
    if B>=0:
        B=0
    else:
        B=b1-(300*b2/100)
    if C>=0:
        C=0
    else:
        C=c1-(300*c2/100)
    if D>=0:
        D=0
    else:
        D=d1-(300*d2/100)

    ap=30*A*0.5/(A*0.5+B*0.5+C*0.5+D*0.5)
    bp=30*B*0.5/(A*0.5+B*0.5+C*0.5+D*0.5)
    cp=30*C*0.5/(A*0.5+B*0.5+C*0.5+D*0.5)
    dp=30*D*0.5/(A*0.5+B*0.5+C*0.5+D*0.5)

    
    if(a1+b1+c1+d1==253):
        if(A>=0):
            label1.configure(text="A당의 지역구 의원수:" +str(a1))
            label12.configure(text="A당의 전국구 의원수:" +str(round(17*a2/100)))
        else:
            label1.configure(text="A당의 지역구 의원수:" +str(a1))
            label12.configure(text="A당의 전국구 의원수:" +str(round(17*a2/100)+round(ap)))
        if(B>=0):
           label2.configure(text="B당의 지역구 의원수:" +str(b1))
           label22.configure(text="B당의 전국구 의원수:" +str(round(17*b2/100)))
        else:
           label2.configure(text="B당의 지역구 의원수:" +str(b1))
           label22.configure(text="B당의 전국구 의원수:" +str(round(17*b2/100)+round(bp)))
        if(C>=0):
           label3.configure(text="C당의 지역구 의원수:" +str(c1))
           label32.configure(text="C당의 전국구 의원수:" +str(round(17*c2/100)))
        else:
           label3.configure(text="B당의 지역구 의원수:" +str(c1))
           label32.configure(text="B당의 전국구 의원수:" +str(round(17*c2/100)+round(cp)))
        if(D>=0):
           label4.configure(text="D당의 지역구 의원수:" +str(d1))
           label42.configure(text="D당의 전국구 의원수:" +str(round(17*d2/100)))
        else:
           label4.configure(text="D당의 지역구 의원수:" +str(d1))
           label42.configure(text="D당의 전국구 의원수:" +str(round(17*d2/100)+round(dp)))

    
    





window=Tk()
window.title("Business Programming 201823869_ 조성우 ")
window.geometry("500x600")
window.resizable(False,False)

imgObj=PhotoImage(file="ajougif.gif")
imgLabel=Label(window,image=imgObj)
imgLabel.pack()
imgLabel.place(x=10,y=10)

infolabel1=Label(window,text="준연동형 비례대표제 계산기",font="Helvetica 13 bold italic")
infolabel2=Label(window,text="201823869")
infolabel3=Label(window,text="조성우")
infolabel1.pack()
infolabel2.pack()
infolabel3.pack()
infolabel1.place(x=160,y=30)
infolabel2.place(x=420,y=70)
infolabel3.place(x=440,y=90)





l1=Label(window,text="A당의 지역구 당선 의원수")
l2=Label(window,text="B당의 지역구 당선 의원수")
l3=Label(window,text="C당의 지역구 당선 의원수")
l4=Label(window,text="D당의 지역구 당선 의원수")
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l1.place(x=10,y=150)
l2.place(x=10,y=170)
l3.place(x=10,y=190)
l4.place(x=10,y=210)


l5=Label(window,text="A당의 정당 지지율")
l6=Label(window,text="B당의 정당 지지율")
l7=Label(window,text="C당의 정당 지지율")
l8=Label(window,text="D당의 정당 지지율")
l5.pack()
l6.pack()
l7.pack()
l8.pack()
l5.place(x=10,y=230)
l6.place(x=10,y=250)
l7.place(x=10,y=270)
l8.place(x=10,y=290)


e1=Entry(window)
e1.pack()
e1.place(x=180,y=150)
e2=Entry(window)
e2.pack()
e2.place(x=180,y=170)
e3=Entry(window)
e3.pack()
e3.place(x=180,y=190)
e4=Entry(window)
e4.pack()
e4.place(x=180,y=210)

e5=Entry(window)
e5.pack()
e5.place(x=180,y=230)
e6=Entry(window)
e6.pack()
e6.place(x=180,y=250)
e7=Entry(window)
e7.pack()
e7.place(x=180,y=270)
e8=Entry(window)
e8.pack()
e8.place(x=180,y=290)


b1 = Button(window,text="의원수 계산",command=calculate)
b1.pack()
b1.place(x=217,y=320)
b1["fg"]="white"
b1["bg"]="blue"


#-------------
result=Label(window,text="Result",font="bold 10")
result.pack()
result.place(x=180,y=370)

label1=Label(window,text="A당의 지역구 의원수:")
label1.pack()
label1.place(x=180,y=400)
label12=Label(window,text="A당의 전국구 의원수:")
label12.pack()
label12.place(x=180,y=420)


label2=Label(window,text="B당의 지역구 의원수:")
label2.pack()
label2.place(x=180,y=440)
label22=Label(window,text="B당의 전국구 의원수:")
label22.pack()
label22.place(x=180,y=460)

label3=Label(window,text="C당의 지역구 의원수:")
label3.pack()
label3.place(x=180,y=480)
label32=Label(window,text="C당의 전국구 의원수:")
label32.pack()
label32.place(x=180,y=500)

label4=Label(window,text="D당의 지역구 의원수:")
label4.pack()
label4.place(x=180,y=520)
label42=Label(window,text="D당의 전국구 의원수:")
label42.pack()
label42.place(x=180,y=540)


window.mainloop()




