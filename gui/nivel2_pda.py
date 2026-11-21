import customtkinter as ctk
from models.pda import AutamataPila


class Nivel2Window(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Nivel 2 - Autómata de Pila (PDA) | Camilo Rodríguez")
        self.geometry("1060x620")
        self.configure(fg_color="#0F172A")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        info = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=10)
        info.grid(row=0, column=0, padx=20, pady=(16, 8), sticky="ew")
        ctk.CTkLabel(
            info,
            text="Lenguaje Libre de Contexto: L = { w c w^R | w ∈ {a,b}* }   |   Memoria LIFO   |   Γ = {Z0, A, B}",
            font=("Segoe UI", 13, "bold"),
            text_color="#2DD4BF"
        ).pack(pady=10)

        controles = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=10)
        controles.grid(row=1, column=0, padx=20, pady=8, sticky="ew")

        ctk.CTkLabel(controles, text="Cadena:", font=("Segoe UI", 13)).pack(side="left", padx=(14, 6), pady=12)
        self.entrada_cadena = ctk.CTkEntry(controles, width=160, placeholder_text="ej. abcba")
        self.entrada_cadena.pack(side="left", padx=6)

        ctk.CTkButton(controles, text="Cargar", width=90, command=self.cargar_cadena).pack(side="left", padx=4)
        self.btn_ant = ctk.CTkButton(controles, text="◀ Anterior", width=95, command=self.paso_anterior, state="disabled")
        self.btn_ant.pack(side="left", padx=4)
        self.btn_sig = ctk.CTkButton(controles, text="Siguiente ▶", width=105, command=self.siguiente_paso, state="disabled")
        self.btn_sig.pack(side="left", padx=4)
        self.btn_fin = ctk.CTkButton(controles, text="Finalizar", width=85, fg_color="#0D9488", hover_color="#0F766E", command=self.ir_al_final, state="disabled")
        self.btn_fin.pack(side="left", padx=4)
        ctk.CTkButton(controles, text="Limpiar", width=80, fg_color="#DC2626", hover_color="#B91C1C", command=self.limpiar).pack(side="left", padx=4)

        self.combo_ejemplos = ctk.CTkOptionMenu(
            controles,
            values=["Ejemplos...", "🟢 abcba (Válida)", "🟢 aabcbaa (Válida)", "🟢 c (Válida)", "🔴 abca (Inválida)", "🔴 abba (Inválida)"],
            command=self.usar_ejemplo
        )
        self.combo_ejemplos.pack(side="right", padx=14)

        cuerpo = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=10)
        cuerpo.grid(row=2, column=0, padx=20, pady=(8, 18), sticky="nsew")
        cuerpo.grid_columnconfigure(0, weight=2)
        cuerpo.grid_columnconfigure(1, weight=1)

        izq = ctk.CTkFrame(cuerpo, fg_color="transparent")
        izq.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.label_cinta = ctk.CTkLabel(izq, text="Cinta restante: [ ]", font=("Consolas", 20, "bold"))
        self.label_cinta.pack(pady=(30, 15))

        self.label_estado = ctk.CTkLabel(izq, text="Estado Actual: q0", font=("Segoe UI", 22, "bold"), text_color="#2DD4BF")
        self.label_estado.pack(pady=15)

        self.label_detalle = ctk.CTkLabel(izq, text="Operación: -", font=("Consolas", 13), text_color="#94A3B8", wraplength=520)
        self.label_detalle.pack(pady=15)

        der = ctk.CTkFrame(cuerpo, fg_color="#0F172A", corner_radius=10)
        der.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        ctk.CTkLabel(der, text="PILA LIFO (Tope arriba)", font=("Segoe UI", 13, "bold"), text_color="#38BDF8").pack(pady=(12, 6))
        self.vista_pila = ctk.CTkTextbox(der, width=180, height=280, font=("Consolas", 17, "bold"), state="disabled", fg_color="#0F172A")
        self.vista_pila.pack(pady=8, padx=12)

        self.historial = []
        self.paso_actual = 0

    def cargar_cadena(self):
        pda = AutamataPila(self.entrada_cadena.get())
        self.historial = pda.historial
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
        dato = self.historial[self.paso_actual]
        self.label_cinta.configure(text=f"Cinta restante: [ {dato['cinta']} ]")

        color = "#22C55E" if "Aceptada" in dato["estado"] else "#EF4444" if "Rechazada" in dato["estado"] else "#2DD4BF"
        self.label_estado.configure(text=f"Estado Actual: {dato['estado']}", text_color=color)
        self.label_detalle.configure(text=f"Paso {self.paso_actual}/{len(self.historial)-1}  |  {dato['detalle']}")

        self.vista_pila.configure(state="normal")
        self.vista_pila.delete("1.0", "end")
        for elem in reversed(dato["pila"]):
            self.vista_pila.insert("end", f"  |  {elem:^3}  |\n")
            self.vista_pila.insert("end", "  +-------+\n")
        self.vista_pila.configure(state="disabled")

        self.btn_ant.configure(state="normal" if self.paso_actual > 0 else "disabled")
        self.btn_sig.configure(state="normal" if self.paso_actual < len(self.historial) - 1 else "disabled")
        self.btn_fin.configure(state="normal" if self.paso_actual < len(self.historial) - 1 else "disabled")

    def limpiar(self):
        self.entrada_cadena.delete(0, "end")
        self.label_cinta.configure(text="Cinta restante: [ ]")
        self.label_estado.configure(text="Estado Actual: q0", text_color="#2DD4BF")
        self.label_detalle.configure(text="Operación: -")
        self.vista_pila.configure(state="normal")
        self.vista_pila.delete("1.0", "end")
        self.vista_pila.configure(state="disabled")
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

       
     
       
        
