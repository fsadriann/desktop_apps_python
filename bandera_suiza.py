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

ventana_principal.config(bg="red2")

#------------------------
# frame blanco1
#------------------------
frame_blanco1 = Frame(ventana_principal)
frame_blanco1 = Frame(bg="white", width=300, height=100)
frame_blanco1.place(x=100, y=200)

#------------------------
# frame blanco2
#------------------------
frame_blanco2 = Frame(ventana_principal)
frame_blanco2 = Frame(bg="white", width=100, height=300)
frame_blanco2.place(x=200, y=100)

# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()