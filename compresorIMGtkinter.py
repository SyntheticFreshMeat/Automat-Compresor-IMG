import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button
from PIL import Image
import os

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title="JRC", message="holi"):
        tk.Toplevel.__init__(self, parent)
        self.title(title) # Establece el título de la ventana
        self.geometry("300x200")  # Establece el tamaño de la ventana

        self.label = Label(self, text=message) # Establece el texto de la ventana     
        self.label.pack(pady=10)

        self.button = Button(self, text="CERRAR", command=self.on_ok) # Establece el texto del botón y la función que se ejecutará al hacer clic en el botón
        self.button.pack(pady=10)
        
        
    def on_ok(self):
        self.destroy()
        root.destroy()

def comprimir_imagenes():
    while True:
        carpetaDeImagenes = filedialog.askdirectory(title="Selecciona la carpeta donde se encuentran las imagenes")
        carpetafinal = filedialog.askdirectory(title="Selecciona la carpeta donde se guardarán las imagenes")

        if not os.path.exists(carpetaDeImagenes):
            messagebox.showerror("Error","La ruta a la carpeta de imagenes no existe")
            return
        
        if not os.path.exists(carpetafinal):
            messagebox.showerror("Error","La ruta a la carpeta final no existe")
            return
        
        if carpetaDeImagenes == carpetafinal:
            messagebox.showerror(f"Error","La carpeta de origen no puede ser la misma que la carpeta de destino")
            return

        for nombreimagen in os.listdir(carpetaDeImagenes): # preguntamos por cada imagen en la carpeta
            nombre, extension = os.path.splitext(nombreimagen) # separamos el nombre de la imagen de su extension
            
            if extension in [".jpg", ".jpeg", ".png"]: # preguntamos si la extensión es una de las que queremos comprimir
                try:
                    imagen = Image.open(os.path.join(carpetaDeImagenes, nombreimagen)) # abrimos la imagen
                    imagen.save(os.path.join(carpetafinal, "comprimida_" + nombreimagen), "JPEG", optimize=True, quality=60) # guardamos la imagen comprimida con la palabra "comprimida_" al inicio del nombre
                except Exception as e:
                    messagebox.showwarning(f"Hubo un error al procesar la imagen {nombreimagen}: {e}") # En Python, {e} es una forma de formatear cadenas. En este caso, {e} se reemplazará por el valor de la variable e.
                    CustomDialog(root, title="Gracias por usar mi programa", message="Hasta luego.")
                    
        if messagebox.askyesno("Pregunta", "¿Deseas comprimir más imagenes?"):
            continue
        else:
            CustomDialog(root, title="Información", message="Gracias por usar mi programa.\n\u00AEJRC")         
            break

            
root = tk.Tk()
root.title("Bienvenido a \u00AEJRC")
root.geometry("300x200")
root.resizable(False, False)
root.config(bg="#EB823D")



button = tk.Button(root, text="Comprimir Imagenes", command=comprimir_imagenes)
button.pack()
root.mainloop()