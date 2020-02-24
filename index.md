---
title: Hola, soy Alberto Di Biase
nav: false
---

Vivo en Santiago de Chile y estudio Ingeniería Biomédica en la Pontificia
Universidad Católica de Chile (UC). Cuando no estoy estudiando, escribo en esta
pagina sobre Python, Machine Learning, Wolfram Mathematica y otros temas.

$for(posts)$

<!-- Using /nowrap pipe to prevent pandoc inserting new lines -->

## [$posts.title/nowrap$]($posts.url/nowrap$)

::: sub-title
$posts.date$
:::

:::: description
$posts.description$
::::
$endfor$
