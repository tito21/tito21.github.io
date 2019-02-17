---
layout: post
title: "UCaccess: Extension para desbloquear artículos científicos"
slug: "UCaccess"
date: 2019-02-16 23:10:43 -0300
use_math: true
categories: ["ciencia", "extensiones"]
tags: ["firefox", "chrome"]
---

Cualquiera que ha intentado hacer una investigación sobre algún tema de investigación punta se habrá topado con que la mayoría de los artículos científicos están detrás de una barrera de pago.
Bastante se ha [escrito]("") sobre como esto limita el avance científico al limitar el acceso al conocimiento.
Esta frustración llevo a la creación de la popular pagina [sci-hub.tw](https:\\sci-hub.tw) para piratear papers.
Al margen de la legalidad de este tipo de paginas, estas tienen otras desventajas como no estar integrado a motores de busqueda y no poder mantener una misma URL por mucho tiempo.

Algo que no muchos saben es que muchas universidades tienen convenios con las editoriales para acceder al contenido y proven de un servidor proxy para que sus alumnos y académicos tengan acceso.
Generalmente el uso de este proxy es engorroso o desconocido por la comunidad.
Para solucionar esto en mi universidad ([PUC](https://uc.cl)) decidí crear una extension de navegador que permitiera automatizar el acceso a los artículos a través del proxy de la universidad.
La extensión esta disponible para [Google Chrome](https://chrome.google.com/webstore/detail/uc-access/leoijilpkelhgbhkneanedjffjhedcoa) y [Firefox](https://addons.mozilla.org/en-US/firefox/addon/uc-access/).
Esta diseñada usando la WebExtensions API por lo que debería funcionar en cualquier navegador que los soporte (ej.Opera, Edge, Brave, Vivaldi).

<div class="boxed">
<p>
Para usar la extension es necesario tener acceso a una cuenta de la Universidad Católica de Chile.
</p>
</div>

La aplicación esta bajo una licencia MIT y el código esta disponible [aquí](https://github.com/tito21/UCaccess).
Cualquier duda o sugerencia no duden en abrir  una *Issue* o enviarme un correo.