from tkinter import *

from Fileop import File

text_font = ("Consolas italic" , 15  )

btn_font = ("Brush Script MT" ,20 ,'bold')

def Record():
	
	def Clear():
	
		File(Path = 'TODO.TL' , Mode = 'wb' , Content = " " )

		for item in range(0,2) :
			
			List_box.delete(item)
	

	root2 = Tk()

	root2["bg"] = "#000"

	root2.geometry("300x550")

	root2.title('TODO LIST')

	# root2.iconbitmap('image-86.ico')


	root2.resizable(0,0)

	List_box = Listbox(root2 ,font = text_font,bg = '#fcfbbe')

	List_box.place(relx= 0.07 , rely = 0.07, relwidth = 0.85 ,relheight = 0.8)

	Clear_btn = Button(root2 ,font = btn_font ,text = 'Clear' , bg  = '#333' ,
	
	command = Clear , fg = '#fff' ,cursor= "hand2", relief = 'flat')

	Clear_btn.place(relx = 0.35 ,rely = 0.9  , relwidth = 0.35,relheight = 0.08)

	with open("TODO.TL" , 'rb') as file :

		Data = file.readlines()
	
	for i , line in enumerate(Data) :

		List_box.insert( i , line )
