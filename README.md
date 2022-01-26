# api_test

La app esta creada en lenguaje Python con el framework django.

la parte front esta conformada por las siguientes plantillas

- Welcome.html
es la plantilla principal del proyecto, en ella se ve una tabla con los datos requeridos. tiene los enlaces que completan las operaciones CRUD, el link 
para crear un nuevo usuario esta disponible en laparte superior, y al ingresar usuarios se van listando en la tabla. En frente de cada registro quedan 
diponibles los link para ver el detalle del registro, el de actualizar y el de eliminar registro
tambien hay un link para filtrar los registros existentes registros

- detail.html
muestra en detalle el registro seleccionado 

- edit.html
permite la modificacion del registro seleccionado

- new.html
permite la creacion de un nuevo registro

- list.html
muestra los registros existentes y permite el filtro segun el parametro seleccionado

El gestor de base de datos usado fue postgreSQL

todas las plantillas tienen link para regresar al inicio

todas la vistas estan basadas en clases, sguiendo el patron de diseño MVT






