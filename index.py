from tkinter import *

ventana = Tk()
menu = Menu(ventana)
ventana.config(menu=menu)

File=Menu(menu, tearoff=0)
File.add_command(label='new proyect')
Edit=Menu(menu, tearoff=0)
Help=Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu =File)
menu.add_cascade(label="Edit", menu =Edit)
menu.add_cascade(label="Help", menu =Help)

ventana.title('hola')
ventana.mainloop()
