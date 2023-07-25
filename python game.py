from tkinter import*
from tkinter import messagebox
import random,pickle,os
w=Tk()
w.title("MAIN PAGE")
w.configure(bg="#ffd343")
w.geometry("800x800")
l1=Label(w,text="F\nU\nN\n\nT\nI\nM\nE\n",fg="midnight blue",bg="#ffd343",font=("Segoe Script",36,"bold")).place(x=60,y=60)
l2=Label(w,text="F\nU\nN\n\nT\nI\nM\nE\n",fg="midnight blue",bg="#ffd343",font=("Segoe Script",36,"bold")).place(x=880,y=60)
with open("users.txt","w") as fn: pass
def rules():
    rule=Tk()
    rule.title("RULES")
    rule.geometry("900x800")
    rule.configure(bg="cadetblue1")
    with open(r'C:\Users\Public\Documents\rules.txt',"r") as fn:
        f=fn.readlines()
        l=Text(rule,width=400,height=400,wrap="word")
        l.pack()
        for i in f:
            print(i)
            l.insert("end",i)
        l.configure(fg="midnight blue",font=("arial",18),state="disabled") 
    rule.mainloop()
def change():
    wuha=Tk()
    wuha.title("CHANGE")
    wuha.geometry("900x800")
    wuha.configure(bg="cadetblue1")
    def add():
        li.insert("end",e.get())
        if c12i=="heads up":
            Q=ci+"HU.dat"
        else:
            Q=ci+c12i+".dat"
        with open(Q,"ab")as f:
            bina=e.get()
            pickle.dump(bina,f)
    def delete():
        ddd=li.get(li.curselection())
        li.delete(li.curselection())
        if c12i=="heads up":
            Q=ci+"HU.dat"
        else:
            Q=ci+c12i+".dat"
        f=open(Q,"rb")
        t=open("tempt.dat","wb")
        while True:
            try:
                rec=pickle.load(f)
                if rec!=ddd:
                    pickle.dump(rec,t)
            except EOFError:
                break
        f.close()
        t.close()
        os.remove(q)
        os.rename("tempt.dat",Q)
    lwe=Label(wuha,text="CUSTOMIZE\nTHE TASK",fg="dark goldenrod4",bg="cadetblue1",font=("Segoe Script",30)).place(x=350,y=19)
    c1=StringVar(wuha)
    c1.set("Levels")
    d1=OptionMenu(wuha,c1,"Levels","Kid","Teen","Family")
    d1.place(x=430,y=145)
    d1.configure(fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12))
    c11=StringVar(wuha)
    c11.set("Mode")
    d11=OptionMenu(wuha,c11,"Mode","truth","dare","heads up")
    d11.place(x=430,y=190)
    d11.configure(fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12))
    e=Entry(wuha,width=31,font=("Segoe Script",14))
    e.place(x=311,y=240)
    sb=Scrollbar(wuha,orient="horizontal")
    sb.place(x=685,y=585)
    li=Listbox(wuha,width=58,height=16,xscrollcommand=sb.set)
    li.place(x=219,y=280)
    li.configure(fg="midnight blue",font=("arial",12))
    sb.config(command=li.xview,bg="red")
    b2i=Button(wuha,text=" Add  ",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",14),command=add).place(x=662,y=230)
    b2t=Button(wuha,text="Delete",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",14),command=delete).place(x=230,y=230)
    def done():
        li.delete(0,"end")
        global ci
        global c12i
        ci=c1.get()
        c12i=c11.get()
        if c12i=="Mode" and ci=="Levels":
            messagebox.showinfo("MODE AND LEVEL","CHOOSE THE MODE AND LEVEL")
        elif c12i=="Mode":
            messagebox.showinfo("MODE","CHOOSE THE MODE")
        elif ci=="Levels":
            messagebox.showinfo("LEVEL","CHOOSE THE LEVEL")
        else:
            if c12i=="heads up":
                Q="C:\\Users\\Public\\Documents\\"+ci+"HU.dat"
            else:
                Q=ci+c12i+".dat"
            f=open(Q,"rb")
            while True:
                try:
                    ka=pickle.load(f)
                    li.insert("end",ka)
                except EOFError:
                    break
            f.close()
    done=Button(wuha,text="go",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",14),command=done).place(x=456,y=595)
    do=Button(wuha,text="done",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",14),command=wuha.destroy).place(x=447,y=650)
    wuha.mainloop()
def rateus():
    t=Tk()
    t.title("RATE US")
    def no():
        t.destroy()
        t1=Tk()
        t1.configure()
        l123=Label(t1,text="Share us your problem at XYZ33@gmail.com",fg="dark goldenrod4",font=("Segoe Script",25))
        l123.pack()
        bu=Button(t1,text="Ok",fg="dark goldenrod4",command=t1.destroy,font=("Segoe Script",18))
        bu.pack()
        t1.mainloop()
    l12=Label(t,text="do you like the game",fg="dark goldenrod4",font=("Segoe Script",20))
    l12.pack()
    bu=Button(t,text="Yes",fg="dark goldenrod4",command=t.destroy,font=("Segoe Script",18)).pack(side="left",padx=50)
    bu1=Button(t,text="No",fg="dark goldenrod4",command=no,font=("Segoe Script",18)).pack(side="right",padx=50)
def start():
    s=Tk()
    s.title("START")
    s.configure(bg="linen")
    s.geometry("900x700")
    def decline():
        messagebox.showinfo("Fail","You failed your task")
        we1.destroy()
    def add():
        li.insert("end",e.get())
        with open("users.txt","a") as nam:
            nam.write(e.get())
            nam.write(",")
    def delete():
        ppp=li.get(li.curselection())
        li.delete(li.curselection())
        with open("users.txt","r") as nam:
            fnams=nam.read()
            fname=fnams.split(",")
            del(fname[len(fname)-1])
        with open("users.txt","w") as nam:
            for i in fname:
                if i!=ppp:
                    nam.write(i)
                    nam.write(",")
    def play():
        global we1
        we1=Tk()
        we1.title("TASK MASTER")
        we1.configure(bg="antique white")
        we1.geometry("750x400")
        def DARE():
            q=c+"dare.dat"
            e=[]
            ee=0
            with open(q,"rb")as f:
                while True:
                    try:
                        ka=pickle.load(f)
                        e.append(ka)
                        ee+=1
                    except EOFError:
                        break
                kau=random.randint(0,ee)
                kaus=e[kau]
            utt=Label(we1,text="Your dare is: "+kaus,bg="antique white",fg="tomato2",font=("arial",14)).place(x=200,y=300)
            bu12=Button(we1,text="accept",fg="firebrick3",bg="antique white",command=we1.destroy,font=("Segoe Script",16)).place(x=500,y=350)
            bu121=Button(we1,text="decline",fg="firebrick3",bg="antique white",command=decline,font=("Segoe Script",16)).place(x=300,y=350)
        def TRUTH():
            q=c+"truth.dat"
            e=[]
            with open(q,"rb")as f:
                while True:
                    try:
                        ka=pickle.load(f)
                        e.append(ka)
                    except EOFError:
                        break
                kau=random.randint(0,len(e))
                kaus=e[kau]
            utt=Label(we1,text="Your Truth is: "+kaus,bg="antique white",fg="tomato2",font=("arial",14)).place(x=300,y=300)
            bu122=Button(we1,text="accept",fg="firebrick3",bg="antique white",command=we1.destroy,font=("Segoe Script",16)).place(x=500,y=350)
            bu121=Button(we1,text="decline",fg="firebrick3",bg="antique white",command=decline,font=("Segoe Script",16)).place(x=300,y=350)
        def HEADSUP():
            we1.destroy()
            global head
            head=Tk()
            head.title("HEAD UP")
            head.geometry("500x200")
            head.configure(bg="linen")
            q="C:\\Users\\Public\\Documents\\"+c+"HU.dat"
            e=[]
            with open(q,"rb")as f:
                while True:
                    try:
                        ka=pickle.load(f)
                        e.append(ka)
                    except EOFError:
                        break
                kau=random.randint(0,len(e))
                global kaus
                kaus=e[kau]
            wee=Label(head,text="The word is:",fg="firebrick3",bg="antique white",font=("Segoe Script",30)).place(x=180,y=20)
            we=Label(head,text=e[kau],fg="firebrick3",bg="antique white",font=("Segoe Script",24)).place(x=240,y=80)
            head.after(5000,entry)
            head.mainloop()
        def entry():
            kaa=Tk()
            kaa.title("ENTRY")
            kaa.after(1000,head.destroy)
            kaa.geometry("700x400")
            kaa.configure(bg="antique white")
            global iff
            iff=600
            def cc():
                global iff
                we=Label(kaa,text=iff,fg="firebrick3",bg="antique white",font=("Segoe Script",40),width=10).place(x=250,y=50)
                iff-=1
                if iff<=200:
                    we=Label(kaa,text="You dont have much time Hurry up",fg="firebrick3",bg="antique white",font=("Segoe Script",16)).place(x=250,y=140)
                if iff==0:
                    kaa.destroy()
                    messagebox.showinfo("Times up","Better luck next time")
                    iff=0
                kaa.after(1000,cc)
            cc()
            we11=Label(kaa,text="Enter your answer before time up",fg="firebrick3",bg="antique white",font=("Segoe Script",16)).place(x=250,y=140)
            e=Entry(kaa,width=28,font=("aerial",16))
            e.place(x=250,y=180)
            def check():
                eget=e.get()
                if eget.lower()==kaus:
                   messagebox.showinfo("Congratulation","Your guess is right")
                else:
                   messagebox.showinfo("Fail","your guess is wrong")
                   op="Correct word was: "+kaus
                   messagebox.showinfo("Better luck next time",op)
                kaa.destroy()
            but=Button(kaa,text="ENTRY",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12),command=check).place(x=380,y=220)
        c=c1.get() 
        c12=c11.get()
        cc=c12e.get()
        we=Label(we1,text="Player's Name",fg="firebrick3",bg="antique white",font=("Segoe Script",36)).place(x=300,y=20)
        if cc=="   Random  ":   
            LEN=li.size()
            k=random.randint(0,LEN)
            k1=li.get(k)
            we=Label(we1,text=k1,fg="firebrick3",bg="antique white",font=("Segoe Script",30)).place(x=380,y=90)
        elif cc=="   In series ":
            lnames=[]
            with open("users.txt","r")as fna:
                fnam=fna.read()
                fname=fnam.split(",")
                del(fname[len(fname)-1])
                for i in fname:
                    lnames.append(i)
            ins=lnames[0]
            we=Label(we1,text=ins,fg="firebrick3",bg="antique white",font=("Segoe Script",30)).place(x=380,y=90)
            lnames.append(ins)
            del(lnames[0])
            with open("users.txt","w")as f:
                for i in lnames:
                    f.write(i)
                    f.write(",")
        else:
          we=Label(we1,text="CHOOSE THE GAME TYPE!!",fg="firebrick3",bg="antique white",font=("Segoe Script",20)).place(x=380,y=90)  
        if c12=="Truth or Dare":
            bu12=Button(we1,text="Truth",fg="firebrick3",bg="antique white",command=TRUTH,font=("Segoe Script",16)).place(x=330,y=200)
            bu123=Button(we1,text="Dare",fg="firebrick3",bg="antique white",command=DARE,font=("Segoe Script",16)).place(x=530,y=200)
        elif c12=="Game of Dare":
            DARE()
        elif c12=="Face The Truth":
            TRUTH()
        elif c12=="Heads Up":
            we1.after(5000,HEADSUP)
        else:
           wi=Label(we1,text="CHOOSE THE GAME YOU WANT TO PLAY!!",fg="firebrick3",bg="antique white",font=("Segoe Script",20)).place(x=150,y=250)
        we1.mainloop()
    llwe=Label(s,text="FUN BEGINS",fg="goldenrod4",bg="linen",font=("Segoe Script",28)).place(x=350,y=15)
    e=Entry(s,width=22,font=("aerial",20))
    e.place(x=310,y=85)
    li=Listbox(s,width=19,height=9)
    li.place(x=305,y=130)
    li.configure(fg="grey1",font=("Segoe Script",18))
    b2i=Button(s,text="Add",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",15),command=add).place(x=645,y=70)
    b2t=Button(s,text="Delete",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",15),command=delete).place(x=222,y=72)
    c1=StringVar(s)
    c1.set("Levels")
    d1=OptionMenu(s,c1,"Levels","Kid","Teen","Family")
    d1.place(x=425,y=505)
    d1.configure(fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12))
    c11=StringVar(s)
    c11.set("    Games  ")
    d11=OptionMenu(s,c11,"  Games  ","Truth or Dare","Game of Dare","Face The Truth","Heads Up")
    d11.place(x=470,y=550)
    d11.configure(fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12))
    c12e=StringVar(s)
    c12e.set("Game types")
    d12e=OptionMenu(s,c12e,"Game types","   Random  ","   In series ")
    d12e.place(x=335,y=550)
    d12e.configure(fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12))
    but=Button(s,text="  PLAY   ",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",11),command=play).place(x=427,y=595)
    but=Button(s,text="   END   ",fg="#FFFA66",bg="dodger blue",font=("Segoe Script",12),command=s.destroy).place(x=426,y=640)
    s.mainloop()
f=Frame(w,highlightbackground="#42ff46",highlightthickness=9,width=600,height=1000,bd=3,bg="#426eff")
f.place(x=200,y=0)
l=Label(f,text="IT'S\nTIME\nTO\nPLAY",bg="#426eff",fg="#42ff46",font=("Segoe Script",42,"bold")).place(x=210,y=100)
b1=Button(f,text="START",bg="#ff426e",fg="#ffd343",font=("Segoe Script",18),command=start).place(x=30,y=420)
b2=Button(f,text="CHANGE",bg="#ff426e",fg="#ffd343",font=("Segoe Script",18),command=change).place(x=427,y=420)
b3=Button(f,text="RATE US",bg="#ff426e",fg="#ffd343",font=("Segoe Script",18),command=rateus).place(x=30,y=60)
b4=Button(f,text="EXIT",bg="#ff426e",fg="#ffd343",font=("Segoe Script",18),command=w.destroy).place(x=250,y=500)
b4=Button(f,text="RULES",bg="#ff426e",fg="#ffd343",font=("Segoe Script",18),command=rules).place(x=427,y=64)
l1=Label(f,text="*******************************",bg="#426eff",fg="#ff426e",font=("Segoe Script",22,"bold")).place(x=50,y=580)
l2=Label(f,text="\" Your enjoyment, Our motto \"",bg="#426eff",fg="#42ff46",font=("Segoe Script",20,"bold")).place(x=60,y=620)
w.mainloop()

