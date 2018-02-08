from tkinter import *  
def Btnclick(numbers):
	global operator
	operator=operator+str(numbers)
	text_input.set(operator)	
def btnequalsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""    
cal=Tk()
cal.title("calculator")
operator=""
text_input=StringVar()
txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=3,insertwidth=4,
	             bg="powder blue",justify='right').grid(columnspan=4)
btn7=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="7",bg="powder blue",command=lambda:Btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="8",bg="powder blue",command=lambda:Btnclick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="9",bg="powder blue",command=lambda:Btnclick(9)).grid(row=1,column=2)
addition=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="+",bg="powder blue",command=lambda:Btnclick("+")).grid(row=1,column=3)
btn4=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="4",bg="powder blue",command=lambda:Btnclick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="5",bg="powder blue",command=lambda:Btnclick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="6",bg="powder blue",command=lambda:Btnclick(6)).grid(row=2,column=2)
subtraction=Button(cal,padx=16,bd=8,fg="black",font=('aqua',20,'bold'),
	        text="-",bg="powder blue",command=lambda:Btnclick("-")).grid(row=2,column=3)
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="1",bg="powder blue",command=lambda:Btnclick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="2",bg="powder blue",command=lambda:Btnclick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="3",bg="powder blue",command=lambda:Btnclick(3)).grid(row=3,column=2)
multiplication=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="*",bg="powder blue",command=lambda:Btnclick("*")).grid(row=3,column=3)
floated=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text=".",bg="powder blue",command=lambda:Btnclick(".")).grid(row=4,column=0)
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="0",bg="powder blue",command=lambda:Btnclick(0)).grid(row=4,column=1)
delete=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="del",bg="powder blue").grid(row=4,column=2)
divide=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="/",bg="powder blue",command=lambda:Btnclick("/")).grid(row=4,column=3)
clear=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="c",bg="powder blue",command=lambda:btncleardisplay()).grid(row=5,column=0)
Equal=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="=",bg="powder blue",command=lambda:btnequalsinput()).grid(row=5,column=1)
power=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="**",bg="powder blue").grid(row=5,column=2)
logarithm=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),
	        text="ln",bg="powder blue").grid(row=5,column=3)
cal.mainloop()
