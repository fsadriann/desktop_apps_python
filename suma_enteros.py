#------------------------
#    Desktop app No.1
#------------------------

#se importa la libreria tkinter con todas sus funciones
from tkinter import *

#------------------------
#   funciones de la app
#------------------------

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
titulo.place(x=140, y=10)


#------------------------
# frame operaciones
#------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones = Frame(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#------------------------
# frame resultados
#------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados = Frame(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()