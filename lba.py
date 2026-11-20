class AutomataLinealAcotado:
    """LBA para L = { 0^n 1^n 2^n | n >= 1 } con cinta acotada por [ y ]."""

    ESTADOS = ["q0", "q1", "q2", "q3", "q4", "q_aceptacion", "q_error"]
    ALFABETO_CINTA = ["[", "]", "0", "1", "2", "X", "Y", "Z"]

    def __init__(self, cadena: str):
        self.cadena = cadena.strip()
        self.historial = []
        self.simular()

    def simular(self):
        cinta = ["["] + list(self.cadena) + ["]"]
        cabezal = 1
        estado = "q0"

        self.registrar_paso(estado, cinta, cabezal, "Cinta acotada inicializada entre fronteras '[' y ']'.")

        pasos_max = 500
        while pasos_max > 0:
            pasos_max -= 1
            simbolo = cinta[cabezal]
            detalle = ""

            if estado == "q0":
                if simbolo == "0":
                    cinta[cabezal] = "X"
                    cabezal += 1
                    estado = "q1"
                    detalle = "δ(q0, '0') → (q1, 'X', R)"
                elif simbolo == "Y":
                    cabezal += 1
                    estado = "q4"
                    detalle = "δ(q0, 'Y') → (q4, 'Y', R)"
                else:
                    estado = "q_error"
                    detalle = f"δ(q0, '{simbolo}') → Error de orden o cadena vacía."

            elif estado == "q1":
                if simbolo in ("0", "Y"):
                    cabezal += 1
                    detalle = f"δ(q1, '{simbolo}') → (q1, '{simbolo}', R)"
                elif simbolo == "1":
                    cinta[cabezal] = "Y"
                    cabezal += 1
                    estado = "q2"
                    detalle = "δ(q1, '1') → (q2, 'Y', R)"
                else:
                    estado = "q_error"
                    detalle = f"δ(q1, '{simbolo}') → Se esperaba '1'."

            elif estado == "q2":
                if simbolo in ("1", "Z"):
                    cabezal += 1
                    detalle = f"δ(q2, '{simbolo}') → (q2, '{simbolo}', R)"
                elif simbolo == "2":
                    cinta[cabezal] = "Z"
                    cabezal -= 1
                    estado = "q3"
                    detalle = "δ(q2, '2') → (q3, 'Z', L)"
                else:
                    estado = "q_error"
                    detalle = f"δ(q2, '{simbolo}') → Se esperaba '2'."

            elif estado == "q3":
                if simbolo in ("0", "1", "Y", "Z"):
                    cabezal -= 1
                    detalle = f"δ(q3, '{simbolo}') → (q3, '{simbolo}', L)"
                elif simbolo == "X":
                    cabezal += 1
                    estado = "q0"
                    detalle = "δ(q3, 'X') → (q0, 'X', R)"
                else:
                    estado = "q_error"
                    detalle = f"δ(q3, '{simbolo}') → Error retrocediendo cabezal."

            elif estado == "q4":
                if simbolo in ("Y", "Z"):
                    cabezal += 1
                    detalle = f"δ(q4, '{simbolo}') → (q4, '{simbolo}', R)"
                elif simbolo == "]":
                    estado = "q_aceptacion"
                    detalle = "δ(q4, ']') → Frontera derecha alcanzada. Cadena Aceptada."
                else:
                    estado = "q_error"
                    detalle = f"δ(q4, '{simbolo}') → Símbolos sin emparejar."

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
