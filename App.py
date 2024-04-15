import customtkinter as ctk
import tkinter as tk
from Machine import Machine

# Configuración global de la apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


# Clase que contiene la interfaz gráfica
class App(ctk.CTk):

    # Constructor
    def __init__(self):
        super().__init__()

        self.inner_machine = Machine()
        self.geometry("1000x600")
        self.title("Codificador")
        self.resizable(False, False)

        self.add_frames()
        self.add_widgets()

    # Agrega los frames a la ventana
    def add_frames(self):
        self.top_frame = ctk.CTkFrame(self, width=925, height=300)
        self.top_frame.pack(pady=(30, 15))
        self.top_frame.pack_propagate(0)

        self.bottom_frame = ctk.CTkFrame(self, width=925, height=200)
        self.bottom_frame.pack(pady=(15, 30))
        self.bottom_frame.pack_propagate(0)
    
    # Agrega los widgets a cada frames
    def add_widgets(self):
        self.title_label = ctk.CTkLabel(self.top_frame, text="Lector de Mensajes", font=("Roboto", 36))
        self.title_label.pack(pady=30, padx=10, expand=False)

        self.entry = ctk.CTkEntry(self.top_frame, placeholder_text="Introduce el texto...", font=("Roboto", 16))
        self.entry.pack(side="left", padx=(30, 0), pady=(0, 30), fill="both", expand=True)

        self.option = ctk.CTkOptionMenu(self.top_frame, values=["Codificar", "Decodificar"], font=("Roboto", 16))
        self.option.pack(side="left", padx=(30, 30), pady=(0,30), expand=False)

        self.button = ctk.CTkButton(self.top_frame, text="Procesar", font=("Roboto", 16))
        self.button.pack(side="right", padx=(0, 30), pady=(0, 30), expand=False)
        self.button.bind("<Button-1>", self.on_click)

        self.subtitle_label = ctk.CTkLabel(self.bottom_frame, text="Resultado:", font=("Roboto", 24))
        self.subtitle_label.pack(pady=30, padx=10, expand=False)

        self.result = ctk.CTkEntry(self.bottom_frame, state="readonly", textvariable=tk.StringVar(), font=("Roboto", 16), width=300)
        self.result.pack(pady=(0, 30), padx=10)

    # Muestra un texto en la parte de resultados
    def show_result(self, text):
        var_result = tk.StringVar()
        var_result.set(text)
        self.result.configure(textvariable=var_result)

    # Añade interactividad al botón
    def on_click(self, event):
        users_input = self.entry.get();

        if self.option.get() == "Codificar":
            encrypted_phrase = self.inner_machine.encrypt_phrase(users_input)
            self.show_result(encrypted_phrase)
            
        if self.option.get() == "Decodificar":
            phrase = self.inner_machine.reveal_phrase(users_input)
            self.show_result(phrase)

    # Corre la vista
    def run(self):
        self.mainloop()
