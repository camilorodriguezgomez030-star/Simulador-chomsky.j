class AutamataPila:
    """PDA para L = { w c w^R | w ∈ {a,b}* } usando pila LIFO."""

    ESTADOS = ["q0 (Apilar)", "q1 (Comparar)", "q2 (Aceptada)", "q_error"]
    ALFABETO_CINTA = ["a", "b", "c"]
    ALFABETO_PILA = ["Z0", "A", "B"]

    def __init__(self, cadena: str):
        self.cadena = cadena.strip()
        self.historial = []
        self.simular()

    def simular(self):
        estado = "q0"
        pila = ["Z0"]
        cinta = list(self.cadena)

        self.historial.append({
            "estado": estado,
            "cinta": "".join(cinta),
            "pila": list(pila),
            "detalle": "Inicio en q0 con fondo de pila Z0."
        })

        error = False
        detalle = ""
        for i, simbolo in enumerate(cinta):
            tope = pila[-1]
            if estado == "q0":
                if simbolo in ("a", "b"):
                    marca = simbolo.upper()
                    pila.append(marca)
                    detalle = f"δ(q0, '{simbolo}', {tope}) → (q0, Push '{marca}')"
                elif simbolo == "c":
                    estado = "q1"
                    detalle = f"δ(q0, 'c', {tope}) → (q1, Cambio a fase de desapilado)"
                else:
                    error = True
                    detalle = f"Símbolo inválido '{simbolo}' en q0."
                    break
            elif estado == "q1":
                if simbolo == "a" and tope == "A":
                    pila.pop()
                    detalle = "δ(q1, 'a', A) → (q1, Pop 'A')"
                elif simbolo == "b" and tope == "B":
                    pila.pop()
                    detalle = "δ(q1, 'b', B) → (q1, Pop 'B')"
                else:
                    error = True
                    detalle = f"Fallo de coincidencia: leído '{simbolo}' con tope '{tope}'."
                    break

            self.historial.append({
                "estado": estado,
                "cinta": "".join(cinta[i + 1:]),
                "pila": list(pila),
                "detalle": detalle
            })

        if not error and estado == "q1" and len(pila) == 1 and pila[0] == "Z0":
            self.historial.append({
                "estado": "q2 (Aceptada)",
                "cinta": "",
                "pila": list(pila),
                "detalle": "Cadena consumida y pila vacía (solo Z0) → Aceptada."
            })
        else:
            motivo = detalle if error else "Cadena incompleta (falta 'c' o sobran símbolos en pila)."
            self.historial.append({
                "estado": "q_error (Rechazada)",
                "cinta": "",
                "pila": list(pila),
                "detalle": f"{motivo} → Rechazada."
            })
