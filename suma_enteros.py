#------------------------
#    Desktop app No.1
#------------------------

#se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#------------------------
#   funciones de la app
#------------------------

# sumar
def sumar():
    pass

# borrar
def borrar():
    pass

# salir
def salir():
    messagebox.showinfo("Suma Enteros 1.0", "La app se cerrará")
    ventana_principal.destroy()

#------------------------------
# ventana principal de la app
#------------------------------


# se declara una variable llamada ventana_principal, que adquiere las propiedades de un objeto Tk
ventana_principal = Tk()

# titulo de la ventana

ventana_principal.title("bandera de colombia")

# tamaño de la ventana

ventana_principal.geometry("500x500")

# deshabilitar botón de maximizar

ventana_principal.resizable(False, False)

# color de fondo de la ventana

ventana_principal.config(bg="navy")

#------------------------
# frame entrada datos
#------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada = Frame(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=40)

# titulo de la app
titulo=Label(frame_entrada, text="Suma de enteros 1.0")
titulo.config(font=("Arial", 16), bg="white", fg="navy")
titulo.place(x=240, y=10)

# etiqueta para el valor de x
lb_x = Label(frame_entrada, text="X = ")
lb_x.config(font=("Arial", 16), bg="white", fg="navy")
lb_x.place(x=240, y=60)

# caja de texto para x
Entry_x = Entry(frame_entrada)
Entry_x.config(font=("Arial", 16), bg="white", fg="navy",)
Entry_x.focus_set()
Entry_x.place(x=280, y=60, width=100)

# etiqueta para el valor de y
lb_y = Label(frame_entrada, text="Y = ")
lb_y.config(font=("Arial", 16), bg="white", fg="navy")
lb_y.place(x=240, y=100)

# caja de texto para y
Entry_y = Entry(frame_entrada)
Entry_y.config(font=("Arial", 16), bg="white", fg="navy")
Entry_y.place(x=280, y=100, width=100)

#------------------------
# frame operaciones
#------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones = Frame(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
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

#------------------------
# frame resultados
#------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados = Frame(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(font=("Courier", 20), bg="black", fg="green yellow")
t_resultados.place(x=10, y=10, width=460, height=160)

# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()