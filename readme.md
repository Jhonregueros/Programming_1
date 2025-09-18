Este archivo README describe tres tareas prácticas para familiarizarse con el uso de bucles y gráficos en Python. Cada tarea tiene un enfoque diferente: desde la impresión de secuencias de números hasta la creación de figuras gráficas con Turtle Graphics.

Ejercicio1_bucles: Uso de Bucles para Imprimir Números y Frases
Descripción:
En esta tarea, se ejercita el uso de bucles for para imprimir una secuencia de números y frases. Completa los siguientes ejercicios:

Imprimir los números del 0 al 5:
Escribe un bucle for que imprima los números del 0 al 5 (inclusive).
Pista: Asegúrate de que el bucle incluya el número 5.

Salida esperada:

0
1
2
3
4
5


Imprimir la frase "Soy" tres veces:
Escribe un bucle for que imprima la frase "Soy" tres veces, sin cambiar el texto.
Pista: Solo imprime la frase tal como está.

Salida esperada:

Soy
Soy
Soy


Imprimir los números pares entre 2 y 10:
Escribe un bucle for que imprima los números pares entre 2 y 10 (inclusive).
Pista: Usa range() para contar de dos en dos.

Salida esperada:

2
4
6
8
10

Instrucciones:

Escribe el código para cada tarea y ejecútalo para verificar que la salida sea la correcta.

Asegúrate de utilizar correctamente los bucles for y las funciones como range().

Ejercicio2_turtle: Crear un Triángulo con Turtle Graphics
Descripción:

Esta tarea tiene como objetivo familiarizarte con Turtle Graphics. Debes escribir un código para dibujar un triángulo equilátero utilizando Turtle. El triángulo debe ser de color azul, con un grosor de línea de 3 y lados de 150 unidades.

Código base:
import turtle

t = turtle.Turtle()
t.color("blue")
t.pensize(3)

for _ in range(3):
    t.forward(150)
    t.left(120)

turtle.done()

Pasos a seguir:

Ejecuta el código proporcionado para generar un triángulo equilátero.

Toma una captura de pantalla de la figura generada.

Asegúrate de que el triángulo tenga tres lados iguales de 150 unidades y los ángulos correctos de 120 grados.

Instrucciones adicionales:

Cuando el triángulo se dibuje correctamente, guarda la captura de pantalla y compártela.

Ejercicio3_arco: Crear una Figura Diferente con Turtle Graphics
Descripción:

Usando el archivo codigo2.py como base, modifica el código para crear una figura diferente. Algunas ideas incluyen un arco, un paralelogramo, una estrella o cualquier otra figura creativa que puedas imaginar.

Ejemplos de figuras:

Arco: Utiliza t.circle() con un ángulo específico para crear un arco. Ejemplo:

t.circle(100, 180)  # Dibuja un arco de radio 100 y 180 grados


Paralelogramo: Usa combinaciones de movimientos y giros para crear un paralelogramo:

for _ in range(2):
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.left(120)


Estrella: Dibuja una estrella con 5 puntas usando ángulos de 144 grados:

for _ in range(5):
    t.forward(100)
    t.right(144)

Pasos a seguir:

Modifica el código base para crear una figura diferente.

Puedes probar diferentes formas como un arco, paralelogramo, estrella o cualquier otra idea creativa.

Ejecuta el código y verifica que la figura se dibuje correctamente.

Instrucciones Generales:

Verificación: Asegúrate de que cada programa funcione correctamente y que los resultados coincidan con la salida esperada.

Creatividad: No dudes en experimentar con Turtle Graphics en la tarea 3, creando cualquier figura que te guste.

Capturas de Pantalla: Para las tareas con gráficos, guarda y comparte las capturas de pantalla de tus resultados.