Title: Restaurando passwords.
Date: 2021-09-22 21:00
Slug: restaurando-passwords
Authors: ivan
tags: tips, linux, pass, productividad
Cover: https://images.pexels.com/photos/4985505/pexels-photo-4985505.jpeg




Hoy en día existen muchas opciones para almacenar contraseñas en internet, pero peculiarmente yo utilizo el administrador de contraseñas estándar en unix: **pass.**

El fin de semana, me llego mi nuevo ssd para mi equipo y me dedique a instalar  **Debian11** (¡chulada! 😍)  y lo mas importante para mi en ese momento era tener mis contraseñas disponibles en mi nueva instalación.

Así que me puse a investigar como llevarlo acabo, te comparto los pasos para que los puedas replicar cuando te encuentres en una situación similar.  

- **Haz un backup de tus passwords:**
    - Instala la extensión [https://github.com/8go/pass-backup](https://github.com/8go/pass-backup)
    - Esta extensión te genera un zip con tus passwords, este lo deberás copiar a tu nueva maquina o guárdalo en un usb.
- **Exporta tu secret-key gpg:**

    *Esto es importante por que la **secret-key gpg** es con la que están encriptadas tus contraseñas.*

```bash
gpg --export-secret-keys > mi_backup.gpg
```

- **Importa tu secret-key gpg a tu nueva instalación:**

```bash
gpg --import path/to/secret-key-gpg
```

- **Instala pass en tu equipo:**

```bash
sudo apt-get install pass
```

- **Inicializa pass:**

```bash
pass init <id_secret_key_gpg>
```

- Verifica que en el archivo **.gpg_id, sea el id de tu secret_key**

```bash
~.password-store/.gpg_id 
# El folder .password-store se genera cuando inicializas pass
```

- Descomprime tu backup de passwords en **.password-store**
- Una vez tengas tus passwords listas, podras empezar a utilizarlas.

```bash
pass # Lista todas tus contraseñas
```

**Conclusión**

Esta puede ser una manera de como compartir las contraseñas entre tus equipos personales, de seguro hay maneras mas eficaces, por ahora esta, me ayudo bastante con mi objetivo. 

Igual  te dejo unos recursos por si deseas profundizar en el tema:

- [https://www.passwordstore.org/](https://www.passwordstore.org/)
- [https://git.zx2c4.com/password-store/about/#EXTENDED GIT EXAMPLE](https://git.zx2c4.com/password-store/about/#EXTENDED%20GIT%20EXAMPLE)

Si tienes dudas/comentarios, con gusto puedes mandarme un DM a [LinkedIn](https://www.linkedin.com/in/ivanlopz/) o [Twitter](https://twitter.com/BawbamGeek). 😉