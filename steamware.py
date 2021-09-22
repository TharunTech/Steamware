import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import subprocess

from tkinter import filedialog, IntVar,Radiobutton

root = tk.Tk()
root.title('Steamware-the exclusive code helper!!')
root.iconbitmap('img/12.ico')
root.configure(bg="#BFA2DB")

canvas = tk.Canvas(root, width=600, height=300,bg="#BFA2Db")
canvas.grid(columnspan=4, rowspan=3)

#logo
logo= Image.open('img/logo_128.png')
logo=ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=2,rowspan=1,column=1,row=0)

#header
instructions=tk.Label(root,text="choose a programming language from the give below list", font=("Raleway",14),bg='#BFA2DB')
instructions.grid(columnspan=4,column=0,row=1)


#adding buttons to choose the programming language
#browse_text = tk.StringVar()
#browse_btn=tk.Button(root, textvariable=browse_text, font="Raleway",bg="#506D84",fg="white",height=2,width=15)
#browse_text.set("Choose")
#browse_btn.grid(column=1, row=7)




r2 = IntVar()
r2.set("0")


#adding radio buttons to TAB 1
r2b1=Radiobutton(root, text="Python",variable=r2, value=1,font=("Raleway",12),bg="#BFA2DB")
r2b1.grid(column=0,row=2)
r2b2=Radiobutton(root, text="Java",variable=r2, value=2,font=("Raleway",12),bg="#BFA2DB")
r2b2.grid(column=1,row=2)
r2b2=Radiobutton(root, text="C++",variable=r2, value=3,font=("Raleway",12),bg="#BFA2DB")
r2b2.grid(column=2,row=2)
r2b2=Radiobutton(root, text="Web Dev.",variable=r2, value=4,font=("Raleway",12),bg="#BFA2DB")
r2b2.grid(column=3,row=2)   

# button to load the TAB_2
browse_text2 = tk.StringVar()
button = tk.Button( root , textvariable=browse_text2 ,command =lambda:openNewWindow(r2.get()),font=("Raleway",12),bg="#D97642",fg="white",height=2,width=15,)
browse_text2.set("confirm")
button.grid(rowspan=6,columnspan=2,column=1,row=6)




# Create Label
#label = tk.Label( root , text = " " )
#label.grid(columnspan=3,column=0, row=20)

#if (clicked.set=="Python"):
#    file1 = open("myfile.txt")


#canvas extender
canvas = tk.Canvas(root, width=600, height=100,bg="#BFA2DB")
canvas.grid(columnspan=4)


