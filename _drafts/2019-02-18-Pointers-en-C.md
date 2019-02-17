---
layout: post
title: "Pointers y manejo de memoria en C"
date: 2019-02-08 22:22:43 -0300
categories: ["C", "algoritmo", "programacion"]
tags: ["punteros", "memoria", "pinters", "arrays"]
---

Cuando comencé a programar en C/C++ ya había tenido experiencia con JavaScript y Java, por lo que pense que seria fácil aprender un nuevo lenguaje.
Que inocente fui. Pude entender como declarar variables, --loops--, ifs, y algunas otras cosas básicas, pero cuando vi un `*` ya no logre seguir el código.
Se que tienen algo que ver con el acceso a la memoria, pero ¿para que sirven?, ¿porque se usan con arreglos?
Asi que decidí convertirme en un programador de C de verdad y aprender punteros y manejo de memoria.

# La memoria de un computador

Lo primero que hay que comprender es como funciona la memoria del computador.
La memoria RAM de computador es como una calle con muchas casas donde cada una tiene un numero de dirección y un habitante.
El procesador es capaz de ir a una dirección y ver quien es el habitante o cambiarlo.

![Calle con direcciones](../assets/posts/pointers-c/street-of-houses.jpg)

Cuando programas algo en el computador, por ejemplo `x = 12` el computador guardara el numero 12 en una posición de la memoria RAM.
En nuestra analogía seria poner el habitante `12` en la casa `A` (por ejemplo) y guardar que te vas a referir a el por `x`.
La memoria de un computador las direcciones son un numero de 8 bytes normalmente expresado por un numero [hexadecimal](https://es.wikipedia.org/wiki/Sistema_hexadecimal) como 0xd5638970.

# Acceso a la memoria de C

Un de las razones de porque C es un lenguaje muy poderoso es su capacidad de manejar directamente la memoria del computador.

```c
int main() {
    int *num;
    return 0;
}
```