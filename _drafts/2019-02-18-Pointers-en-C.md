---
layout: post
title: "Pointers y manejo de memoria en C"
date: 2019-02-08 22:22:43 -0300
categories: ["C", "algoritmo", "programacion", "tutorial"]
tags: ["punteros", "memoria", "pointers", "arrays"]
---

Cuando comencé a programar en C/C++ ya había tenido experiencia con JavaScript y Java, por lo que pense que seria fácil aprender un nuevo lenguaje.
Pude entender como declarar variables, *loops*, *ifs*, y algunas otras cosas básicas, pero cuando vi un `*` ya no logre seguir el código.
Se supone que tienen algo que ver con el acceso a la memoria, pero ¿para que sirven?, ¿qué tienen que ver con los arreglos?
Durante el último mes decidí aprender más de C y aprender punteros y manejo de memoria.

En este articulo documentare el

<!-- Un de las razones de porque C es un lenguaje muy poderoso es su capacidad de manejar directamente la memoria del computador. -->

# La memoria de un computador

Lo primero que hay que comprender es como funciona la memoria del computador.
La memoria RAM de computador es como una calle con muchas casas donde cada una tiene un numero de dirección y un habitante.
El procesador es capaz de ir a una dirección y ver quien es el habitante o cambiarlo.

![Calle con direcciones](../assets/posts/pointers-c/street-of-houses.jpg)

Cuando programas algo en el computador, por ejemplo `int x = 12` el computador guardara el numero 12 de tipo `int` en una posición de la memoria RAM y recordara que te vas a referir a esa posición como `x` y que allí hay un `int`.
En nuestra analogía seria poner el habitante "12" en la casa `A` (por ejemplo) y guardar que te vas a referir a con el nombre `x`.
En un computador las direcciones de la *"calle"* (o de memoria) son un numero de 32 bytes (depende de la arquitectura del PC) normalmente expresado por un numero [hexadecimal](https://es.wikipedia.org/wiki/Sistema_hexadecimal) como 0xd5638970.


# Acceso a la memoria de C

Vamos directo a un ejemplo

```c
#include <stdio.h>

int main() {
    int x = 12;
    int y = x;
    int *np = &x; // np es una direccion en memoria
    printf("&x: %#x\n", &x); // &x: 0xd5638970
    printf("*np: %i\n", *np); // con esto accedemos a su valor
    x = x + 8; // x ahora es 20
    printf("*np: %i, y: %i\n", *np); // imprime *np: 20, y = 12
    *np += 1; \\ incrementamos x
    printf("x: %i\n", x) // x: 21
    return 0;
}
```
<!--
    printf("x: %i\n", x);
    // x: 12
    printf("&x: %#x\n", &x);
    // &x: 0xd5638970
    printf("np: %#x\n", np);
    // np: 0xd5638970
    printf("*np: %i\n", *np);
    // *np: 12 -->

En la primera linea definimos una variable tipo `int` y le asignamos el valor 12.
También copiamos el valor en otra variable `y`
La siguiente expresión es más interesante y con mucho símbolo que puede parecer críptica.
Declaramos un puntero con el operador `*` al que llamamos `np` y le asignamos la dirección de la variable `x`, la que obtenemos mediante el operador `&`.
Usando el operador `*` en un puntero podemos acceder al valor que esta almacenado en esa posición de memoria.
Cuando modificamos el valor de `x` al buscar el valor a través del puntero `np` obtenemos es valor modificado (20).
`y` no cambio porque cuando





| Código           | Valor        | Representa |
|------------------|--------------|------------------------------------------------------|
|  `x`             |  `12`        | El valor guardado en memoria (`int 12`)              |
|  `&x`            | `0xd5638970` | La posicion en memoria donde esta guardado el numero |
|  `int * np = &x` | `0xd5638970` | `np` es un puntero a la dirección de memoria de `x`  |

# Arreglos y punteros

En C el concepto de arreglo (cosas como `int *a[10]`) y punteros esta muy relacionada.
Tanto asi que no se pueden usar arreglos sin saber de punteros ni comprender los punteros sin entender como se conectan con arreglos.
