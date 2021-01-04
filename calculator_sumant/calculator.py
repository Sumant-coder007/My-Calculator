import tkinter
from tkinter import *
from tkinter.messagebox import *
from math import *
font=('Constantia',20,'bold underline')
numericfont=('Old Standard TT',25)

window= Tk()
pic=PhotoImage(file='D:\python projects\calculator_sumant\caclpro.png')
window.title('Calc_Sumant')
window.configure(bg='gray')
window.geometry('450x590')
#functions
def all_clear(evevt):
    textfield.delete(0,END)
def clear(event):
    ex=textfield.get()
    ex=ex[0:(len(ex)-1)]
    textfield.delete(0,END)
    textfield.insert(0,ex)

def on_click(event):
    print('button clicked')
    b=event.widget
    text=b['text']
    print(text)
    if text=='=':
        try:
            ex=textfield.get()
            sol=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,sol)
        except Exception as e:
            print("Invalid Input",e)
            showerror("ERROR",e)
        return
    if text=='%':
        showinfo('INFORMATION','for a%b calculates remainder when a divided by b')
    textfield.insert(END,text)

#picture
headingLabel=Label(window,image=pic)
headingLabel.pack(side=TOP,pady=10)
#heading
heading=Label(window,text='My Calculator',font=font,bg='gray')
heading.pack(side=TOP)
#textfiled
textfield=Entry(window,font=numericfont,fg='white',justify=RIGHT,bg='gray')
textfield.pack(side=TOP,pady=10,fill=X,padx=10)
#buttons
buttonframe=Frame(window,bg='black')
buttonframe.pack(side=TOP)
temp=1
for i in range(1,4):
    for j in range(0,3):
        btn=Button(buttonframe,text=str(temp),width=5,font=numericfont,fg='green',highlightcolor='green',relief='sunken')
        btn.grid(row=i,column=j,padx=2,pady=2)
        btn.bind('<Button-1>',on_click)
        temp+=1
