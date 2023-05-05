#------------------------
#    Desktop app No.1
#------------------------

#se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#------------------------
#   funciones de la app
#------------------------

#sumar
def calcular():
    messagebox.showinfo("minicalculadora 1.0", "las operaciones han sido realizadas")
    s = int(x.get()) + int(y.get())
    r = int(x.get()) - int(y.get())
    m = int(x.get()) * int(y.get())
    d = int(x.get()) / int(y.get())
    de = int(x.get()) // int(y.get())
    mod = int(x.get()) % int(y.get())
    p = int(x.get()) ** int(y.get())
    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} % {int(y.get())} = {mod}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} ** {int(y.get())} = {p}")
    
    
    
#borrar
def borrar():
    messagebox.showinfo("minicalculadora 1.0", "los datosseran borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0", "end")
    

#salir
def salir():
    messagebox.showinfo("mini calculadora 1.0", "la app se va a cerrar")
    ventana_principal.destroy()


#Ventana principal de la app


#Se declara una ventana llamada ventana_principal, que adquiere las caracteristicas de un objeto TK()
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("minicalculadora 1.0")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Desabilitar el boton de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="navy")


#---------------------------
# variables globales
#---------------------------

x = StringVar()
y = StringVar()

#-----------------------------------
# Entrada datos
#-----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=40)

# titulo de la app
titulo=Label(frame_entrada, text="Mini calculadora 1.0")
titulo.config(font=("Arial", 16), bg="white", fg="navy")
titulo.place(x=240, y=10)

#etiqueta para el valor de x
lb_x=Label(frame_entrada, text= "X =")
lb_x.config(bg="white", fg="navy", font=("helvetica", 20))
lb_x.place(x=240, y=60)

#caja de texto para el valor x
entry_x=Entry(frame_entrada, textvariable=x)
entry_x.config(bg="white", fg="navy", font=("Helvetica", 18),width=6)
entry_x.focus_set()
entry_x.place(x=290, y=60)

#etiqueta para el valor de y
lb_y=Label(frame_entrada, text= "Y =")
lb_y.config(bg="white", fg="navy", font=("helvetica", 20))
lb_y.place(x=240, y=120)

#caja de texto para el valor y
entry_y=Entry(frame_entrada, textvariable=y)
entry_y.config(bg="white", fg="navy", font=("helvetica", 18),width=6)
entry_y.focus_set()
entry_y.place(x=290, y=120)

#----------------------------------
# frame operaciones
#-----------------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)


# boton para calcular
bt_sumar = Button(frame_operaciones, text="Calcular", command=calcular)
bt_sumar.config(font=("Arial", 16), bg="white", fg="navy")
bt_sumar.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.config(font=("Arial", 16), bg="white", fg="navy")
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.config(font=("Arial", 16), bg="white", fg="navy")
bt_salir.place(x=335, y=35, width=100, height=30)

#-----------------------------------
# frame resultados
#-----------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

#area de texto para los resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow",font=("courier",18))
t_resultados.place(x=10, y=10, width=460, height=160)

# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()