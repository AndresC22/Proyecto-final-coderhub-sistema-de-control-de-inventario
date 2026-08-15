# Proyecto final Coderhub-Andres Cambero

* Titulo: Sistema de control de inventario de equipos

---
* Que es la aplicación y problemas resuelve: La aplicación es un sistema de control de inventario de equipos web ligero y diseñado para registrar, organizar, monitorear y gestionar los activos tecnológicos de una organización de manera rápida y accesible como pueden ser computadora, laptops, monitores entre otro. Solucionando casos de perdida de equipos por fallas de monitoreo por el uso de métodos manuales.

---
* Para quien fue pensado: Esta aplicación fue pensando en organizaciones e individuos que necesitan una solución ágil y fácil de manejar en la gestión como puedes ser pequeñas empresas e intuiciones ya sea los departamentos de soporte técnicos que se encargan de monitorear los activos tecnológicos en la empresa y su reparación.

---
* Funciones Principales (M.V.P):

-- *Primer flujo* Gestión de Accesos: Un sistema de login y registro básico con su validaciones con el fin solamente la persona encarga pueda manejarlo e ingresar al sistema.

-- *Segundo flujo* CRUD Completo y funcional: Este sistema permite y tiene la capacidad de crear registro, visualizar los registro de manera detalla, actualizar o modificar los registro y borrar los registro de los equipos.

-- *Tercer flujo* Ubicación y Clasificación: El sistema permite saber la ubicación de donde pertenece el equipo y clasificar el tipo de equipo, acompañado con la capacidad de subir una foto opcional para mejorar su identificación.

# Tecnologías:
* Lenguajes:

-- *Python(3.14.2)*

-- *HTML*

-- *CSS*

-- *Javascript*

*Librería:

-- *flask*

-- *Boostrap*

*Motor de plantilla:

-- *jinja2

*Base de datos:

-- *SQLITE*

# Instalacion:

* Paso 1: Clonar el repositorio publico copiando su link o también descargar el zid con el sistema completo

* Paso 2: Crea un entorno virtual para aislar las dependencias del proyecto como puede ser python -m venv env

* Paso 3: Activa el entorno virtual ejecutando este comando env\Scripts\activate

* Paso 4: Se debe de instalar flask una vez teniendo el entorno virtual mediante este comando pip install flask

* Paso 5 (opcional): Se puede instalar todas las dependencias necesarias de manera directa con el requirements.txt usando este comando pip install -r requirements.txt

# Uso:

Una vez instalado todas las dependencia y tener abierto un entorno virtual se deber de ingresar el siguiente comando python app.py

* AL ejecutarlo se debe copiar el http que de la consola y pegarlo en un navegador.
  
* Al hacerlo te enviara al login del donde se debe de ingresar el usuario y su clave o en caso contrario dar en registrar donde se podrá crear un usuario y su clave y posteriormente seras redireccionado al login para que puedas ingresarlos.

* Una vez que seas reconocido serás enviado al main donde podrás manejar el sistema de inventario permitiéndote ingresar, modificar, visualizar y eliminar los registro de los equipos

* Tras quedar satisfechos puede cerrar la sesión arriba del navbar para culminar la sesión ser direccionado al login

# Estrutura
- bd / *carpeta donde se ubica la base datos*
-- equipo.sql / *base de datos del sistema*

---
- conexion / *carpeta donde se ubica la conexion con la base de datos*
-- conexionDB.py / *archivo que llama y conecta con la base de datos*

---
 - controller / *carpeta donde el cotrollerEquipo*
-- controllerEquipo.py / *archivo que maneja las funciones y el manejo de la base de datos*

---
- static / assets *carpeta donde almacena los recuros como estilos, imagenes, iconos, y javascript*
- assets / css *carpeta donde se almacena los estilos y el bootstrap*
-- bootstrap.min.css - tooltip.css / *archivos bootstrap para los estilos*
-- custom_alert,css *archivo del estilo de las alertas*
-- style,css *archivo de estilos del sistema*

---
- assets / fotos_equipos *carpeta donde almacenan las imagenes ingresadas por el usuario*
- assets / icons *carpeta donde almacena los iconos*
  
---
- assets / js *carpeta donde almacena la función de las alert mediante javascript*
-- bootstrap.min.js *archivo javascript para bootstrap
-- alerta.js - loader.js / *archivos de javasscript para ejecutar una alerta*
  
---
- templates / accion *carpeta donde almacena la estructura de la funciones del crud*
-- add.html *archivo para la estructura del registro*
-- lista.html *archivo para la estructura de la tablas crud*
-- update.html *archivo para la estructura de la modificacion de la actualizacion*
-- view.html *archivo para la estrutura de la visualización detallada del registro*

---
- templates / inicio *carpeta donde almacena la estructura al ingresa al sistema*
-- alerta.html *archivo para la estructura de la alerta *
-- main.html *archivo para la estructura principal al ingresar al sistema*
-- navbar.html *archivo para la estructura del navbar superior*

---
- templates / loginregistro *carpeta donde almacena la estructura del login y registro*
-- login *archivo para la estructura del inicio de sesión del usuario *
-- register *archivo para la estructura del registro de usuario*

---
--app.py *archivo principal para ejecutar las rutas del sistema

---
requirements.txt *archivo con los requerimientos que posee*

---
.gitignore *archivo que indicara a git que archivo ignorar*

---
# Entidades base datos equipos
*Tabla equipos
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Clave primaria |
| usuario_id | INTEGER | FK → usuario(id) |
| marca | TEXT | Marcas de equipos |
| modelo | TEXT | Modelo de equipos|
| clase | Text | Clase o tipo de equipos |
| area | TEXT | Area que pertenece el equipo |
| observacion | TEXT | Observación del equipo|
| revisado | Text | Determina si el equipo fue revisado o no |
| foto | TEXT | Foto del equipo |

*Tabla usuario
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER | Clave primaria |
| nombre | Text | Nombre de usuario |
| clave | TEXT | Clave de usuario |


