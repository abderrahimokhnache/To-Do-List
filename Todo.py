from tkinter import *

from tkinter.scrolledtext import ScrolledText

from datetime import datetime

from Fileop import File

from Record import Record


root = Tk()

root["bg"] = "#000"

root.geometry("300x550")

root.title('TODO LIST')

# root.iconbitmap('image-86.ico')

root.resizable(0,0)

text_font = ("Consolas italic" , 15  )

btn_font = ("Brush Script MT" ,20 ,'bold')

def Save():

	TL = text.get(0.1 , END)
	
	now = datetime.today()

	Data = str(now.date()) + '\n' + TL 

	File(Path = 'TODO.TL' , Mode = 'a' , Content = Data )

def Delete(event):

	text.delete(1.0, END)	

	

f_line = Label(root  , text = 'TODO LIST' , font = text_font , bg = '#000' , fg = '#fff' )

f_line.place(relx= 0.3 , rely = 0.0)

text = ScrolledText(root, font = text_font ,bg = '#fcfbbe')

text.place(relx= 0.07 , rely = 0.07, relwidth = 0.85 ,relheight = 0.8) 


Save_btn = Button(root ,font = btn_font ,text = 'Save' , bg  = '#333' ,
 command = Save , fg = '#fff' ,cursor= "hand2", relief = 'flat')

Save_btn.place(relx = 0.57 ,rely = 0.9  , relwidth = 0.35,relheight = 0.08)

Record_btn = Button(root ,font = btn_font ,text = 'Record' , bg  = '#333' ,
command = Record , fg = '#fff' ,cursor= "hand2", relief = 'flat')

Record_btn.place(relx = 0.07 ,rely = 0.9  , relwidth = 0.35,relheight = 0.08)

root.bind("<Alt-d>" ,Delete)

root.mainloop()
