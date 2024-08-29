<<<<<<< HEAD
# Welcome to DnD-AI!


Each year, 10 million Dungeons and Dragons sessions are created, but did you know that more than half of these cannot take place due to a `lack of a Dungeon Master?` Dungeons and Dragons is a game that relies entirely on the imagination of its players, and among them, the Dungeon Master is `the one who creates the story` the players will follow, develops characters, their abilities, monsters, maps, and items – essentially, `the heart of the game`. We depend heavily on them, and there isn't always someone willing to take on the role.

What if we replaced them with an `artificial intelligence` that is available at all times? One that allows you and your friends to play a quality session whenever you want, `generating the map and enemies` automatically. That's us, DnD-AI, and we want to offer you this new way of playing – much more focused on immediate gameplay and with a faster pace.

Unlike similar ideas, we have various visual enhancements, such as `real-time map` visualization and the `generation of images` for the epic scenes that, until now, you could only imagine.

`Our wiki:` https://github.com/QuitoTactico/DnD-AI/wiki

`Our backlog:` https://github.com/users/QuitoTactico/projects/1

## To run *(do the pip install if it's your first time running the project):*

```
pip install -r "requirements.txt"
python manage.py runserver
```

## Software requirements

- Python 3.12.X (3.11.X and below are not supported)
- The needed dependencies and libraries defined in requirements.txt. To get them, run ```pip install -r "requirements.txt"```

## AI usage requirements

- For image generation is needed either a `OpenAI API key` or a `HuggingFace API key`.  
- For action interpretation, storytelling and campaign's info providing, a `Google Gemini API key` is needed. OpenAI GPT option will be re-added in the future.

You can provide this keys either creating a file called `api_keys.env` on the root dir of the project.

```
# api_keys.env
# on root dir of the project

openai_api_key = 
hf_api_key = 
gemini_api_key = 
```

Or a file called `API.py` on `/DnD_AI/` (the application, not the project). At the same level of `functions_AI.py`, the file that uses the api keys.
```
# API.py
# on same folder as /DnD_AI/functions_AI.py

openai_api_key = " "
hf_api_key = " "
gemini_api_key = " "
```

In any case, `the game is still playable with some (or none) of the API keys`. While AI generated images being replaced with placeholder images and action inputs not being interpreted, but supporting the use of commands instead.

## What's should to be seen:

![image](https://github.com/QuitoTactico/DnD-AI/assets/99926526/4bac83d7-8e10-4661-bfef-7cbe5681a18f)

![image](https://github.com/QuitoTactico/DnD-AI/assets/99926526/21186308-4e1e-4799-bc64-f393180639c0)

https://github.com/QuitoTactico/DnD-AI/assets/99926526/f426ac7c-4650-45de-a765-424f47cc1a3c


## Created by:
> - [Esteban Vergara Giraldo](https://github.com/QuitoTactico)
> - [Miguel Angel Cock Cano](https://github.com/MiguelCock)
> - [Sebastian Salazar Osorio](https://github.com/Sebasalazaro)
>
> For the EAFIT course: Integrator project 1
=======
## Actividad 2 (Revisión autocrítica): 

Mencionen aspectos de su proyecto, relacionados con los 
parámetros de calidad vistos en clase (Usabilidad, Compatibilidad, Rendimiento, Seguridad), 
resaltando aspectos que cumplan estos parámetros y aspectos a mejorar. Incluya aspectos 
donde pueda aplicar inversión  

### *Usabilidad:*

Aspectos Positivos: ¿Qué tan fácil es para los usuarios entender y usar el sistema? ¿Hay una buena documentación o una interfaz amigable?
Aspectos a Mejorar: ¿Existen partes del sistema que podrían ser más intuitivas? ¿Hay alguna mejora que podría hacer la experiencia del usuario más fluida?
Archivos a Revisar: Archivos de plantilla (HTML, CSS), documentación del proyecto, comentarios en el código.


### *Compatibilidad:*

Aspectos Positivos: ¿El sistema funciona bien en diferentes navegadores, dispositivos o sistemas operativos?
Aspectos a Mejorar: ¿Hay problemas de compatibilidad que deberían abordarse? ¿Qué cambios serían necesarios para mejorar la compatibilidad?
Archivos a Revisar: Archivos CSS, archivos de configuración de navegadores.

### *Rendimiento:*

Aspectos Positivos: ¿El sistema responde rápidamente y maneja la carga adecuadamente?
Aspectos a Mejorar: ¿Hay cuellos de botella en el rendimiento? ¿Cómo se podría optimizar el rendimiento del sistema?
Archivos a Revisar: Consultas a la base de datos, código de vistas, archivos de configuración de caché.

### *Seguridad:*

Aspectos Positivos: ¿El sistema tiene medidas adecuadas de seguridad, como cifrado de datos o autenticación de usuarios?
Aspectos a Mejorar: ¿Existen vulnerabilidades conocidas? ¿Qué medidas de seguridad adicionales podrían implementarse?
Archivos a Revisar: Archivos de configuración de seguridad, código de autenticación.

## Actividad 3 (Inversión de Dependencias): 
Escoja alguna clase de su proyecto y realice una inversión de dependencia según lo visto en clase. Documente bien los cambios en el repositorio. 

* Se hizo en models.py en la clase Weapon. 
* Archivo repositories.py: Define la interfaz y la implementación para manejar la lógica de Weapon.
* Archivo models.py: Actualiza la clase Weapon para usar la interfaz IWeaponRepository.

## Actividad 4
Se hizo en el archivo views.py.
Proceso de Decisión
Elección del Patrón de Diseño:

Patrón Factory: Elegimos el patrón Factory porque la vista playerCreation realiza consultas directas a la base de datos para obtener armas, lo que puede complicar la vista y hacerla menos reutilizable. Al utilizar una factory, encapsulamos la lógica de creación y obtención de armas en un solo lugar, lo que mejora la separación de preocupaciones y facilita la mantenibilidad del código.
Mejoras Aportadas:

##### Modularidad: 
La lógica para obtener armas predeterminadas se encuentra en una factory separada, lo que facilita la prueba y el mantenimiento del código.

##### Reutilización: 
La factory WeaponFactory puede ser utilizada en otras partes del proyecto si se necesita obtener armas predeterminadas de manera similar.

##### Simplicidad: 
La vista playerCreation es más sencilla y centrada en su tarea principal, lo que mejora la legibilidad y la gestión del código.

##### Documentación de los Cambios:
* Archivo factories.py: Añade la WeaponFactory para manejar la creación y obtención de armas.
* Archivo views.py: Actualiza la vista playerCreation para utilizar la WeaponFactory.
>>>>>>> 6b7a768c3d598e5168f830ce4ec720a35e4c9f23
