# python3 -m pip install Pillow

from PIL import Image # libreria para manejar imagenes
import os # libreria para manejar archivos
import colorama # libreria para darle color a los textos
from colorama import Fore, Style

colorama.init() # inicializamos colorama

while True:
    try:
        carpetaDeImagenes = input("Introduce la ruta de la carpeta donde se encuentran las imagenes: ") # carpeta donde se encuentran las imagenes
        carpetafinal = input("Introduce la ruta de la carpeta donde se guardarán las imagenes: ") # carpeta donde se guardaran las imagenes comprimidas

        if not os.path.exists(carpetaDeImagenes):
            print(f"{Fore.RED}La ruta a la carpeta {carpetaDeImagenes} no existe{Style.RESET_ALL}")
            continue
    
        if not os.path.exists(carpetafinal):
            print(f"{Fore.CYAN}La ruta a la carpeta {carpetafinal} no existe{Style.RESET_ALL}")
            continue
        
        if carpetaDeImagenes == carpetafinal:
            print(f"{Fore.BLUE}La carpeta de origen no puede ser la misma que la carpeta de destino{Style.RESET_ALL}")
            continue

    except Exception as e:
        print(f"{Fore.GREEN}Por favor, asegurese de introducir las rutas correctamente a las carpetas: {e}{Style.RESET_ALL}")
        continue

    break

if __name__ == "__main__":
    for nombreimagen in os.listdir(carpetaDeImagenes): # preguntamos por cada imagen en la carpeta
        nombre, extension = os.path.splitext(nombreimagen) # separamos el nombre de la imagen de su extension
        
        if extension in [".jpg", ".jpeg", ".png"]: # preguntamos si la extensión es una de las que queremos comprimir
            try:
                imagen = Image.open(os.path.join(carpetaDeImagenes, nombreimagen)) # abrimos la imagen
                imagen.save(os.path.join(carpetafinal, "comprimida_" + nombreimagen), "JPEG", optimize=True, quality=60) # guardamos la imagen comprimida con la palabra "comprimida_" al inicio del nombre
            except Exception as e:
                print(f"{Fore.CYAN}{nombreimagen}{Fore.GREEN} no se ha podido procesar: {Fore.RED}{e}{Style.RESET_ALL}") # En Python, {e} es una forma de formatear cadenas. En este caso, {e} se reemplazará por el valor de la variable e.
                print(f"{Fore.GREEN}gracias por usar mi programa.{Style.RESET_ALL}")
                
    print(f"{Fore.GREEN}Proceso de compresión finalizado Gracias por usar mi programa.\n\u00AEJRC{Style.RESET_ALL}")