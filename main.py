import customtkinter as ctk
from gui.nivel3_dfa import Nivel3Window
from gui.nivel2_pda import Nivel2Window
from gui.nivel1_lba import Nivel1Window
from gui.nivel0_tm import Nivel0Window

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SimuladorChomskyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simulador de la Jerarquía de Chomsky | Camilo Rodríguez")
        self.geometry("980x620")
        self.resizable(False, False)
        self.configure(fg_color="#0F172A")

        self.ventana_activa = None
        self._construir_interfaz()

    def _construir_interfaz(self):
        header = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=12)
        header.pack(fill="x", padx=28, pady=(24, 14))

        ctk.CTkLabel(
            header,
            text="SIMULADOR COMPUTACIONAL: JERARQUÍA DE CHOMSKY",
            font=("Segoe UI", 22, "bold"),
            text_color="#38BDF8"
        ).pack(pady=(16, 4))

        ctk.CTkLabel(
            header,
            text="Visualización paso a paso de autómatas y gramáticas formales (Tipos 3, 2, 1 y 0)",
            font=("Segoe UI", 13),
            text_color="#CBD5E1"
        ).pack(pady=(0, 14))

        grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True, padx=28, pady=6)
        grid_frame.grid_columnconfigure((0, 1), weight=1)
        grid_frame.grid_rowconfigure((0, 1), weight=1)

        modulos = [
            {
                "row": 0, "col": 0,
                "badge": "TIPO 3 • LENGUAJES REGULARES",
                "titulo": "Autómata Finito Determinista (AFD)",
                "desc": "Reconocimiento símbolo a símbolo para L = { w ∈ {0,1}* | w termina en '01' }.\nVisualiza conjunto de estados Q y estado activo.",
                "color": "#0284C7", "hover": "#0369A1",
                "cmd": lambda: self._abrir_modulo(Nivel3Window)
            },
            {
                "row": 0, "col": 1,
                "badge": "TIPO 2 • LIBRES DE CONTEXTO",
                "titulo": "Autómata de Pila (PDA - Memoria LIFO)",
                "desc": "Reconocimiento de palíndromos con marcador L = { w c w^R | w ∈ {a,b}* }.\nAnimación dinámica de operaciones Push y Pop en la pila.",
                "color": "#0D9488", "hover": "#0F766E",
                "cmd": lambda: self._abrir_modulo(Nivel2Window)
            },
            {
                "row": 1, "col": 0,
                "badge": "TIPO 1 • SENSIBLES AL CONTEXTO",
                "titulo": "Autómata Linealmente Acotado (LBA)",
                "desc": "Reconocimiento de L = { 0^n 1^n 2^n | n ≥ 1 } en memoria acotada.\nCinta con delimitadores de frontera [ ] y cabezal bidireccional.",
                "color": "#7C3AED", "hover": "#6D28D9",
                "cmd": lambda: self._abrir_modulo(Nivel1Window)
            },
            {
                "row": 1, "col": 1,
                "badge": "TIPO 0 • RECURSIVAMENTE ENUMERABLES",
                "titulo": "Máquina de Turing (MT)",
                "desc": "Cálculo de Complemento a Uno Binario sobre {0,1}+.\nCinta dinámicamente expansible (⊔), alfabeto Γ y cabezal L/E.",
                "color": "#D97706", "hover": "#B45309",
                "cmd": lambda: self._abrir_modulo(Nivel0Window)
            }
        ]

        for m in modulos:
            card = ctk.CTkFrame(grid_frame, fg_color="#1E293B", corner_radius=12, border_width=1, border_color="#334155")
            card.grid(row=m["row"], column=m["col"], padx=10, pady=10, sticky="nsew")

            ctk.CTkLabel(
                card, text=m["badge"], font=("Segoe UI", 11, "bold"), text_color="#38BDF8"
            ).pack(anchor="w", padx=18, pady=(16, 2))

            ctk.CTkLabel(
                card, text=m["titulo"], font=("Segoe UI", 17, "bold"), text_color="#F8FAFC"
            ).pack(anchor="w", padx=18, pady=(0, 8))

            ctk.CTkLabel(
                card, text=m["desc"], font=("Segoe UI", 12), text_color="#94A3B8", justify="left"
            ).pack(anchor="w", padx=18, pady=(0, 14))

            ctk.CTkButton(
                card, text="Abrir Simulador →", height=36,
                fg_color=m["color"], hover_color=m["hover"],
                font=("Segoe UI", 13, "bold"), command=m["cmd"]
            ).pack(side="bottom", fill="x", padx=18, pady=16)

        footer = ctk.CTkFrame(self, fg_color="transparent")
        footer.pack(fill="x", padx=28, pady=(4, 14))
        ctk.CTkLabel(
            footer,
            text="Desarrollado por: Camilo Rodríguez  |  Teoría de la Computación y Lenguajes Formales",
            font=("Segoe UI", 12),
            text_color="#64748B"
        ).pack()

    def _abrir_modulo(self, clase_ventana):
        if self.ventana_activa is None or not self.ventana_activa.winfo_exists():
            self.ventana_activa = clase_ventana(self)
            self.ventana_activa.grab_set()
        else:
            self.ventana_activa.focus()


if __name__ == "__main__":
    app = SimuladorChomskyApp()
    app.mainloop()
        
            

           
