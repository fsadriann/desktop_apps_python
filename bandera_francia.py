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

ventana_principal.geometry("1200x800")

# deshabilitar botón de maximizar

ventana_principal.resizable(False, False)

# color de fondo de la ventana

ventana_principal.config(bg="white")

#------------------------
# frame azul
#------------------------
frame_azul = Frame(ventana_principal)
frame_azul = Frame(bg="navy", width=400, height=800)
frame_azul.place(x=0, y=0)

#------------------------
# frame blanco
#------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco = Frame(bg="white", width=400, height=800)
frame_blanco.place(x=400, y=0)

#------------------------
# frame rojo
#------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo = Frame(bg="red3", width=400, height=800)
frame_rojo.place(x=800, y=0)

# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()