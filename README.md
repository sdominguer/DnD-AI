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

### Actividad 4
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

##### Documentación de los Cambios
* Archivo factories.py: Añade la WeaponFactory para manejar la creación y obtención de armas.
* Archivo views.py: Actualiza la vista playerCreation para utilizar la WeaponFactory.
