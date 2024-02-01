---
layout: post
title: "Fitting an ellipse to a polygon"
slug: "polygon"
date: 2024-01-31 16:00:00 -0300
math: true
categories: ["tutorial", "creative coding"]
tags: ["polygon", "tutorial" ]
description: I describe a method to calculate the moments of a polygon by only
    knowing the value of the vertices. The moments are then used to fit an
    ellipse on the polygon.
---

# Which direction does this shape point to?
As a human, it is natural to identify when a shape points in a certain
direction, but how do we do it algorithmically? In other words, in which
direction is this polygon pointing?

![Image of an N sided polygon pointing to the upper-right corner](/posts/polygon/polygon.png)

A way to find this direction is to fit an ellipse to the shape and use the major
axis as the direction it's pointing. Fitting an ellipse can be done by doing an
eigenvector decomposition of the covariance matrix. The covariance matrix is
defined as:

$$
\frac{1}{\mu_{xx}\mu_{yy} - \mu_{xy}^2}\begin{bmatrix}
\mu_{yy} & -\mu_{xy} \\\\
-\mu_{xy} & \mu_{xx}
\end{bmatrix} = U^TVU
$$

With $\mu_{ij}$ the normalized second order moments of the shape. This can be
calculated with the following integrals:

$$
A = \iint_P 1 dxdy \\\\
\alpha_x = \frac{1}{A} \iint_P x dxdy \\\\
\alpha_y = \frac{1}{A} \iint_P y dxdy \\\\
\alpha_{xx} = \frac{1}{A} \iint_P x^2 dxdy \\\\
\alpha_{yy} = \frac{1}{A} \iint_P y^2 dxdy \\\\
\alpha_{xy} = \frac{1}{A} \iint_P xy dxdy \\\\
\mu_{xx} = \frac{1}{A} \iint_P (x - \alpha_x)^2 dxdy = \alpha_{xx} - \alpha_x^2 \\\\
\mu_{yy} = \frac{1}{A} \iint_P (y - \alpha_y)^2 dxdy = \alpha_{yy} - \alpha_y^2 \\\\
\mu_{xy} = \frac{1}{A} \iint_P (x - \alpha_x)(y - \alpha_y) dxdy = \alpha_{xy} - \alpha_x\alpha_y
$$

Ok, so the question now is how to calculate these integrals. In this article, we
are interested in the case where the region $P$ is a $N$-sided polygon. A
polygon is best represented by a collection of intersecting lines that define
the border of the shape. This implies that it is easier to do operations on the
border rather that on the inside.

## Calculating the inside from the border: Green's Theorem
The final result of calculus, the fundamental theorem of calculus, say we can
calculate a process from the inside of a function (an integral) from a process
happening at the boundaries of the function. In more formal terms, the integral
of a function over the interval $[a, b]$ is equal to evaluating the function's
antiderivative at the boundaries. In math:

$$
\int_a^b \frac{d}{dx}f(x)dx = f(b) - f(a)
$$

Remarkably, this idea can be extended to more dimentions. One of the forms of
the fundamental theorem in 2D is Green's theorem. This theorem relates an
integral over a shape to a line integral over the border of the shape

$$
\iint_P \left( \frac{\partial M}{\partial x} - \frac{\partial L}{\partial y}  \right) dxdy
= \oint_{\partial P} (Ldx + Mdy)
$$

This means if we found the adequate functions $M$ and $L$ we can calculate the
integrals for the moments given above by just calculating a line integral over
the border. More over since we are dealing with polygons the border consist of
piecewise linear functions which make the line integrals particularly easy to
calculate.

## Calculating the area

For the area we need to find $M$ and $L$ such that

$$
 \frac{\partial M}{\partial x} - \frac{\partial L}{\partial y} = 1
$$

There are several options but here we would use $M = \frac{1}{2}x$ and
$L= -\frac{1}{2}y$. The line integral is therefore

$$
A = \iint_P 1 dxdy = \oint_{\partial P} \frac{1}{2}(-y dx + x dy)
$$

because the border is made of piecewise linear functions, the border can be
parametrized as:

$$
\begin{align}
x_i(t) &= x_{i-1} + t(x_i - x_{i-1}) \\\\
y_i(t) &= y_{i-1} + t(y_i - y_{i-1})
\end{align}
$$

with $t \in [0, 1]$. So the line integral is

$$
\begin{align}
A =&  \oint_{\partial P} \frac{1}{2}(-y dx + x dy) \\\\
=& \sum_{i=1}^N \frac{1}{2} \left( \int_0^1  ( x_{i-1} + t(x_i - x_{i-1}))(y_i - y_{i-1}) dt - \int_0^1  ( y_{i-1} + t(y_i - y_{i-1}))(x_i - x_{i-1}) dt \right) \\\\
=& \frac{1}{2}\sum_{i=1}^N \left( \frac{(x_i - x_{i-1})}{2}(y_i - y_{i-1}) - \frac{(y_i - y_{i-1})}{2}(x_i - x_{i-1}) \right) \\\\
=& \frac{1}{2} \sum_{i=1}^N x_{i-1}y_i - x_i y_{i-1}
\end{align}
$$

For the other moments, we can derive similar formulas. For complete derivations
see [this article](https://mv.in.tum.de/_media/members/steger/publications/1996/fgbv-96-04-steger.pdf).

$$
\alpha_x = \frac{1}{6A} \sum_{i=1}^N (x_{i-1} + x_i)(x_{i-1}y_i - x_i y_{i -1}) \\\\
\alpha_y = \frac{1}{6A} \sum_{i=1}^N (y_{i-1} + y_i)(x_{i-1}y_i - x_i y_{i -1}) \\\\
\alpha_{xx} = \frac{1}{12A} \sum_{i=1}^N (x_{i-1}^2 + x_{i-1} x_i + x_i^2)(x_{i-1}y_i - x_i y_{i -1}) \\\\
\alpha_{yy} = \frac{1}{12A} \sum_{i=1}^N (y_{i-1}^2 + y_{i-1} y_i + y_i^2)(x_{i-1}y_i - x_i y_{i -1}) \\\\
\alpha_{xy} = \frac{1}{24A} \sum_{i=1}^N (2x_{i-1}y_{i-1} + x_{i-1} y_i  + x_i y_{i-1} + 2x_iy_i)(x_{i-1}y_i - x_i y_{i -1}) \\\\
$$

With this formulas we can calculate the moments of any polygon by only knowing
its vertex points.

## Fitting the ellipse
Now that we have formulas for the moments of the polygon we can fit the ellipse
by diagonalizing the matrix

$$
\frac{1}{\mu_{xx}\mu_{yy} - \mu_{xy}^2}\begin{bmatrix}
\mu_{yy} & -\mu_{xy} \\\\
-\mu_{xy} & \mu_{xx}
\end{bmatrix} = U^TVU
$$

The eigenvelues, $\lambda_{1,2}$ are placed on the diagonal of the matrix $V$
and the eigenvectors in the matrix $U$. The main axes of the ellipse are given
by $a = 2/\sqrt{\lambda_1}$ and $b = 2/\sqrt{\lambda_2}$.


## Example

Now let's demonstrate this by fitting an ellipse to the shape from the start

![Same shape as above, with fitted ellipse and arrows showing the principal directions](/posts/polygon/polygon-ellipse.png)

In a more complete example, I fitted an ellipse to a Voronoi cell in an image.
And later render the ellipse as a fingerprint, simulating an artistic effect.
You can play with this application
[here](https://tito21.github.io/voronoi-fingerprint/).

![francis.png](/posts/polygon/francis.png)

