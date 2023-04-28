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

ventana_principal.config(bg="red3")

#------------------------
# frame blanco1
#------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco = Frame(bg="white", width=120, height=800)
frame_blanco.place(x=300, y=0)

#------------------------
# frame blanco2
#------------------------
frame_blanco2 = Frame(ventana_principal)
frame_blanco2 = Frame(bg="white", width=1200, height=120)
frame_blanco2.place(x=0, y=300)

#------------------------
# frame azul1
#------------------------
frame_azul1 = Frame(ventana_principal)
frame_azul1 = Frame(bg="navy", width=63, height=800)
frame_azul1.place(x=327, y=0)

#------------------------
# frame azul2
#------------------------
frame_azul2 = Frame(ventana_principal)
frame_azul2 = Frame(bg="navy", width=1200, height=63)
frame_azul2.place(x=0, y=327)

# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()