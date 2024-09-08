from tkinter import *
def mostrarLabel():
   lbl = Label(ventana, text="Hola mundo!", font=("Comic Sans", 13, "bold"))
   lbl.pack()
def aumentarPuntaje(puntaje):
   puntaje += 50
   puntos.pack()
ventana = Tk()
ventana.geometry("1280x720")
ventana.title("Hola mundo")
ventana.config(bg="lightblue", bd=10)
ventana.resizable(0,0)
puntaje = 0
puntos = Label(ventana, text=f"{puntaje}", font=("Comic Sans", 13, "bold"))
puntos.pack()
btn = Button(ventana, text="Aumentar puntaje", command = aumentarPuntaje(puntaje), background="blue", foreground="white")
btn.pack()
ventana.mainloop()