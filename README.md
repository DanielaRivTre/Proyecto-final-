# Proyecto-final-
Proyecto final equipo 3

Integrante 1: 
Daniela Rivera Trejo A01714245
Juego: Pacman
Cambios: Primero se alteró la estructura del tablero, al manipular la matriz tiles, se intercambian los valores donde los 0 son las paredes azules y los 1 los pasillos transitables. Invertir o reacomodar estos números redibuja por completo la arquitectura del mapa, creando un laberinto totalmente nuevo. Después se aumentó la velocidad de los fantasmas, pasando de 5 a 20. Este ajuste se implementó en dos puntos del código: en los vectores de aparición inicial y en el bloque de decisiones (options) que calcula la nueva ruta cuando un fantasma choca. Por ultimo se reemplazó el punto blanco (dot) por un bloque de color verde lima. Para lograr esto, se eliminó la función predeterminada y se programó un ciclo de cuatro lados (path.forward(6)), ajustando matemáticamente las coordenadas para que el nuevo cuadrado quedara perfectamente centrado dentro del mosaico del pasillo.
