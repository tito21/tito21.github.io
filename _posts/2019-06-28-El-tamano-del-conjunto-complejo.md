---
layout: post
title: "El tamaño del conjunto complejo"
slug: "tamano-conjunto-complejo"
date: 2019-06-24 22:22:43 -0300
use_math: true
categories: ["matematicas", "numeros"]
tags: ["complejos", "cardinalidad", "grupos", "matemáticas", "números", "sets", biyeccion"]
description: Algunos infinitos son más grandes que otros... Entre los números
             racionales y los numeros reales esto es cierto, ¿Pero entre los
             números reales e imaginarios, también son los complejos más
             numerosos?
---

El otro día mientras caminaba de regreso a casa recordé la explicación de mi
profesor de precálculo [Mario Ponce](http://www.mat.uc.cl/~mponcea/index.html)
sobre la cantidad de los números en el conjunto racional (fracciones
$\mathbb{Q}$) y el real ($\mathbb{R}$). Mi profesor explico que en una recta los
números racionales tiene "hoyos" en comparación a la recta de los reales. Nos
explico que siempre es posible encontrar una cantidad infinita de reales entre
dos racionales y ese infinito contiene más elementos que todo el conjunto de los
racionales. Al caminar se me ocurrió preguntarme que pasa entre los reales y el
siguiente conjunto de números, los complejos. ¿Existirán más complejos que
reales? Los complejos son como dos números reales ($a+ib$) por lo que deberían
ser más grandes pero mi experiencia me dice que en las matemáticas no siempre la
primera respuesta es la correcta.

# Cardinalidad de un conjunto

Formalmente la cantidad de elementos en un conjunto se llama cardinalidad. Por
ejemplo el conjunto $S=\{1, 3, 5, 6, 8\}$ contiene 5 elementos por lo tanto su
cardinalidad es 5. Usualmente se denota $|S|$ o $\#S$. Cuando dos conjuntos
tienen la misma cantidad de elementos, es decir, $|S_1|=|S_2|$$ existe una
función[^1] que relaciona cada elemento de $S_1$ con uno de $S_2$. Por ejemplo
los elementos del conjunto y $S_2=\{1, 4, 9, 16 \}$ se pueden escribir a partir
de los cuadrados del conjunto $S_1=\{1, 2, 3, 4 \}$. En este caso la función es
$x^2$. Esta definición se puede usar incluso para conjuntos con una cantidad
infinita de elementos. Por ejemplo el conjunto $P=\{0, 2, 4, 6, 8, ... \}$ de
los números pares tiene la misma cardinalidad que el conjunto de todos los
naturales $\mathbb{N}=\{0, 1, 2, 3, 4, ...\}$ ya que los pares se pueden
escribir a partir de los naturales como $2n$, por lo tanto $|P|=|\mathbb{N}|$.
Cuando existe este mapa o función entre dos conjuntos se dice que existe una
biyeccion entre ambos.

![biyeccion de conjuntos (de Wikipedia.org)](https://upload.wikimedia.org/wikipedia/commons/f/ff/Aplicaci%C3%B3n_2_inyectiva_sobreyectiva04.svg)

Un resultado sorprendente es que existen conjuntos con cantidad infinita de
elelmentos que tienen menos elementos que otro conjunto infinito. El mejor
ejemplo de esto es la relacion entre el conjunto real y el racional. Como me
explico mi profesor la cardinalidad del conjunto real es mayor a la del conjunto
de los racionales, porque no es posible establecer una relación entre los
conjuntos. La demostracion de esto se puede hacer a traves de la diagonal de
Cantor como explica James Grime para Numberphile en este
[video](https://youtu.be/elvOZm0d4H0).

# Cardinalidad del conjunto complejo

Para poder responder la pregunta de este articulo debemos verificar que existe
una función biyectiva entre el conjunto complejo y el real. Una forma de pensar
en este problema es buscar una forma de transformar un numero real en uno
complejo (y solo uno). Recordando que un complejo tiene la forma $a+ib$ tenemos
que encontrar una forma de conectar un numero $x$ con $a$ y $b$. Si
representamos el numero real como una serie de dígitos, $0.x_1x_2x_3...$
podemos tomar los dígitos pares para formar la parte real y los impares para la
parte imaginaria teniendo asi el numero $0.x_2x_4 + i0.x_1x_3$. Dado que existe
más de una forma de representar algunos números (ej. $0.999... 1$) debemos
preocuparnos de usar la representacion con menos digitos ($1$ en el caso
anterior). Esta biyeccion nos permite transformar un numero real en uno complejo
por lo que es posible utilizarla para demostrar la igualdad de la cardinalidad
entre el conjunto complejo y el real.

Otra forma de demostrar este resultado que descubrí investigando para este
articulo es usar curva rellenadora del espacio (_space-filling curves_). Estas
curvas se construyen iterativamente a partir de reglas simples que en cada
iteración cobren mas y mas lugares del plano. Estas fueron uno de los primeros
ejemplos de los fractales. Fueron usadas por primera vez por Peano para
responder esta misma pregunta en 1900. Peano utilizo la curva

![Curva de Peano](../../assets/posts/conjuntos-cardinalidad/Peano2.gif)

Otra curva popular es la curva de Hilbert

![Curva de Hilbert](../../assets/posts/conjuntos-cardinalidad/Hilbert2.gif)

Estas curvas son continuas y pueden recorrerse sin salirse nunca de la linea. En
términos más avanzados se pueden parametrizar con una sola variable, pero
recorren todo el espacio 2D. Luego pueden usarse como un mapa entre un valor
unidimensional y el plano.

Estas curvas me hicieron recordar a otra función que había visto $a\sin(ax)$ que
también al hacer $a\rightarrow\infty$ también rellena todo el espacio. Aunque
esta no están elegante ni agradable a la vista como la de Peano también cumple
con rellenar el espacio y ser continua asi que también sirve como una biyecion
entre el conjunto complejos y el real.

![Curva a sin(ax)](../../assets/posts/conjuntos-cardinalidad/sin2.gif)

Dado que el conjunto complejo y $\mathbb{R}^2$ son homólogos, también hemos
mostrado que el infinito del espacio es igual al de una recta. Lo que hemos
logrado descubrir es muy sorprendente y a primera vista puede parecer extraño.
Pero eso es lo bonito de las matemáticas, la verdad puede esconderse pero
siempre aflora cuando uno intenta buscarla.


[^1]: La función debe ser biyectiva o 1 a 1, es decir, debe asignar un elemento único del recorrido a cada elemento del dominio.
