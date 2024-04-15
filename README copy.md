# Drone Racing League

## Información del Equipo de Desarrollo

El proyecto del curso implica desarrollar una plataforma web altamente escalable para la International FPV Drone Racing League (IDRL). La plataforma permitirá a los pilotos aficionados de drones cargar sus videos de carreras FPV para que el público los vote. Los 24 videos con más votos representarán a su país en el FPV Enthusiast Tour - IDRL.

El objetivo general es aplicar principios de arquitectura de soluciones en la nube, centrándose en la escalabilidad de la aplicación. Se trabajarán en grupos de 4 personas para desarrollar la aplicación de forma incremental, integrando elementos arquitectónicos de la nube.

Los objetivos específicos incluyen desarrollar aplicaciones bajo el modelo de software como servicio (SaaS), implementar una aplicación altamente escalable en la nube pública y responder a los requerimientos técnicos para escalar la aplicación en capas web, de procesamiento y de datos.

El proyecto se dividirá en 5 entregas a lo largo de las semanas, cubriendo desde el desarrollo en un entorno tradicional hasta la migración a la nube pública y la implementación de una aplicación altamente escalable.

Se requerirá el uso de tecnologías como Python 3.10, Flask Framework, SQLAlchemy, Flask RESTful, Celery, Redis o RabbitMQ, PostgreSQL, Gunicorn, Nginx, entre otras, para desarrollar el backend REST de la aplicación web.

Es importante destacar que el proyecto se enfoca en el desarrollo del backend y otras partes de la infraestructura ya definidas y documentadas.

## Integrantes del Equipo de Desarrollo

1. Yojan Stiben Hungría
2.
3. 
4. 


# Guía de Instalación y Configuración

## Paso 1: Iniciar el Proyecto
Para iniciar el proyecto, use el siguiente comando en su terminal:
```bash 
docker compose up -d
```

## Paso 2: Importar la colección y las variables de entorno en Postman
Importe las colecciones de Postman que se han proporcionado para evaluar la API y confirmar que funciona correctamente

### Comandos útiles

```bash 
# Comando para eliminar contenedores, imágenes y volúmenes
docker-compose down -v --rmi all

# Comando para liberar memoria después de detener los contenedore, esto eliminará todos los datos
docker system prune -a --volumes


### Formato de json para pruebas manueales del consumidor
```json
    {
        "file_name": "",
        "file_path": "videos_cargados + video_name",
        "user_id": 1,
        "task_id": 1,
        "video_id": 1
    }
```
## Recursos Adicionales
