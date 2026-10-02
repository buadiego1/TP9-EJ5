# pyrefly: ignore [missing-import]
from fastapi import FastAPI

from database import Base, engine
import models
from routers import (
    lugar_router,
    sector_router,
    evento_router,
    cliente_router
)


# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)


# Crear la aplicación
app = FastAPI(
    title="Sistema de Gestión de Eventos",
    description="API para gestionar lugares, sectores, eventos y clientes.",
    version="1.0.0"
)


# Registrar routers
app.include_router(lugar_router)
app.include_router(sector_router)
app.include_router(evento_router)
app.include_router(cliente_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }