from fastapi import FastAPI
import logging

app = FastAPI()

# Configuración de logging para escribir en un archivo
logging.basicConfig(
    filename="/var/log/service1.log",  # Archivo de log donde se escribirán los logs
    level=logging.INFO,  # Nivel de log INFO
    format='%(asctime)s %(levelname)s %(message)s'  # Formato del log
)

logger = logging.getLogger(__name__)
logger.info("Microservicio 1 started")
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World from Service 1"}

@app.get("/status")
def get_status():
    logger.info("Status endpoint accessed 1")
    return {"status": "Running"}