#zerobtn
zerobtn=Button(buttonframe,text='0',width=5,font=numericfont,fg='green',highlightcolor='green',relief='sunken')
zerobtn.grid(row=4,column=1,padx=2,pady=2)
zerobtn.bind('<Button-1>',on_click)
#doublezero
doublezerobtn=Button(buttonframe,text='00',width=5,font=numericfont,fg='green',highlightcolor='green',relief='sunken')
doublezerobtn.grid(row=4,column=0,padx=2,pady=2)
doublezerobtn.bind('<Button-1>',on_click)
#dotbtn
dotbtn=Button(buttonframe,text='.',width=5,font=numericfont,fg='green',highlightcolor='green',relief='sunken')
dotbtn.grid(row=4,column=2,padx=2,pady=2)
dotbtn.bind('<Button-1>',on_click)
#allclear
allclearbtn=Button(buttonframe,text='C',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
allclearbtn.grid(row=0,column=0,padx=2,pady=2)
allclearbtn.bind('<Button-1>',all_clear)
#clear
clearbtn=Button(buttonframe,text='Del',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
clearbtn.grid(row=0,column=2,padx=2,pady=2)
clearbtn.bind('<Button-1>',clear)
#percentage
perbtn=Button(buttonframe,text='%',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
perbtn.grid(row=0,column=1,padx=2,pady=2)
perbtn.bind('<Button-1>',on_click)
#add
addbtn=Button(buttonframe,text='+',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
addbtn.grid(row=3,column=3,padx=2,pady=2)
addbtn.bind('<Button-1>',on_click)
#subtract
subbtn=Button(buttonframe,text='-',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
subbtn.grid(row=2,column=3,padx=2,pady=2)
subbtn.bind('<Button-1>',on_click)
#divide
divbtn=Button(buttonframe,text='/',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
divbtn.grid(row=0,column=3,padx=2,pady=2)
divbtn.bind('<Button-1>',on_click)
#multiply
multbtn=Button(buttonframe,text='*',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
multbtn.grid(row=1,column=3,padx=2,pady=2)
multbtn.bind('<Button-1>',on_click)
#equal
equalbtn=Button(buttonframe,text='=',width=5,font=numericfont,fg='orange',highlightcolor='green',relief='sunken')
equalbtn.grid(row=4,column=3,padx=2,pady=2)
equalbtn.bind('<Button-1>',on_click)
def enter_btn(event):
    e=Event()
    e.widget=equalbtn
    on_click(e)
textfield.bind('<Return>',enter_btn)

####################################################################
scframe=Frame(window,bg="black")
def compute_sc(event):
    print('calculate')
    btn=event.widget
    text=btn['text']
    ex=textfield.get()  
    print(text)
    if text=='sin':
        print('sin')
        textfield.insert(END,'sin(')
    elif text=='cos':
        print('cosine')
        textfield.insert(END,'cos(')
    elif text=='tan':
        print('tangent')
        textfield.insert(END,'tan(')
    elif text=="x!":
        print('factorial')
        textfield.insert(END,'factorial(')
    elif text=='(':
        print('open')
        textfield.insert(END,'(')
    elif text==')':
        print('close')
        textfield.insert(END,')')
    elif text=='^':
        print('power')
        textfield.insert(END,'**')
    elif text=='Sqrt':
        print('square root')
        textfield.insert(END,'sqrt(')
    elif text=='pi':
        print('3.14')
        textfield.insert(END,'3.14')
    elif text=='e':
        print('2.178')
        textfield.insert(END,'2.178')
    elif text=='log':
        print('logarithm')
        textfield.insert(END,'log10(')
    elif text=='ln':
        print('ln') 
        textfield.insert(END,'log(')  
    elif text==',':
        print(',') 
        textfield.insert(END,',')     
#sine
sinbtn=Button(scframe,text='sin',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
sinbtn.grid(row=0,column=0,padx=2,pady=2)
sinbtn.bind('<Button-1>',compute_sc)
#cosine
cosbtn=Button(scframe,text='cos',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
cosbtn.grid(row=0,column=1,padx=2,pady=2)
cosbtn.bind('<Button-1>',compute_sc)
#tangent
tanbtn=Button(scframe,text='tan',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
tanbtn.grid(row=0,column=2,padx=2,pady=2)
tanbtn.bind('<Button-1>',compute_sc)
#factorial
factbtn=Button(scframe,text='x!',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
factbtn.grid(row=0,column=3,padx=2,pady=2)
factbtn.bind('<Button-1>',compute_sc)
#openbracket
openbtn=Button(scframe,text='(',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
openbtn.grid(row=1,column=0,padx=2,pady=2)
openbtn.bind('<Button-1>',compute_sc)
#closebracket
closebtn=Button(scframe,text=')',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
closebtn.grid(row=1,column=1,padx=2,pady=2)
closebtn.bind('<Button-1>',compute_sc)
#power
powbtn=Button(scframe,text='^',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
powbtn.grid(row=1,column=2,padx=2,pady=2)
powbtn.bind('<Button-1>',compute_sc)
#squareroot
sqrtbtn=Button(scframe,text='Sqrt',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
sqrtbtn.grid(row=1,column=3,padx=2,pady=2)
sqrtbtn.bind('<Button-1>',compute_sc)
#pi
pibtn=Button(scframe,text='pi',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
pibtn.grid(row=2,column=0,padx=2,pady=2)
pibtn.bind('<Button-1>',compute_sc)
#exponent
expbtn=Button(scframe,text='e',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
expbtn.grid(row=2,column=1,padx=2,pady=2)
expbtn.bind('<Button-1>',compute_sc)
#log
logbtn=Button(scframe,text='log',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
logbtn.grid(row=2,column=2,padx=2,pady=2)
logbtn.bind('<Button-1>',compute_sc)
#ln
lnbtn=Button(scframe,text='ln',width=5,font=numericfont,fg='black',highlightcolor='green',relief='raised')
lnbtn.grid(row=2,column=3,padx=2,pady=2)
lnbtn.bind('<Button-1>',compute_sc)
#comma
lnbtn=Button(scframe,text=',',width=22,font=numericfont,fg='green',highlightcolor='green',relief='raised')
lnbtn.grid(row=3,column=0,columnspan=4,padx=2,pady=2)
lnbtn.bind('<Button-1>',compute_sc)


normalcal=True

def sc_clk():
    global normalcal
    if normalcal:
        buttonframe.pack_forget()
        scframe.pack(side=TOP)
        buttonframe.pack(side=TOP)
        window.geometry('450x800')
        print('scientific')
        normalcal=False
    else:
        print('normal')
        scframe.pack_forget()
        window.geometry('450x590')
        normalcal=True
menufont=('Constantia',12,'bold')
scientific=Menu(window)
mode=Menu(scientific,font=menufont,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sc_clk)
scientific.add_cascade(label="Mode",menu=mode)
window.config(menu=scientific)
window.mainloop() 
