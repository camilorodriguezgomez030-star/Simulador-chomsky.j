class AutomataFinito:
    """AFD para el lenguaje regular L = { w ∈ {0,1}* | w termina en '01' }."""

    ESTADOS = ["q0", "q1", "q2 (Final)", "q_error"]
    ALFABETO = ["0", "1"]

    def __init__(self, cadena: str):
        self.cadena = cadena.strip()
        self.historial = []
        self.simular()

    def simular(self):
        estado = "q0"
        cinta = list(self.cadena)

        self.historial.append({
            "estado": estado,
            "cinta": "".join(cinta),
            "detalle": "Estado inicial q0. Esperando símbolos en {0, 1}."
        })

        for i, simbolo in enumerate(cinta):
            estado_ant = estado
            if simbolo not in self.ALFABETO:
                estado = "q_error"
                detalle = f"Símbolo '{simbolo}' fuera de Σ={{0,1}} → q_error"
            elif estado == "q0":
                if simbolo == "0":
                    estado = "q1"
                else:
                    estado = "q0"
                detalle = f"δ({estado_ant}, '{simbolo}') = {estado}"
            elif estado == "q1":
                if simbolo == "0":
                    estado = "q1"
                else:
                    estado = "q2"
                detalle = f"δ({estado_ant}, '{simbolo}') = {estado}"
            elif estado == "q2":
                if simbolo == "0":
                    estado = "q1"
                else:
                    estado = "q0"
                detalle = f"δ({estado_ant}, '{simbolo}') = {estado}"

            self.historial.append({
                "estado": estado,
                "cinta": "".join(cinta[i + 1:]),
                "detalle": detalle
            })

            if estado == "q_error":
                break

        estado_final = self.historial[-1]["estado"]
        if estado_final == "q2":
            self.historial[-1]["estado"] = "q2 (Aceptada)"
            self.historial[-1]["detalle"] += " | Fin de cadena en estado de aceptación q2."
        else:
            if "error" not in estado_final:
                self.historial[-1]["estado"] = f"{estado_final} (Rechazada)"
                self.historial[-1]["detalle"] += f" | Fin de cadena en {estado_final} (no es estado final)."
            else:
                self.historial[-1]["estado"] = "q_error (Rechazada)"
