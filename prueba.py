from tkinter import * 
from tkinter import messagebox
import random

# Funciones
















ventana_principal=Tk()
ventana_principal.geometry("1250x650")
ventana_principal.title("Comparador y Recomendador de Aseguradoras en Colombia", )
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

# Frames e imagenes

frame_superior=Frame(ventana_principal)
frame_superior.config(bg="blue", width=1250, height=170)
frame_superior.place(x=0, y=0)

imagen_1 = PhotoImage(file="Sup.png")
lb_imagen_1= Label(frame_superior, image=imagen_1)
lb_imagen_1.place(x=0, y=0)


frame_izquierdo=Frame(ventana_principal)
frame_izquierdo.config(bg="gray", width=625, height=600)
frame_izquierdo.place(x=0, y=170)

imagen_i = PhotoImage(file="comparar.png")
lb_imagen_i= Label(frame_izquierdo, image=imagen_i)
lb_imagen_i.place(x=0, y=0)


frame_derecho=Frame(ventana_principal)
frame_derecho.config(bg="red", width=625, height=600)
frame_derecho.place(x=625, y=170)




titulo = Label(ventana_principal, text="CYRAC")
titulo.config(bg = "midnight blue",fg="white", font=( "Arial Black", 20,))
titulo.place(x=80,y=30)


#lb_titulo1=Label(ventana_principal, text="Elige una opción:")
#lb_titulo1.config( bg="light blue" , fg="black", bd=5,relief="raised",  font=("new time roma",20))
#lb_titulo1.place(x=80,y=50)


rb_k = Button(ventana_principal, text="Comparar", width=8, height=1, bg="gray80" )
rb_k.config(bg="white", fg="black", font=("Italic", 18))
rb_k.place(x=700, y=30)

# radiobutton para farenheit
rb_f = Button(ventana_principal, text="Recomendar",width=10, height=1, bg="gray80" )
rb_f.config(bg="white", fg="black", font=("Italic", 18))
rb_f.place(x=900, y=30)


ventana_principal.mainloop()