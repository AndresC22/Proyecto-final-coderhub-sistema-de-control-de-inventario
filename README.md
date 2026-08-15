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

* Tras quedar satisfechos puede cerrar la sesión arriba del navbar para ser direccionado al login

