---
layout: post
title: "Método Babilónico para calcular raíces cuadradas"
slug: "metodo babilonico"
date: 2019-02-08 22:22:43 -0300
use_math: true
categories: ["Python", "algoritmo", "programacion"]
tags: ["numpy", "raíz", "babilonico", "newton-raphson"]
description: Calcular raíces cuadradas numéricamente es un problema muy antiguo.
             Aquí veremos como calcularlo usando un método desarrollado en
             mesopotamia y lo implementaremos en python.
---

# ¿Cómo calcular $\sqrt{2}$?

¡Fácil con la app calculadora de mi celular!

Bien, pero sabemos que en 1600 BC mesopotamia ya se había calculado la raíz de 2
correctamente a 6 decimales. Probablemente fue calculado utilizando el algoritmo
que hoy se conoce com el método Babilónico.

La explicación de este algoritmo puede ser deducida a partir de un
[rectángulo](https://es.wikipedia.org/wiki/C%C3%A1lculo_de_la_ra%C3%ADz_cuadrada#Algoritmo_babil%C3%B3nico)
con area igual al numero que se le desea calcular el area y a través de un
proceso iterativo convertirlo en un cuadrado con la misma area. Aquí deduciremos
el mismo algoritmo a partir de un método numérico para encontrar los ceros de la
función $f(x)=x^2 - S$ (¿puedes mostrar porque esta función?). Para encontrar
numéricamente los ceros de una función existen diversos métodos, uno de los mas
populares es el el método de
[Newton-Raphson](https://es.wikipedia.org/w/index.php?title=M%C3%A9todo_de_Newton-Raphson)
(a veces llamado simplemente de Newton). En este articulo deduciremos la formula
del método Babilónico y lo implementaremos en Python. Voy a asumir que ya tienen
un conocimiento básico de las librerías [Numpy](https://www.numpy.org) y
[Matplotlib](https://www.matplotlib.org)

## Metodo de Newton-Raphson

Este método de Newton-Raphson se vasa en buscar los ceros de la función a partir
de una serie de aproximaciones lineales, cada vez más cercanas al cero real.

![Animación del método de
Newton](https://upload.wikimedia.org/wikipedia/commons/e/e0/NewtonIteration_Ani.gif)

Como ya mencionamos los ceros de la función $f(x)=x^2 - S$ son $\pm\sqrt{S}$ por
lo tanto si podemos aproximar con este método sus ceros obtendremos la raíz que
estábamos buscando.


```python
import matplotlib.pyplot as plt
import numpy as np

S = 2
x = np.linspace(-1, 3, 100)

def f(x, S=2):
    return x**2 - S

plt.plot(x, f(x))
plt.grid()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
```


![png](/assets/posts/metodo-babilonico/output_1_0.png)


El primer paso es partir de un valor inicial $x_0$. Luego podemos aproximar la
función en este punto con su linea tangente. Usando la derivada sabemos que la
recta tangente a este punto es

$$ f(x) \approx f'(x_0)(x - x_0) + f(x_0) $$

Luego podemos encontrar una nueva aproximación para el cero despejando $x$ de la
función aproximada.

$$x_1 = x_0 - f(x_0)/f'(x_0)$$

Finalmente remplazando con la función $f(x)=x^2 - S$ encontramos que luego de
$k$ iteraciones una aproximación para la raíz de $S$ esta dada por las
siguientes ecuaciones (¿puedes ver porque?)

$$x_{k} = \frac{S+x_{k-1}^2}{2x_{k-1}}$$

$$\sqrt{S} =  \lim_{k \rightarrow \infty}x_k$$


```python
def f_prime(x):
    return 2*x

x0 = 2
plt.scatter([x0], [f(x0)], 50)
plt.plot(x, f(x))
plt.plot(x, f_prime(x0)*(x - x0) + f(x0))
plt.grid()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
```


![png](/assets/posts/metodo-babilonico/output_3_0.png)


## Implementación en Python

Si buscamos la raíz cuadrada de $2$ podemos partir con $x_0=2$ y usando las
ecuaciones que encontramos en la sección anterior buscar una aproximación cada
vez mas cercana al valor real.


```python
S = 2
x0 = 2
x_n = [x0] # guardaremos la aprroximacion de cada iteracion
for i in range(3):
    x_prev = x_n[-1] # el ultimo elemento de la lista
    x_next = (S + x_prev**2) / (2*x_prev)
    x_n.append(x_next)

print(x_n)
print(x_n[-1])
print(f"Error: {x_n[-1] - np.sqrt(S)}")
print(np.sqrt(2))
```

    [2, 1.5, 1.4166666666666667, 1.4142156862745099]
    1.4142156862745099
    Error: 2.1239014147411694e-06
    1.4142135623730951


¡Listo! Ya con solo 3 iteraciones ya podemos encontrar la raíz correcta a 5
decimales, y si tan solo iteramos dos veces más ya tenemos la respuesta a 12
decimales.

Un parámetro importante para el método de Newton es el punto de partida $x_0$.
Prueba con distintos valores y observa que para un numero pequeño de iteraciones
el algoritmo no es capaz de llegar a la respuesta si el punto de partida es muy
lejano al real.

Las calculadoras y computadores implementan aproximaciones para poder garantizar
una rápida convergencia. Por ahora solo implementaremos parámetros extras que
controlan el numero de iteraciones y la precisión de la respuesta. Lo que
hacemos es iterar todas las veces que sea necesario hasta que la distancia entre
la aproximación actual y la respuesta correcta sea menor a un numero pequeño
`epsilon`. Por otro lado independiente de la calidad de la aproximación no
haremos más de `maxiter` iteraciones.


```python
def sqrt(S, x0=None, maxiter=100, epsilon=1e-6):
    if x0 is None:
        x0 = S
    i= 0
    while abs(x0**2-S) > epsilon and i < maxiter:
        x0 = (S + x0**2) / (2*x0)
        i = i + 1
    return x0

print(sqrt(2))
```

    1.4142135623746899


En este articulo aprendimos como deducir el metodo Babilónico para encontrar
raíces cuadradas. El metodo de Newton-Rapson utilizado se puede aplicar para
encontrar las soluciones de una gran cantidad de ecuaciones usadas en la
practica incluyendo aplicaciones en optimización. Puedes descargar este articulo
como un cuaderno de Jupyter
[aquí](/assets/posts/metodo-babilonico/Metodo-de-Babilonia-para-calcular-raices-cuadradas.ipynb)
