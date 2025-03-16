import tkinter as tk
from tkinter import messagebox
#crear ventana
root = tk.Tk()
root.withdraw()
def mostrar_alerta():
    messagebox.showinfo('noti','hola')
mostrar_alerta()
