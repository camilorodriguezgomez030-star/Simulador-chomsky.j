import customtkinter as ctk
from models.lba import AutomataLinealAcotado


class Nivel1Window(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Nivel 1 - Autómata Linealmente Acotado (LBA) | Camilo Rodríguez")
        self.geometry("1080x540")
        self.configure(fg_color="#0F172A")

        self.grid_columnconfigure(0, weight=1)

        info = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=10)
        info.grid(row=0, column=0, padx=20, pady=(16, 8), sticky="ew")
        ctk.CTkLabel(
            info,
            text="Lenguaje Sensible al Contexto: L = { 0^n 1^n 2^n | n ≥ 1 }   |   Fronteras: '[' y ']'   |   Γ = {[, ], 0, 1, 2, X, Y, Z}",
            font=("Segoe UI", 13, "bold"),
            text_color="#A78BFA"
        ).pack(pady=10)

        controles = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=10)
        controles.grid(row=1, column=0, padx=20, pady=8, sticky="ew")

        ctk.CTkLabel(controles, text="Cadena:", font=("Segoe UI", 13)).pack(side="left", padx=(14, 6), pady=12)
        self.entrada_cadena = ctk.CTkEntry(controles, width=160, placeholder_text="ej. 001122")
        self.entrada_cadena.pack(side="left", padx=6)

        ctk.CTkButton(controles, text="Cargar", width=90, command=self.cargar_cadena).pack(side="left", padx=4)
        self.btn_ant = ctk.CTkButton(controles, text="◀ Anterior", width=95, command=self.paso_anterior, state="disabled")
        self.btn_ant.pack(side="left", padx=4)
        self.btn_sig = ctk.CTkButton(controles, text="Siguiente ▶", width=105, command=self.siguiente_paso, state="disabled")
        self.btn_sig.pack(side="left", padx=4)
        self.btn_fin = ctk.CTkButton(controles, text="Finalizar", width=85, fg_color="#7C3AED", hover_color="#6D28D9", command=self.ir_al_final, state="disabled")
        self.btn_fin.pack(side="left", padx=4)
        ctk.CTkButton(controles, text="Limpiar", width=80, fg_color="#DC2626", hover_color="#B91C1C", command=self.limpiar).pack(side="left", padx=4)

        self.combo_ejemplos = ctk.CTkOptionMenu(
            controles,
            values=["Ejemplos...", "🟢 012 (Válida)", "🟢 001122 (Válida)", "🔴 00122 (Inválida)", "🔴 0122 (Inválida)"],
            command=self.usar_ejemplo
        )
        self.combo_ejemplos.pack(side="right", padx=14)

        visual = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=10)
        visual.grid(row=2, column=0, padx=20, pady=8, sticky="nsew")

        self.label_cinta = ctk.CTkLabel(visual, text="Cinta: [ ]", font=("Consolas", 26, "bold"), text_color="#F8FAFC")
        self.label_cinta.pack(pady=(26, 4))

        self.label_indicador = ctk.CTkLabel(visual, text="", font=("Consolas", 26, "bold"), text_color="#FACC15")
        self.label_indicador.pack(pady=(0, 12))

        self.label_estado = ctk.CTkLabel(visual, text="Estado Actual: -", font=("Segoe UI", 22, "bold"), text_color="#A78BFA")
        self.label_estado.pack(pady=8)

        self.label_detalle = ctk.CTkLabel(visual, text="Transición: -", font=("Consolas", 14), text_color="#94A3B8")
        self.label_detalle.pack(pady=(8, 22))

        self.historial = []
        self.paso_actual = 0

    def cargar_cadena(self):
        lba = AutomataLinealAcotado(self.entrada_cadena.get())
        self.historial = lba.historial
        self.paso_actual = 0
        self.actualizar_vista()

    def siguiente_paso(self):
        if self.paso_actual < len(self.historial) - 1:
            self.paso_actual += 1
            self.actualizar_vista()

    def paso_anterior(self):
        if self.paso_actual > 0:
            self.paso_actual -= 1
            self.actualizar_vista()

    def ir_al_final(self):
        if self.historial:
            self.paso_actual = len(self.historial) - 1
            self.actualizar_vista()

    def actualizar_vista(self):
        paso = self.historial[self.paso_actual]
        cinta_str = " ".join(paso["cinta"])
        self.label_cinta.configure(text=f"Cinta: {cinta_str}")

        espacios = " " * 7 + "  " * paso["cabezal"]
        self.label_indicador.configure(text=f"{espacios}^")

        color = "#22C55E" if "aceptacion" in paso["estado"] else "#EF4444" if "error" in paso["estado"] else "#A78BFA"
        self.label_estado.configure(text=f"Estado Actual: {paso['estado']}", text_color=color)
        self.label_detalle.configure(text=f"Paso {self.paso_actual}/{len(self.historial)-1}  |  {paso['detalle']}")

        self.btn_ant.configure(state="normal" if self.paso_actual > 0 else "disabled")
        self.btn_sig.configure(state="normal" if self.paso_actual < len(self.historial) - 1 else "disabled")
        self.btn_fin.configure(state="normal" if self.paso_actual < len(self.historial) - 1 else "disabled")

    def limpiar(self):
        self.entrada_cadena.delete(0, "end")
        self.label_cinta.configure(text="Cinta: [ ]")
        self.label_indicador.configure(text="")
        self.label_estado.configure(text="Estado Actual: -", text_color="#A78BFA")
        self.label_detalle.configure(text="Transición: -")
        self.btn_ant.configure(state="disabled")
        self.btn_sig.configure(state="disabled")
        self.btn_fin.configure(state="disabled")
        self.historial = []
        self.paso_actual = 0

    def usar_ejemplo(self, choice):
        if choice != "Ejemplos...":
            cadena = choice.split(" ")[1]
            self.entrada_cadena.delete(0, "end")
            self.entrada_cadena.insert(0, cadena)
            self.cargar_cadena()
        self.combo_ejemplos.set("Ejemplos...")
