# Proyecto-final-

Proyecto final equipo 3

Integrante 1:
Daniela Rivera Trejo A01714245
Juego: Pacman
Cambios: Primero se alteró la estructura del tablero, al manipular la matriz tiles, se intercambian los valores donde los 0 son las paredes azules y los 1 los pasillos transitables. Invertir o reacomodar estos números redibuja por completo la arquitectura del mapa, creando un laberinto totalmente nuevo. Después se aumentó la velocidad de los fantasmas, pasando de 5 a 20. Este ajuste se implementó en dos puntos del código: en los vectores de aparición inicial y en el bloque de decisiones (options) que calcula la nueva ruta cuando un fantasma choca. Por ultimo se reemplazó el punto blanco (dot) por un bloque de color verde lima. Para lograr esto, se eliminó la función predeterminada y se programó un ciclo de cuatro lados (path.forward(6)), ajustando matemáticamente las coordenadas para que el nuevo cuadrado quedara perfectamente centrado dentro del mosaico del pasillo.



Integrante 2:

## Luis Gabriel Miranda Espinoza — Memoria

* **Matrícula:** A01714017
* **Usuario:** Luis-777777
* **Archivo:** `memory.py`
* **Rama:** `A01714017_memory`

### Proceso y modificaciones

Trabajé en Windows con PowerShell, Python y un entorno virtual. Primero descargué y probé el juego original de Freegames. Después realicé estas modificaciones:

1. **Contador de pares:** agregué `state['pairs']` para contar las parejas encontradas y mostrar el avance en pantalla. Los clics sobre casillas descubiertas se ignoran para evitar contar una pareja nuevamente.
2. **Final de partida:** utilicé `not any(hide)` para detectar que todas las casillas están descubiertas. Al ganar, aparece un mensaje y se desactivan los clics.
3. **Tablero de 4 × 4:** reduje el tablero a 16 casillas y ocho pares. Ajusté el tamaño de las casillas, sus coordenadas y la posición de los números.

Registré la versión original, cada modificación y los comentarios en commits separados. Conservé los comentarios en inglés e integré mi rama en `main`. El archivo `.gitignore` excluye el entorno virtual y los archivos temporales.

### Instalación y ejecución

Con Python instalado, ejecutar desde la carpeta del repositorio en PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install freegames==2.5.3
python memory.py
```

Si PowerShell bloquea la activación, ejecutar `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` y volver a activarla.

Para jugar, seleccionar dos casillas con el ratón y encontrar los ocho pares.

### Pruebas realizadas

Comprobé que el tablero inicia con 16 casillas y el contador `0/8`. Al completar las parejas, muestra `8/8`, la imagen descubierta y el mensaje de victoria.

Durante el desarrollo corregí un error de indentación en `draw()` y verifiqué la sintaxis con `python -m py_compile memory.py`. También confirmé que los commits quedaron publicados en `main`.



