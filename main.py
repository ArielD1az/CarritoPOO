import tkinter as tk
from tkinter import ttk, messagebox
from carrito import deposito, carrito, buscar


def actualizar_tabla_deposito():
    tabla_deposito.delete(*tabla_deposito.get_children())
    for prod in deposito:
        tabla_deposito.insert("", "end", values=(prod.nombre, prod.precio, prod.stock))

def actualizar_tabla_carrito():
    tabla_carrito.delete(*tabla_carrito.get_children())
    for i, item in enumerate(carrito.productos):
        datos = carrito.mostrarProducto(i)
        tabla_carrito.insert("", "end", values=(datos[0], datos[1], datos[2], datos[3]))
    label_total.config(text=f"Total: ${carrito.total:.2f}")

def agregar_producto():
    nombre = combo_productos.get().strip()
    cantidad_txt = entrada_cantidad.get().strip()

    if not nombre or not cantidad_txt.isdigit():
        messagebox.showwarning("Error", "Seleccione un producto y una cantidad válida")
        return

    cantidad = int(cantidad_txt)
    prod = buscar(nombre, deposito)

    if not prod:
        messagebox.showerror("Error", "Producto inexistente")
        return

    if carrito.agregarProducto(prod, cantidad):
        actualizar_tabla_deposito()
        actualizar_tabla_carrito()
        combo_productos.set("Seleccioná un producto")
        entrada_cantidad.delete(0, tk.END)
    else:
        messagebox.showerror("Stock insuficiente", f"Solo hay {prod.stock} unidades disponibles.")

def eliminar_producto():
    seleccionado = tabla_carrito.focus()
    if not seleccionado:
        messagebox.showwarning("Error", "Seleccione un producto del carrito para eliminar")
        return

    valores = tabla_carrito.item(seleccionado, "values")
    nombre = valores[0]
    prod = buscar(nombre, deposito)

    if carrito.eliminarProducto(prod):
        actualizar_tabla_carrito()
        actualizar_tabla_deposito()
    else:
        messagebox.showinfo("Info", "El producto no está en el carrito")

def vaciar_carrito():
    if messagebox.askyesno("Confirmar", "¿Seguro que desea vaciar el carrito?"):
        carrito.vaciarCarrito()
        actualizar_tabla_carrito()
        actualizar_tabla_deposito()



ventana = tk.Tk()
ventana.title("Carrito de Compras")
ventana.iconbitmap("icon.ico")
ventana.geometry("800x600")
ventana.resizable(False, False)
ventana.config(bg="#f5f5f5")


frame_deposito = tk.LabelFrame(ventana, text="Productos disponibles", padx=10, pady=10, bg="#f5f5f5")
frame_deposito.pack(fill="x", padx=20, pady=10)

tabla_deposito = ttk.Treeview(frame_deposito, columns=("nombre", "precio", "stock"), show="headings", height=5)
tabla_deposito.heading("nombre", text="Nombre")
tabla_deposito.heading("precio", text="Precio")
tabla_deposito.heading("stock", text="Stock")
tabla_deposito.pack(fill="x")


frame_agregar = tk.LabelFrame(ventana, text="Agregar producto al carrito", padx=10, pady=10, bg="#f5f5f5")
frame_agregar.pack(fill="x", padx=20, pady=10)

tk.Label(frame_agregar, text="Producto:", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)


combo_productos = ttk.Combobox(frame_agregar, values=[p.nombre for p in deposito], state="readonly", width=23)
combo_productos.set("Seleccioná un producto")
combo_productos.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_agregar, text="Cantidad:", bg="#f5f5f5").grid(row=0, column=2, padx=5, pady=5)
entrada_cantidad = tk.Entry(frame_agregar, width=10)
entrada_cantidad.grid(row=0, column=3, padx=5, pady=5)

boton_agregar = tk.Button(frame_agregar, text="Agregar al carrito", bg="#4CAF50", fg="white", command=agregar_producto)
boton_agregar.grid(row=0, column=4, padx=10)


frame_carrito = tk.LabelFrame(ventana, text="Carrito de compras", padx=10, pady=10, bg="#f5f5f5")
frame_carrito.pack(fill="both", expand=True, padx=20, pady=10)

tabla_carrito = ttk.Treeview(frame_carrito, columns=("nombre", "precio", "cantidad", "subtotal"), show="headings", height=8)
tabla_carrito.heading("nombre", text="Nombre")
tabla_carrito.heading("precio", text="Precio")
tabla_carrito.heading("cantidad", text="Cantidad")
tabla_carrito.heading("subtotal", text="Subtotal")
tabla_carrito.pack(fill="both", expand=True)


frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(fill="x", padx=20, pady=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar producto", bg="#f44336", fg="white", command=eliminar_producto)
boton_eliminar.pack(side="left", padx=10)

boton_vaciar = tk.Button(frame_botones, text="Vaciar carrito", bg="#ff9800", fg="white", command=vaciar_carrito)
boton_vaciar.pack(side="left", padx=10)

label_total = tk.Label(frame_botones, text="Total: $0.00", font=("Arial", 12, "bold"), bg="#f5f5f5")
label_total.pack(side="right", padx=20)


actualizar_tabla_deposito()
actualizar_tabla_carrito()

ventana.mainloop()
