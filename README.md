#Documentación

##Autores

+ Felipe Bedoya Castaño
+ Justo Fuentes Meléndez
+ Jesús Mendoza Lara
+ Christian Suárez Picón

##Descripcion

Mediante el uso de la API de Dropbox y la API de Gmail nuestro proyecto permite al usuario descargar sus correos y almacenarlos en su cuenta de Dropbox.
Mediante la API de Gmail accedemos a la cuenta de Gmail y descargarmos los correos.
Mediante la API de Dropbox accedemos a la cuenta de Dropbox y almacenamos los correos previamente descargados.

####NOTAS: 
+ Al intentar iniciar sesion en gmail por primera vez, google nos enviara un correo para comprobar si somos nosotros los que estamos intentando acceder al correo, debemos notificar que 	hemos sido nosotros y habilitar la opcion de “Acceso de aplicaciones menos segura”.
+ Hay que intalar el sdk de dropbox para python haciendo uso de la orden:

>                     pip install dropbox.

##Historico de cambios
###Planificación

Semana | Encargados | Tareas
-- | ---- | ---
Primera | Felipe, Justo, Jesús, Christian | Pensar qué proyecto vamos a hacer.
Segunda | Felipe, Jesús | Buscar información en la API de Dropbox, cómo logearse y subir ficheros.
Segunda | Justo, Christian | Buscar informacion en la API de Gmail, cómo logearse y cómo descargar ficheros adjuntos de correos.
Tercera | Felipe, Jesús | Elaborar la parte relacionada con Dropbox y realizar pruebas de funcionamiento.
Tercera | Justo, Christian| Elaborar la parte relacionada con Gmail y realizar pruebas de funcionamiento.
Tercera | Felipe, Justo, Jesús, Christian | Unir las partes de Dropbox y Gmail.  Realizar pruebas de funcionamiento. Realizar la documentación. Despliegue del proyecto en Github.

##Tarea adicionales
La aplicación realizada cuenta con autentificación tanto para Google como para Dropbox.