#SECOND SUB window starts
def openNewWindow(value):
    browse_text2.set("loading....")

    
    # Toplevel object which will
	# be treated as a new window
    newWindow = tk.Toplevel(root)
    newWindow.iconbitmap('img/12.ico')
    newWindow.configure(bg="#BFA2DB")

    canvas = tk.Canvas(newWindow, width=600, height=300,bg="#BFA2Db")
    canvas.grid(columnspan=3,rowspan=2)    

    #image for tab 2
    logo2= Image.open('img/logo_128.png')
    logo2=ImageTk.PhotoImage(logo2)
    logo_label2 = tk.Label(newWindow,image=logo2)
    logo_label2.image = logo2
    logo_label2.grid(columnspan=1,rowspan=1,column=1,row=0)

    instructions=tk.Label(newWindow,text="choose a ''Library to add'' from the give below list", font=("Raleway",14),bg='#BFA2DB')
    instructions.grid(columnspan=3,column=0,row=1)
	# sets the title of the
	# Toplevel widget
    newWindow.title("'Steamware-Make coding easier !!'")
    
    #instructions=tk.Label(newWindow,text="choose a programming language from the give below list", font=("Raleway",14),bg='#BFA2DB')
    #instructions.grid(columnspan=3,column=0,row=1)


    canvas = tk.Canvas(newWindow, width=600, height=100,bg="#F0D9FF")
    canvas.grid(columnspan=3,rowspan=2)

    


    #python option menue
    if(value==1):
      r = IntVar()
      r.set("0")
      

      #adding radio buttons
      rb1=Radiobutton(newWindow, text="Matplot",variable=r, value=1,font=("Raleway",12),bg="#F0D9FF")
      rb1.grid(column=0,row=2)
      rb2=Radiobutton(newWindow, text="Pandas",variable=r, value=2,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=1,row=2)
      rb2=Radiobutton(newWindow, text="NumPy",variable=r, value=3,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=2,row=2)
      rb2=Radiobutton(newWindow, text="Seaborn",variable=r, value=4,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=0,row=3)
     
      #secondcanvas size increased
      canvas = tk.Canvas(newWindow, width=600, height=50, bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

	  #button to second window
      browse_text3 = tk.StringVar()
      button = tk.Button( newWindow , textvariable=browse_text3 ,command =lambda:clicked(r.get()),font=("Raleway",14),bg="#D97642",fg="white",height=2,width=18,)
      browse_text3.set("confirm")
      button.grid(column=1,row=4,rowspan=1)
  #C:\Users\OMEGA\OneDrive\Desktop\Steamware\main\Batch Files\Python
      def clicked(value):
         if(value==1):
             subprocess.Popen("main/Batch Files/Python/matplot.bat")
         if(value==2):
             subprocess.Popen('main/Batch Files/Python/pandas.bat')
         if(value==3):
             subprocess.Popen('main/Batch Files/Python/numpy.bat')
         if(value==4):
             subprocess.Popen('main/Batch Files/Python/seaborn.bat')

      canvas = tk.Canvas(newWindow, width=600, height=100,bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

    #Java Option Menue
    if(value==2):
      r = IntVar()
      r.set("0")
      

      #adding radio buttons
      rb1=Radiobutton(newWindow, text="guava",variable=r, value=1,font=("Raleway",12),bg="#F0D9FF")
      rb1.grid(column=0,row=2)
      rb2=Radiobutton(newWindow, text="jackson",variable=r, value=2,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=1,row=2)
      rb2=Radiobutton(newWindow, text="jhipster",variable=r, value=3,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=2,row=2)
      rb2=Radiobutton(newWindow, text="jsoup",variable=r, value=4,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=0,row=3)
     
      #secondcanvas size increased
      canvas = tk.Canvas(newWindow, width=600, height=50, bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

	  #button to second window
      browse_text3 = tk.StringVar()
      button = tk.Button( newWindow , textvariable=browse_text3 ,command =lambda:clicked(r.get()),font=("Raleway",14),bg="#D97642",fg="white",height=2,width=18)
      browse_text3.set("confirm")
      button.grid(column=1,row=4,rowspan=1)

      def clicked(value):
         if(value==1):
             subprocess.Popen("main/Batch Files/Java/guava.bat")
         if(value==2):
             subprocess.Popen('main/Batch Files/Java/jackson.bat')
         if(value==3):
             subprocess.Popen('main/Batch Files/Java/jhipster.bat')
         if(value==4):
             subprocess.Popen('main/Batch Files/Java/jsoup.bat')


      canvas = tk.Canvas(newWindow, width=600, height=100,bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

    #C++ option menue
    if(value==3):
      r = IntVar()
      r.set("0")
      

      #adding radio buttons
      rb1=Radiobutton(newWindow, text="google test",variable=r, value=1,font=("Raleway",12),bg="#F0D9FF")
      rb1.grid(column=0,row=2)
      rb2=Radiobutton(newWindow, text="json",variable=r, value=2,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=1,row=2)
      rb2=Radiobutton(newWindow, text="ssl",variable=r, value=3,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=2,row=2)
      rb2=Radiobutton(newWindow, text="tensorflow",variable=r, value=4,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=0,row=3)
     
      #secondcanvas size increased
      canvas = tk.Canvas(newWindow, width=600, height=50, bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

	  #button to second window
      browse_text3 = tk.StringVar()
      button = tk.Button( newWindow , textvariable=browse_text3 ,command =lambda:clicked(r.get()),font=("Raleway",14),bg="#D97642",fg="white",height=2,width=18)
      browse_text3.set("confirm")
      button.grid(column=1,row=4,rowspan=1)

      def clicked(value):
         if(value==1):
             subprocess.Popen("main/Batch Files/C++/google_test.bat")
         if(value==2):
             subprocess.Popen('main/Batch Files/C++/json.bat')
         if(value==3):
             subprocess.Popen('main/Batch Files/C++/ssl.bat')
         if(value==4):
             subprocess.Popen('main/Batch Files/C++/tensorflow.bat')


      canvas = tk.Canvas(newWindow, width=600, height=100,bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

    #Web Dev. Option Menue
    if(value==4):
      r = IntVar()
      r.set("0")
      

      #adding radio buttons
      rb1=Radiobutton(newWindow, text="django",variable=r, value=1,font=("Raleway",12),bg="#F0D9FF")
      rb1.grid(column=0,row=2)
      rb2=Radiobutton(newWindow, text="falcon",variable=r, value=2,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=1,row=2)
      rb2=Radiobutton(newWindow, text="flask",variable=r, value=3,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=2,row=2)
      rb2=Radiobutton(newWindow, text="growler",variable=r, value=4,font=("Raleway",12),bg="#F0D9FF")
      rb2.grid(column=0,row=3)
     
      #secondcanvas size increased
      canvas = tk.Canvas(newWindow, width=600, height=50, bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)

	  #button to second window
      browse_text3 = tk.StringVar()
      button = tk.Button( newWindow , textvariable=browse_text3 ,command =lambda:clicked(r.get()),font=("Raleway",14),bg="#D97642",fg="white",height=2,width=18)
      browse_text3.set("confirm")
      button.grid(column=1,row=4,rowspan=1)

      def clicked(value):
         if(value==1):
             subprocess.Popen("main/Batch Files/WebDev/django.bat")
         if(value==2):
             subprocess.Popen('main/Batch Files/WebDev/falcon.bat')
         if(value==3):
             subprocess.Popen('main/Batch Files/WebDev/flask.bat')
         if(value==4):
             subprocess.Popen('main/Batch Files/WebDev/growler.bat')


      canvas = tk.Canvas(newWindow, width=600, height=100,bg="#BFA2DB")
      canvas.grid(columnspan=3,rowspan=1)






    

    rr = IntVar()
    rr.set("0") 

    rbr=Radiobutton(newWindow, text="Do u wish to also open the IDE (default IDE -- Visual Studio Code)",variable=rr, value=22,command=lambda:ideopner(rr.get()),font=("Raleway",10))
    rbr.grid(column=1,row=5)

    def ideopner(value):
             if(value==22):
                 subprocess.Popen('main/Batch Files/OpenVSC.bat')    



root.mainloop()


#Created,implemented and copyrighted Tharun S.M. and Shamse Ahmad
