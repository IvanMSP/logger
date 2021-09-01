Title: Template Method
Date: 2021-08-31 21:00
Slug: templated-method
Authors: ivan
tags: patterns, python



El template method es un patrón de diseño de comportamiento que define el esqueleto de un algoritmo en una clase base y permite que otras subclases puedan sobrescribir sin modificar la estructura.

![https://i.imgur.com/EM5pyis.png](https://i.imgur.com/EM5pyis.png)

Como puedes ver en el diagrama, se define una clase abstracta donde se define la función para el **template_method()**, que es donde se declara el orden de los demás métodos [***step_one(), step_two()...***]  y a su vez se declaran los métodos de ese **template_method()**, estos métodos pueden tener una implementación o pueden ser implementados en una clase concreta.

Las clases concretas [***Concrete Class A, Concrete Class B...***] pueden sobrescribir todos los métodos de **Abstract Class** pero no el **template_method()** .

**Contexto:**

Estos días he estado estudiando como extraer información de diferentes sitios web y  tuve un problema donde no podía extraer la información de la manera que había investigado, entonces  tuve que investigar otras formas de como extraer información. 

Es donde me puse a analizar un poco y pude obtener lo siguiente:

- Extraer la información de un sitio web, lo hago en varios pasos en orden, es decir:
    - Recibe una url
    - Realiza la request a la url
    - Obtiene el response
    - Del response obtiene el content
    - Del content obtengo las clases que necesito
    - La información que se obtiene la guardo en la db.
- La manera de extraer información de diferentes sitios, puede ser que utilice diferentes herramientas para llevarlo acabo,  pero podemos seguir los mismos pasos.

Llegando a la conclusión de que podia implementar **Template Method.** Si te das cuenta el problema tiene todas las características para poder llevar una implementación del patrón.

**Solución**.  

![https://i.imgur.com/h21T7oE.png](https://i.imgur.com/h21T7oE.png)

Creando la clase abstracta en python:

```python
from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
    Clase abstracta para definir nuestro template method para hacer scrapping
    de sitios webs.
    """

    def template_method(self) -> None:
        """
        Estos son los pasos necesarios para scrappear un sitio web.
        """
        self.make_request()
        self.get_content()
        self.get_data_from_classes()
        self.save_to_db()

    # Métodos implementados en la clase abstracta
    # Se aplican para todos los sitios web
    def save_to_db(self):
        """
        Método para guardar la informacion en la base de datos.
        """
        print(f"Guardando la informacion de: {self.url}")

    # Métodos abstractos que deben ser implementados en las subclases
    @abstractmethod
    def make_request(self) -> None:
        """
        Método que realiza la petición a la url del sitio web.
        args: url
        response: response from request to url
        """
        pass

    @abstractmethod
    def get_content(self) -> None:
        """
        Método que obtiene el contenido de la url del sitio web.
        args: response
        response: content from response of url
        """
        pass

    @abstractmethod
    def get_data_from_classes(self) -> None:
        """
        Método que obtiene la información solicitada.
        response: data
        """
        pass
```

Clases Concretas que heredan de la clase abstracta

```python
# Pattern
from pattern.base import AbstractClass

class WebSiteOne(AbstractClass):
    def __init__(self, url, classes):
        self.url = url
        self.classes = classes
        self.content = None
        self.response = None
        self.data = None

    def make_request(self) -> None:
        print(f"Realizando request a la url: {self.url} con BeatifulSoup")

    def get_content(self) -> None:
        print(f"Obteniendo el contenido de la url en la clase WebSiteOne")

    def get_data_from_classes(self) -> None:
        print(f"Extraer data desde la clase WebSiteOne")
```

```python
# Pattern
from pattern.base import AbstractClass

class WebSiteTwo(AbstractClass):
    def __init__(self, url, classes):
        self.url = url
        self.classes = classes
        self.content = None
        self.response = None
        self.data = None

    def make_request(self) -> None:
        print(f"Realizando request a la url: {self.url} con Xpath")

    def get_content(self) -> None:
        print(f"Obteniendo el contenido de la url en la clase WebSiteTwo")

    def get_data_from_classes(self) -> None:
        print(f"Extraer data desde la clase WebSiteTwo")
```

Para ejecutar nuestro **template method** debemos crear un cliente:

```python
# Pattern
from pattern.base import AbstractClass

def client_code(abstract_class: AbstractClass) -> None:
    """
    Cliente encargado de ejecutar nuestro template_method.
    """
    abstract_class.template_method()
```

Ejecutando el código:

```python
# Pattern
from pattern.client import client_code

# Owner
from websites.web_site_one import WebSiteOne
from websites.web_site_two import WebSiteTwo

if __name__ == "__main__":
    url = input("Ingresa la url: ")
    classes = input("Ingresa las clases a buscar en el sitio(separados por coma): ")
    list_classes = classes.split(", ")
    client_code(WebSiteOne(url, list_classes))
    print("###################\n")
    client_code(WebSiteTwo(url, list_classes))
```

Salida:

```bash
Ingresa la url: https://example.com
Ingresa las clases a buscar en el sitio(separados por coma): price, name, img
Realizando request a la url: https://example.com con BeatifulSoup
Obteniendo el contenido de la url en la clase WebSiteOne
Extraer data desde la clase WebSiteOne
Guardando la informacion de: https://example.com
###################

Realizando request a la url: https://example.com con Xpath
Obteniendo el contenido de la url en la clase WebSiteTwo
Extraer data desde la clase WebSiteTwo
Guardando la informacion de: https://example.com
```

Conclusión:

El implementar este patrón tienes sus ventajas como: Poder modificar algunas partes de un algoritmo sin la necesidad de tener que modificar lo todo y sin afectar otras partes, tener menos código duplicado.

Pero me han surgido preguntas ¿Que pasa si tenemos que extraer información de miles de sitios web? ¿Hasta que punto es sostenible tener una clase por sitio? ¿Que pasa si llegamos en ese punto de tener miles de sitios para extraer información? ¿Como lo podríamos refactorizar?, claro que estas preguntas nos las deberíamos hacer hasta alcanzar ese punto en nuestro sistema, por ahora caminemos paso a paso.

Si bien esta implementación se puede mejorar muchisimo, esta me ha ayudado a entender por mucho mejor el patrón. Espero que igual te ayude.

Te dejo el repositorio en **Github**: [Template-Method](https://github.com/IvanMSP/template-method)

Si tienes dudas/comentarios, con gusto puedes mandarme un DM a [LinkedIn](https://www.linkedin.com/in/ivanlopz/) o [Twitter](https://twitter.com/BawbamGeek). 😉