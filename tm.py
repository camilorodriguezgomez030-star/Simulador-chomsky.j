class MaquinaTuring:
    """Máquina de Turing para calcular el Complemento a Uno Binario sobre {0,1}+."""

    ESTADOS = ["q0 (Invertir)", "q1 (Rebobinar)", "q_aceptacion", "q_error"]
    ALFABETO_ENTRADA = ["0", "1"]
    ALFABETO_CINTA = ["0", "1", "⊔"]

    def __init__(self, cadena: str):
        self.cadena = cadena.strip()
        self.historial = []
        self.simular()

    def simular(self):
        cinta = ["⊔", "⊔"] + list(self.cadena) + ["⊔", "⊔"]
        cabezal = 2
        estado = "q0"

        self.registrar_paso(estado, cinta, cabezal, "Cinta infinita iniciada con blancos '⊔'. Cabezal en primer bit.")

        if not self.cadena:
            self.registrar_paso("q_error", cinta, cabezal, "Entrada vacía no permitida en {0,1}+.")
            return

        pasos_max = 500
        while pasos_max > 0:
            pasos_max -= 1
            if cabezal == 0:
                cinta = ["⊔"] + cinta
                cabezal = 1
            elif cabezal == len(cinta) - 1:
                cinta.append("⊔")

            simbolo = cinta[cabezal]
            detalle = ""

            if estado == "q0":
                if simbolo == "0":
                    cinta[cabezal] = "1"
                    cabezal += 1
                    detalle = "δ(q0, '0') → (q0, '1', R)"
                elif simbolo == "1":
                    cinta[cabezal] = "0"
                    cabezal += 1
                    detalle = "δ(q0, '1') → (q0, '0', R)"
                elif simbolo == "⊔":
                    cabezal -= 1
                    estado = "q1"
                    detalle = "δ(q0, '⊔') → (q1, '⊔', L) [Fin de bits, regresando]"
                else:
                    estado = "q_error"
                    detalle = f"δ(q0, '{simbolo}') → Símbolo inválido fuera de Σ={{0,1}}."

            elif estado == "q1":
                if simbolo in ("0", "1"):
                    cabezal -= 1
                    detalle = f"δ(q1, '{simbolo}') → (q1, '{simbolo}', L)"
                elif simbolo == "⊔":
                    cabezal += 1
                    estado = "q_aceptacion"
                    detalle = "δ(q1, '⊔') → (q_aceptacion, '⊔', R) [Complemento completado]"
                else:
                    estado = "q_error"
                    detalle = f"δ(q1, '{simbolo}') → Error inesperado."

            self.registrar_paso(estado, cinta, cabezal, detalle)

            if estado in ("q_aceptacion", "q_error"):
                break

    def registrar_paso(self, estado, cinta, cabezal, detalle):
        self.historial.append({
            "estado": estado,
            "cinta": list(cinta),
            "cabezal": cabezal,
            "detalle": detalle
        })
