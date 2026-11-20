# Simulador de la Jerarquía de Chomsky

**Autor:** Camilo Rodríguez  
**Repositorio:** [github.com/camilorodriguezgomez030-star/Simulador-chomsky.j](https://github.com/camilorodriguezgomez030-star/Simulador-chomsky.j)

Aplicación de escritorio con Interfaz Gráfica de Usuario (GUI) desarrollada en Python y `customtkinter` para simular, validar y visualizar paso a paso los cuatro niveles de la Jerarquía de Chomsky.

---

## Instalación y Ejecución

### Requisitos previos
* Python 3.10 o superior.
* Biblioteca `customtkinter`.

### Pasos de ejecución
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/camilorodriguezgomez030-star/Simulador-chomsky.j.git
   cd Simulador-chomsky.j
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```
   *(En Windows también puedes hacer doble clic directamente en `ABRIR_SIMULADOR.bat`).*

---

## Módulos y Cadenas de Prueba (Incluidas en la Interfaz)

Desde el panel principal selecciona uno de los cuatro niveles. Puedes escribir una cadena propia o elegir una del menú **Ejemplos...**, pulsar **Cargar** y recorrer la ejecución con **Siguiente ▶**, **◀ Anterior** o **Finalizar**.

| Nivel | Modelo | Lenguaje / Función | Cadenas Válidas | Cadenas Inválidas |
| :--- | :--- | :--- | :--- | :--- |
| **Nivel 3** | Autómata Finito Determinista (AFD) | Cadenas sobre $\{0,1\}$ terminadas en `01` — `(0\|1)*01` | `1001`, `01` | `11010`, `111` |
| **Nivel 2** | Autómata de Pila (PDA - LIFO) | Palíndromos con marcador central $\{w c w^R \mid w \in \{a,b\}^*\}$ | `abcba`, `aabcbaa`, `c` | `abca`, `abba` |
| **Nivel 1** | Autómata Linealmente Acotado (LBA) | Lenguaje sensible al contexto $\{0^n 1^n 2^n \mid n \ge 1\}$ | `012`, `001122` | `00122`, `0122` |
| **Nivel 0** | Máquina de Turing (MT) | Complemento a uno binario sobre $\{0,1\}^+$ | `10110` ($\to$ `01001`), `1110` ($\to$ `0001`) | `102` |

---

## Arquitectura del Proyecto

* `main.py`: Ventana principal con selección interactiva de los cuatro niveles.
* `models/dfa.py`: Lógica de transiciones $\delta(q, a)$ del Autómata Finito Determinista.
* `models/pda.py`: Implementación de pila LIFO con fondo $Z_0$ y operaciones *Push* / *Pop*.
* `models/lba.py`: Cinta acotada entre fronteras `[` y `]` con desplazamiento bidireccional del cabezal.
* `models/tm.py`: Cinta dinámicamente expansible con blancos `⊔` y cabezal de lectura/escritura.
* `gui/`: Interfaces gráficas independientes por cada nivel con traza de transiciones en tiempo real.
