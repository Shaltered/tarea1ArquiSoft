# tarea1ArquiSoft
 Tarea1
# Pasos para iniciar el proyecto
1. Para correr el repositorio, hay que abrir una terminal desde la ruta "\tarea1ArquiSoft-main\tarea1ArquiSoft-main\fastapi_microservices"
2. Desde ahí se escribe el comando "docker-compose up -d --build" (Recordar que el docker debe estar encendido).
3. Luego cuando todos los contenedores esten iniciados y funcionando, se ingresa por un navegador a: http://localhost:3000
4. Desde ahí se selecciona como data source a Loki con la url: "http://loki:3100"
5. De ahí se abre el dashboard y un nuevo panel, agregando una nueva Query, esta siendo: {job="fastapi-logs"}
6. Ahora se pueden hacer peticiones a los microservicios buscando estas URLs: http://localhost:8000 , http://localhost:8001
7. Finalmente se puede refrescar el panel y apareceran los logs

# Como cerrar el proyecto
1. Desde la misma terminal anterior, se puede usar el comando "docker-compose down" o hacerlo desde la misma aplicacion de Docker
