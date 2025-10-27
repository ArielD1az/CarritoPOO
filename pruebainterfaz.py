import tkinter as tk
from tkinter import ttk, messagebox

# ----- Ventana principal -----
ventana = tk.Tk()
ventana.title("🛒 Carrito de Compras")
ventana.geometry("800x600")
ventana.config(bg="#f5f5f5")

# ----- Frame superior: Productos en depósito -----
frame_deposito = tk.LabelFrame(ventana, text="📦 Productos disponibles", padx=10, pady=10, bg="#f5f5f5")
frame_deposito.pack(fill="x", padx=20, pady=10)

tabla_deposito = ttk.Treeview(frame_deposito, columns=("precio", "stock"), show="headings", height=5)
tabla_deposito.heading("precio", text="Precio")
tabla_deposito.heading("stock", text="Stock")
tabla_deposito.insert("", "end", values=("Ejemplo: Manzana", "100", "10"))  # Ejemplo de fila
tabla_deposito.pack(fill="x")

# ----- Frame central: Agregar al carrito -----
frame_agregar = tk.LabelFrame(ventana, text="➕ Agregar producto al carrito", padx=10, pady=10, bg="#f5f5f5")
frame_agregar.pack(fill="x", padx=20, pady=10)

tk.Label(frame_agregar, text="Nombre del producto:", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
entrada_nombre = tk.Entry(frame_agregar, width=25)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_agregar, text="Cantidad:", bg="#f5f5f5").grid(row=0, column=2, padx=5, pady=5)
entrada_cantidad = tk.Entry(frame_agregar, width=10)
entrada_cantidad.grid(row=0, column=3, padx=5, pady=5)

boton_agregar = tk.Button(frame_agregar, text="Agregar al carrito", bg="#4CAF50", fg="white")
boton_agregar.grid(row=0, column=4, padx=10)

# ----- Frame inferior: Carrito -----
frame_carrito = tk.LabelFrame(ventana, text="🛍️ Carrito de compras", padx=10, pady=10, bg="#f5f5f5")
frame_carrito.pack(fill="both", expand=True, padx=20, pady=10)

tabla_carrito = ttk.Treeview(frame_carrito, columns=("precio", "cantidad", "subtotal"), show="headings", height=8)
tabla_carrito.heading("precio", text="Precio")
tabla_carrito.heading("cantidad", text="Cantidad")
tabla_carrito.heading("subtotal", text="Subtotal")
tabla_carrito.pack(fill="both", expand=True)

# ----- Frame de botones -----
frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(fill="x", padx=20, pady=10)

boton_eliminar = tk.Button(frame_botones, text="❌ Eliminar producto", bg="#f44336", fg="white")
boton_eliminar.pack(side="left", padx=10)

boton_vaciar = tk.Button(frame_botones, text="🧹 Vaciar carrito", bg="#ff9800", fg="white")
boton_vaciar.pack(side="left", padx=10)

label_total = tk.Label(frame_botones, text="Total: $0.00", font=("Arial", 12, "bold"), bg="#f5f5f5")
label_total.pack(side="right", padx=20)

# ----- Mainloop -----
ventana.mainloop()
