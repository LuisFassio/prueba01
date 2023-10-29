import tkinter as tk
import pytube

root = tk.Tk()

# Entrada para el enlace del video
link_entry = tk.Entry(root)
link_entry.pack()

# Botón para descargar el video
download_button = tk.Button(root, text="Descargar", command=lambda: download_video(link_entry.get()))
download_button.pack()

def download_video(link):
    # Obtener el video de YouTube
    video = pytube.YouTube(link)

    # Descargar el video
    video.streams.first().download()

    print("El video se ha descargado con éxito.")

root.mainloop()
