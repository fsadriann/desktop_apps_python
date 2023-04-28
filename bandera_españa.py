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
# frame rojo
#------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo = Frame(bg="red3", width=1200, height=200)
frame_rojo.place(x=0, y=0)

#------------------------
# frame amarillo
#------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo = Frame(bg="yellow", width=1200, height=400)
frame_amarillo.place(x=0, y=200)

#------------------------
# frame rojo
#------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo = Frame(bg="red3", width=1200, height=210)
frame_rojo.place(x=0, y=500)

#------------------------
# frame escudo
#------------------------
frame_escudo = Frame(ventana_principal)
frame_escudo = Frame(bg="red3", width=200, height=200)
frame_escudo.place(x=200, y=250)

#------------------------
# frame escudo
#------------------------
frame_escudo = Frame(ventana_principal)
frame_escudo = Frame(bg="white", width=50, height=200)
frame_escudo.place(x=200, y=250)

#------------------------
# frame escudo
#------------------------
frame_escudo = Frame(ventana_principal)
frame_escudo = Frame(bg="white", width=50, height=200)
frame_escudo.place(x=400, y=250)

#------------------------
# frame escudo_amarillo
#------------------------
frame_escudo = Frame(ventana_principal)
frame_escudo = Frame(bg="yellow", width=10, height=200)
frame_escudo.place(x=250, y=250)

#------------------------
# frame escudo_amarillo
#------------------------
frame_escudo = Frame(ventana_principal)
frame_escudo = Frame(bg="yellow", width=10, height=200)
frame_escudo.place(x=390, y=250)


# run
# se ejecuta el método mainloop() de la clase Tk() a través de la instancia ventana_principal. Este método despliega la ventana de la app en pantalla y queda a la espera de lo que el usuario haga. (clic en un botón, etc). cada acción del usuario se conoce como evento. el método mainloop() es un bucle infinito.
ventana_principal.mainloop()