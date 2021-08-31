Title: Template Method
Date: 2021-08-31 21:00
Slug: templated-method
Authors: Ivan Lopez


# Template Method

El template method es un patron de diseño de comportamiento que define el esqueleto de un algoritmo en una clase base y permite que otras subclases pueden sobreescribir sin modificar la estructura.

Para poder entenderlo de una mejor manera, pongamos de ejemplo un web scraper, donde extraes información de distintos sitios web. Bien cuando empiezas tu proyecto, el alcance es solo para extraer información de un solo sitio web y hasta ahí todo cool con el código, ¿pero que pasa si nos piden agregar mas sitios web para poder extraer información?

Mientras vas agregando el código para los demás sitios web, observas que tu código tiende a repetirse en algunas partes.