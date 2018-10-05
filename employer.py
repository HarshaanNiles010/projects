#creating an employer class
class employer:

    #this is the constructor of the class
    def __init__(self,first_name,last_name,fav_num):
        self.first_name=first_name
        self.last_name=last_name
        self.fav_num=fav_num
    def my_email(self):
        return '{}{}{}@miller.com\n'.format(self.first_name,self.last_name,self.fav_num)

    # A random password generator
    def my_password(self):
        password_list='abcdefghijklmnopqrstuvwxyz123456789'
        import random
        password=''
        for i in range(10):
            password += random.choice(password_list)
        return  'your password is: {}\n'.format(password)
def addres(event=None):
    first_candidate=employer(first_name_entry.get(),last_name_entry.get(),fav_num_entry.get())
    my_address=employer.my_email(first_candidate)
    my_key=employer.my_password(first_candidate)
    notebook.insert(ttk.END,my_key)
    notebook.insert(ttk.END,my_address)

#creating a color pallete scheme for the input boxes
color_list=['#fff2d1','#ffb3d1','#ffc4d1']

#creating window
import random
import tkinter as ttk
window = ttk.Tk()
window.geometry("500x500")

#window.configure(background='#FFF933')
frame1= ttk.Frame(master=window,width=250,height=250)
frame1.grid(row=0,column=0)

#creating the first name label
first_name=ttk.Label(master=frame1,text="enter your first name")
first_name.grid(row=0,column=0)

#creating the first name entry
first_name_entry=ttk.Entry(master=frame1,font=('roboto thin',16),bg=random.choice(color_list))
first_name_entry.grid(row=0,column=1)

#creating the last name label
last_name=ttk.Label(master=frame1,text="enter your last name")
last_name.grid(row=1,column=0)

#creating the last name entry
last_name_entry=ttk.Entry(master=frame1,font=('roboto thin',16,'italic'),bg=random.choice(color_list))
last_name_entry.grid(row=1,column=1)

# creating the favourite number label
fav_num=ttk.Label(master=frame1,text="enter the number of u r fav player")
fav_num.grid(row=2,column=0)

#creating the favourite number entry
fav_num_entry=ttk.Entry(master=frame1,font=('roboto thin',16),bg=random.choice(color_list))
fav_num_entry.grid(row=2,column=1)

#creating the scan button
scan=ttk.Button(master=frame1,text="scan the data",command=addres)
scan.grid(row=3,column=1)
window.bind("<Button-3>",addres)

#creating the notebook
notebook=ttk.Text(master=frame1,width=50,height=40)
notebook.grid(row=4,column=1)
window.mainloop()
