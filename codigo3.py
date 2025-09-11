"""
Este programa le pide al usuario que escriba una línea de su canción favorita
y luego la imprime alineada a la derecha de la terminal.
"""

# TODO Tarea 1:
# Pedir al usuario que escriba su línea favorita de una canción

favorita = input("me gusta el olor que tiene la mañana: ")

# TODO Tarea 2:

# Alinear la línea a la derecha de la terminal
# Puedes usar el método .rjust(ancho) para mover el texto hacia la derecha
# Ejemplo: linea.rjust(80)

ancho = 80

# TODO Tarea 3:

# Imprimir la línea alineada a la derecha

print(favorita.rjust(ancho))


