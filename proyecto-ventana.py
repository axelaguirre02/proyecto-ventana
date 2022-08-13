# Importe del paquete "Tkinter" y el componente "ttk"
from tkinter import *
from tkinter import ttk


# Ventana y sus atributos
ventana = Tk()
ventana.title('Proyecto con Tkinter | Master en Python')
ventana.geometry('412x400')


# Opciones y autor
home_label = Label(ventana, text= 'Inicio')
add_label = Label(ventana, text= 'Añadir producto')
info_label = Label(ventana, text= 'Informacion')
autor = Label(ventana, text= 'Creado por Axel Aguirre | 2022')
# -------------------------------------------------------------- #
Label(ventana).grid(row= 1)
cajaDeProductos = ttk.Treeview(height= 10, columns= 2)
cajaDeProductos.grid(row= 1, column= 0, columnspan= 2)
cajaDeProductos.heading('#0', text= 'Producto', anchor= W)
cajaDeProductos.heading('#1', text= 'Precio', anchor= W)

# Configuracion de las "Opciones" 

# Opcion "Inicio"
def home():
    home_label.config(
        foreground= 'white',
        background= 'pink',
        font= ('Arial', 30),
        padx= 160,
        pady= 10
    )
    home_label.grid(row= 0, column= 0)

    cajaDeProductos.grid(row= 2)
 
    for producto in productos:
        if len(producto) == 3:
            producto.append('añadido')
            cajaDeProductos.insert('', 0, text= producto[0], values= (producto[1]))

    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    autor.grid_remove()

# Opcion "Añadir"
def add():
    add_label.config(
        foreground= 'white',
        background= 'green',
        font= ('Arial', 30),
        padx= 65,
        pady= 10
    )
    add_label.grid(row= 0, column= 0, columnspan= 10)

    # Posicion del "Marco"
    add_frame.grid(row= 1)

    # Posicion del "Nombre"
    add_name_label.grid(row= 1, column= 0, padx= 5, pady= 5, sticky= W)
    add_name_entry.grid(row=1, column= 1, padx= 5, pady= 5, sticky= W)

    # Posicion del "Precio"
    add_price_label.grid(row= 2, column= 0, padx= 5, pady= 5, sticky= W)
    add_price_entry.grid(row= 2, column= 1, padx= 5, pady= 5, sticky= W)

    # Posicion y configuracion de la "Descripcion"
    add_description_label.grid(row= 3, column= 0, padx= 5, pady= 5, sticky= NW)
    add_description_entry.grid(row=3, column= 1, padx= 5, pady= 5, sticky= W)
    add_description_entry.config(
        width= 38,
        height= 8
    )

    # Posicion y configuracion del "Boton"
    boton.grid(row= 5, column= 1, sticky= N)
    boton.config(
        background= 'green',
        foreground= 'white',
        padx= 10
    )

    home_label.grid_remove()
    info_label.grid_remove()
    cajaDeProductos.grid_remove()
    autor.grid_remove()

# Opcion "Informacion"
def info():
    info_label.config(
        foreground= 'white',
        background= 'blue',
        font= ('Arial', 30),
        padx= 103,
        pady= 10
    )
    info_label.grid(row= 0, column= 0)
    autor.grid(row= 1, column= 0)

    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    cajaDeProductos.grid_remove()

# Metodo para agregar un producto
def agregarProducto():
    productos.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get('1.0', 'end-1c')
    ])

    name_data.set(''),
    price_data.set(''),
    add_description_entry.delete('1.0', END)

    home()


# Menu 
menu_superior = Menu(ventana)
menu_superior.add_command(label= 'Inicio', command= home)
menu_superior.add_command(label= 'Añadir', command= add)
menu_superior.add_command(label= 'Informacion', command= info)
menu_superior.add_command(label= 'Salir', command= ventana.quit)


# Formulario 

# Variables de texto
productos = []
name_data = StringVar()
price_data = StringVar()

# Marco del formulario
add_frame = Frame(ventana)

# Nombre
add_name_label = Label(add_frame, text= 'Nombre:')
add_name_entry = Entry(add_frame, textvariable= name_data)

# Precio
add_price_label = Label(add_frame, text= 'Precio:')
add_price_entry = Entry(add_frame, textvariable= price_data)

# Descripcion
add_description_label = Label(add_frame, text= 'Descripcion:')
add_description_entry = Text(add_frame)

# Boton
boton = Button(add_frame, text= 'Guardar', command= agregarProducto)
 

# Comandos para las ejecuciones 
home()
ventana.config(menu= menu_superior)
ventana.mainloop()











