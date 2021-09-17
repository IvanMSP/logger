Title: Pre-commit, un framework que te ayuda a ser mas productivo.
Date: 2021-09-13 21:00
Slug: pre-commit-un-framework-que-te-ayudara-a-ser-mas-productivo
Authors: ivan
tags: python, productividad



Cuando estas desarrollando alguna feature o estas haciendo fixes de algún proyecto, la actividad principal es que funcione como se espera el feature o que se arregle la incidencia en la que estas trabajando, no en revisar si tu código esta bien formateado o si seguiste el pep8.

Imagínate que te asignan un hotfix, lo trabajas y solucionas el problema, mandas tu pull request a tu lead, lo revisa y te rechaza por que tu código tiene espacios en blanco, no dejaste los espacios correspondientes en tus funciones o simplemente dejaste importaciones que no usaste. 😢😢 Y que esto te pase cada que mandas un pull request, a la larga, esto representaría tiempo perdido para ti, para tu lead y para tu empresa y/o producto. 🤔 

¡Hey! pero esta situación seria como un happy path, no en todos los lugares siguen estándares o tienen definidos sus procesos. Pero si estas en una situación parecida, atrévete a proponer  cosas que ayuden a mejorar sus procesos, ¡Tus compañeros te lo van agradecer! 🤗🥳

Bien, pues **pre-commit** te ayudara a mejorar esta tarea, pero primero te explicare un poco acerca de él. Es un framework para manejar y  mantener [hooks de git](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) que están escritos en diferentes lenguajes. En el cual, puedes configurar diferentes [hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) que te ayudaran con tareas como: *verificar si en tú código existen espacios en blanco, formatear tu código, ordenar tus imports, verificar si tus migraciones no han sido agregadas a git, si tienes keys privadas en tu proyecto, etc.* Puedes checar la lista de hooks disponibles en este [link.](https://pre-commit.com/hooks.html)

![https://i.imgur.com/8LTRN8T.png](https://i.imgur.com/8LTRN8T.png)

Imagen: Flujo de pre-commit


Para agregar pre-commit a nuestros proyectos hay que realizar los siguientes pasos:


- Instalar pre-commit en nuestro ambiente virtual.

```bash
pip install pre-commit
```

- Agregar el siguiente archivo: **.pre-commit-config.yaml**, a nivel raíz de tu proyecto, donde se definen los hooks que quieres utilizar en tu proyecto, en este caso agregaremos **black y flake8** :

```yaml
repos:
-   repo: https://github.com/ambv/black
    rev: 20.8b1
    hooks:
    - id: black
        language_version: python3.9.1
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.9.0
    hooks:
    - id: flake8
```

- Instalar los hooks en tu .git/ del proyecto:

```bash
pre-commit install
```

- Ahora **pre-commit** se ejecutara automáticamente cada que hagas un **commit**.


### Formateado de código (Black)

Black es una herramienta que te ayuda a formatear tu código python, es decir si olvidaste dejar los dos espacios entre una clase y otra, Black va a agregar esos espacios por ti. Esto te ayudara a concentrarte en cosas de mayor importancia para ti, para tu equipo y/o empresa.

Si quieres personalizar la configuración de black en tu proyecto debes agregar este archivo **black.toml**:

 

```bash
[tool.black]
line-length = 79
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

Te dejo el [link](https://black.readthedocs.io/en/stable/) a la documentación.  

### Flake8

Es una herramienta que te ayuda a que tu código cumpla con la guía de estilo [PEP8.](https://www.python.org/dev/peps/pep-0008/) [Un linter].

Si quieres personalizar la herramienta en tu proyecto, debes agregar el archivo **.flake8:**

```bash
[flake8]
ignore = E203, E266, E501, W503, F403, F401
max-line-length = 79
max-complexity = 18
select = B,C,E,F,W,T4,B9
```

Te comparto el [link](https://flake8.pycqa.org/en/latest/index.html) de la documentación.

### Conclusión

Espero que esta herramienta te ayude en mejorar tu productividad en tus proyectos y recuerda que si en tu equipo y/o empresa aún no lo usan, haz la propuesta de utilizarla. 😎

Si ya lo haz utilizado, seria genial que compartieras que hooks utilizas.  🥳

Por ultimo quiero agradecer a **Christian** por recomendarme esta herramienta. 🕶️

Si tienes dudas/comentarios, con gusto puedes mandarme un DM a [LinkedIn](https://www.linkedin.com/in/ivanlopz/) o [Twitter](https://twitter.com/BawbamGeek). 😉