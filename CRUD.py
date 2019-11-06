from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


# Raiz del Programa

raiz = Tk()

raiz.title("CRUD")


# Programa Principal

framePrincipal = Frame(raiz, height=360, width=260)
framePrincipal.pack()

# STRING CREADOS

id = StringVar()
nombre_usuario = StringVar()
passw = StringVar()
apellido = StringVar()
direccion = StringVar()

# Funciones


def conectarBasedeDatos():

    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))''')

        messagebox.showinfo("Crear Base de Datos",
                            "La Base de datos se ha creada Correctamente.")
    except:
        messagebox.showwarning("Crear Base de Datos", "La Base de datos ya ah sido creada.")


def crearNuevoDato():
    nuevo = [(nombre_usuario.get(), passw.get(), apellido.get(),
              direccion.get(), entryText.get(1.0, END))]
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()
    cursor.executemany(
        "INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)", nuevo)

    conexion.commit()
    messagebox.showinfo("Base de Datos", "Un nuevo Perfil se ah creado correctamente.")
    conexion.close()


def leerDatos():
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + id.get())

    elUsuario = cursor.fetchall()

    for usuario in elUsuario:
        id.set(usuario[0])
        nombre_usuario.set(usuario[1])
        passw.set(usuario[2])
        apellido.set(usuario[3])
        direccion.set(usuario[4])
        entryText.insert(1.0, usuario[5])

    conexion.commit()


def actualizarDatos():
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()

    cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + nombre_usuario.get() +
                   "',PASSWORD='" + passw.get() +
                   "',APELLIDO='" + apellido.get() +
                   "',DIRECCION='" + direccion.get() +
                   "',COMENTARIOS='" + entryText.get("1.0", END) +
                   "'WHERE ID=" + id.get())
    conexion.commit()
    messagebox.showinfo("Base de Datos", "Perfil Actualizado con Exito")


def borrarDatos():
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + id.get())
    messagebox.showinfo("Base de Datos", "El perfil se borro correctamente.")
    conexion.commit()


def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Esta Seguro que desea Salir?")

    if valor == "yes":

        raiz.destroy()


def borrarCampos():
    id.set("")
    nombre_usuario.set("")
    passw.set("")
    apellido.set("")
    direccion.set("")
    entryText.delete(1.0, END)


def avisoLicencia():
    messagebox.showinfo("Licencia CRUD", "LICENCIA BAJO GNU LIBRE")


def avisoSobremi():
    messagebox.showinfo("CRUD", "Programa Diseñado por German Rojas")


# Barra Menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

# Menu Conexion y Salir
base_Menu = Menu(barraMenu, tearoff=0)  # tearoff borra la linea en el menu
barraMenu.add_cascade(label="BBDD", menu=base_Menu)
base_Menu.add_command(label="Conectar", command=lambda: conectarBasedeDatos())
base_Menu.add_command(label="Salir", command=lambda: salirAplicacion())

# Menu BorrarCampos
base_Menu = Menu(barraMenu, tearoff=0)  # tearoff borra la linea en el menu
barraMenu.add_cascade(label="Borrar", menu=base_Menu)
base_Menu.add_command(label="Borrar Campos", command=lambda: borrarCampos())

# Menu CRUD
base_Menu = Menu(barraMenu, tearoff=0)  # tearoff borra la linea en el menu
barraMenu.add_cascade(label="CRUD", menu=base_Menu)
base_Menu.add_command(label="Crear", command=lambda: crearNuevoDato())
base_Menu.add_command(label="Leer", command=lambda: leerDatos())
base_Menu.add_command(label="Actualizar", command=lambda: actualizarDatos())
base_Menu.add_command(label="Borrar", command=lambda: borrarDatos())

# Menu Ayuda
base_Menu = Menu(barraMenu, tearoff=0)  # tearoff borra la linea en el menu
barraMenu.add_cascade(label="Ayuda", menu=base_Menu)
base_Menu.add_command(label="Licencia", command=lambda: avisoLicencia())
base_Menu.add_command(label="Acerca de..", command=lambda: avisoSobremi())

# Cuadro ID

labelID = Label(framePrincipal, text="ID:")
labelID.grid(row=0, column=0, padx=10, pady=10)

entryID = Entry(framePrincipal, textvariable=id)
entryID.grid(row=0, column=1, padx=10, pady=10)


# Cuadro Nombre

labelNombre = Label(framePrincipal, text="Nombre:")
labelNombre.grid(row=1, column=0, padx=10, pady=10)

entryNombre = Entry(framePrincipal, textvariable=nombre_usuario)
entryNombre.grid(row=1, column=1, padx=10, pady=10)


# Cuadro Pass

labelPass = Label(framePrincipal, text="Contraseña: ")
labelPass.grid(row=2, column=0, padx=10, pady=10)

entryPass = Entry(framePrincipal, textvariable=passw, show="*")
entryPass.grid(row=2, column=1, padx=10, pady=10)


# Cuadro Apellido

labelApellido = Label(framePrincipal, text="Apellido: ")
labelApellido.grid(row=3, column=0, padx=10, pady=10)

entryApellido = Entry(framePrincipal, textvariable=apellido)
entryApellido.grid(row=3, column=1, padx=10, pady=10)


# Cuadro Direccion

labelDireccion = Label(framePrincipal, text="Direccion: ")
labelDireccion.grid(row=4, column=0, padx=10, pady=10)

entryDireccion = Entry(framePrincipal, textvariable=direccion)
entryDireccion.grid(row=4, column=1, padx=10, pady=10)

# Cuadro Comentario

labelComent = Label(framePrincipal, text="Comentario: ")
labelComent.grid(row=5, column=0, padx=10, pady=10)

entryText = Text(framePrincipal, height=7, width=15,)
entryText.grid(row=5, column=1, padx=10, pady=10)

barraScroll = Scrollbar(framePrincipal, command=entryText.yview)
barraScroll.grid(row=5, column=2, sticky="nsew")
entryText.config(yscrollcommand=barraScroll.set)


# Botones


botonCreate = Button(framePrincipal, text="Crear", command=lambda: crearNuevoDato())
botonCreate.grid(row=6, column=0, padx=10, pady=10, sticky="w")

botonRead = Button(framePrincipal, text="Leer", command=lambda: leerDatos())
botonRead.grid(row=6, column=0, sticky="e", padx=5, pady=10)

botonActualizar = Button(framePrincipal, text="Actualizar", command=lambda: actualizarDatos())
botonActualizar.grid(row=6, column=1, sticky="w")

botonBorrar = Button(framePrincipal, text="Borrar", command=lambda: borrarDatos())
botonBorrar.grid(row=6, column=1, padx=70, pady=10)


raiz.mainloop()
