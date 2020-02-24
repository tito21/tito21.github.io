---
layout: post
title: "Las matemáticas de la bandera de Independencia de Chile"
slug: "bandera de independencia de chile razon aurea"
date: 2019-02-10 04:22:43 -0300
use_math: true
categories: ["Mathematica", "numeros especiales", "numeros", "matematicas"]
tags: ["matematicas"]
description: La primera bandera de Chile tenia unas proporciones muy distintas
             a las actuales. La bandera estaba construida a partir de la
             razón áurea. En este articulo la describiré basándome
             principalmente en la descripción del libro de Andres Navas al
             respecto.
---

# Las proporciones de la bandera de Chile

Inspirado por la asombrosa descripción de las proporciones de la bandera de Independencia de Chile en el primer capitulo[^1] del excelente libro de Andrés Navas (*"Un viaje a las ideas 33 historias matemáticas asombrosas"*) decidí recrear la bandera en `Mathematica`.
La bandera usada durante la Patria Nueva fue encomendada por Bernardo O'Higgins y oficializada como la bandera del país el 12 de febrero de 1818, día del juramento de Independencia.
Esta bandera tiene los mismos colores y forma de que la bandera actual pero esta diseñada usando la elegancia de proporción áurea.
La proporción áurea es considerada la más bella y esta presente en la naturaleza.
Esta es la razón en la que se divide un segmento tal que la razón entre las partes es igual a la razón entre el lado mayor y el largo total.

![Razón áurea](https://upload.wikimedia.org/wikipedia/commons/4/44/Golden_ratio_line.svg)

$$\varphi = \frac{a}{b} = \frac{1+\sqrt{5}}{2} = 1.6180... $$

La estrella en la bandera de la independencia esta formada a partir de una división particular del area azul. La razón entre el alto y largo del rectángulo es

$$ \frac{\sqrt[\leftroot{-2}\uproot{2}4]{5}}{\sqrt{2+\sqrt{5}}} $$

lo que permite que las diagonales se encuentren en ángulos de $70^\circ$ y $180^\circ$, luego se pueden formar 5 lineas que se cruzan en el origen en $32^\circ$.
Finalmente la estrella de cinco puntas se construye uniendo las diagonales alternadas (en los artículos citados puedes ver un diagrama de esto para que lo entiendas mejor).

Con el siguiente código de`Mathematica` podemos generar la bandera de la independencia

```mathematica
largo = (2 + Sqrt[5])/Sqrt[10 - 2 Sqrt[5]]; largoazul = 5^(1/4)/
 Sqrt[2 + Sqrt[5]];
penOut = CirclePoints[{0.25/largoazul, 0.75}, {0.25/GoldenRatio,
    180 Degree}, 5];
penIn = CirclePoints[{0.25/largoazul, 0.75}, {0.065, -140 Degree}, 5];
star = Polygon[{penOut[[1]], penIn[[1]], penOut[[2]], penIn[[2]],
    penOut[[3]], penIn[[3]], penOut[[4]], penIn[[4]], penOut[[5]],
    penIn[[5]], penOut[[1]]}];
Graphics[{White, Rectangle[{0, 0}, {largo, 1}], RGBColor["#d52b1e"],
  Rectangle[{0, 0}, {largo, 0.5}], RGBColor["#0039a6"],
  Rectangle[{0, 0.5}, {0.5/largoazul, 1}], White, star}]
```
<div class="boxed">
<h4>Bandera de la independencia</h4>
<img alt="bandera de la independencia generada" src="/assets/posts/bandera-independencia/bandera-ind.svg" style="width: 100%;"/>

<h4>Bandera actual</h4>
<img alt="bandera actual" src="https://upload.wikimedia.org/wikipedia/commons/7/78/Flag_of_Chile.svg" style="width: 100%;"/>
</div>

La bandera de la independencia es mucho mas ancha y la estrella apunta en un angulo destacando sus proporciones matemáticas.
¿Cuál version crees que es más bella?
Personalmente creo que la version de la independencia se ve un poco extraña (probablemente por estar más familiarizado con la actual), pero es esto mismo lo que nos hace investigar y aprender más de nuestra historia y las matemáticas.

## Para los curiosos

Las instrucciones de como dibujar la bandera de la independencia con compás y regla están disponibles en el libro. Aunque no debiera ser muy difícil deducirlas si sabes como construir la razón áurea.

[^1]: Este capitulo se vasa en un articulo de la [Revista Bicentenario](http://www.mat.usach.cl/images/Profesores/navas-papers/historia-bandera.pdf) y una columna de [opinion](https://www.elmostrador.cl/cultura/2015/10/17/la-dimension-hermosa-y-desconocida-de-la-primera-estrella-de-chile/) escritos por el autor.
