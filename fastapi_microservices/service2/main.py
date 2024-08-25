from fastapi import FastAPI
import logging

app = FastAPI()

# Configuración de logging para escribir en un archivo
logging.basicConfig(
    filename="/var/log/service2.log",  # Archivo de log donde se escribirán los logs
    level=logging.INFO,  # Nivel de log INFO
    format='%(asctime)s %(levelname)s %(message)s'  # Formato del log
)

logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World from Service 2"}

@app.get("/status")
def get_status():
    logger.info("Status endpoint accessed")
    return {"status": "Running"}
