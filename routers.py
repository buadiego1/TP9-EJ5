# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException, status
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models
import schemas

# =============================================================================
# LUGAR ROUTER
# =============================================================================
lugar_router = APIRouter(
    prefix="/lugares",
    tags=["Lugares"]
)


@lugar_router.post(
    "/",
    response_model=schemas.LugarResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo lugar",
    description="Crea un nuevo registro de lugar en la base de datos."
)
def crear_lugar(lugar: schemas.LugarCreate, db: Session = Depends(get_db)):
    nuevo_lugar = models.Lugar(
        nombre=lugar.nombre,
        direccion=lugar.direccion
    )
    db.add(nuevo_lugar)
    db.commit()
    db.refresh(nuevo_lugar)
    return nuevo_lugar


@lugar_router.get(
    "/",
    response_model=List[schemas.LugarResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los lugares",
    description="Devuelve la lista completa de lugares registrados."
)
def listar_lugares(db: Session = Depends(get_db)):
    return db.query(models.Lugar).all()


@lugar_router.get(
    "/{id}",
    response_model=schemas.LugarResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener un lugar por ID",
    description="Busca y devuelve un lugar específico según su identificador único."
)
def obtener_lugar_por_id(id: int, db: Session = Depends(get_db)):
    lugar = db.query(models.Lugar).filter(models.Lugar.id == id).first()
    if not lugar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lugar con ID {id} no encontrado"
        )
    return lugar


# =============================================================================
# SECTOR ROUTER
# =============================================================================
sector_router = APIRouter(
    prefix="/sectores",
    tags=["Sectores"]
)


@sector_router.post(
    "/",
    response_model=schemas.SectorResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo sector",
    description="Crea un nuevo sector en la base de datos."
)
def crear_sector(sector: schemas.SectorCreate, db: Session = Depends(get_db)):
    nuevo_sector = models.Sector(
        nombre=sector.nombre,
        descripcion=sector.descripcion
    )
    db.add(nuevo_sector)
    db.commit()
    db.refresh(nuevo_sector)
    return nuevo_sector


@sector_router.get(
    "/",
    response_model=List[schemas.SectorResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los sectores",
    description="Devuelve la lista completa de sectores registrados."
)
def listar_sectores(db: Session = Depends(get_db)):
    return db.query(models.Sector).all()


@sector_router.get(
    "/{id}",
    response_model=schemas.SectorResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener un sector por ID",
    description="Busca y devuelve un sector específico según su identificador único."
)
def obtener_sector_por_id(id: int, db: Session = Depends(get_db)):
    sector = db.query(models.Sector).filter(models.Sector.id == id).first()
    if not sector:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Sector con ID {id} no encontrado"
        )
    return sector


# =============================================================================
# EVENTO ROUTER
# =============================================================================
evento_router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"]
)


@evento_router.post(
    "/",
    response_model=schemas.EventoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo evento",
    description="Crea un nuevo evento en la base de datos."
)
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    nuevo_evento = models.Evento(
        nombre=evento.nombre,
        fecha=evento.fecha,
        descripcion=evento.descripcion
    )
    db.add(nuevo_evento)
    db.commit()
    db.refresh(nuevo_evento)
    return nuevo_evento


@evento_router.get(
    "/",
    response_model=List[schemas.EventoResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los eventos",
    description="Devuelve la lista completa de eventos registrados."
)
def listar_eventos(db: Session = Depends(get_db)):
    return db.query(models.Evento).all()


@evento_router.get(
    "/{id}",
    response_model=schemas.EventoResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener un evento por ID",
    description="Busca y devuelve un evento específico según su identificador único."
)
def obtener_evento_por_id(id: int, db: Session = Depends(get_db)):
    evento = db.query(models.Evento).filter(models.Evento.id == id).first()
    if not evento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Evento con ID {id} no encontrado"
        )
    return evento


# =============================================================================
# CLIENTE ROUTER
# =============================================================================
cliente_router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@cliente_router.post(
    "/",
    response_model=schemas.ClienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo cliente",
    description="Crea un nuevo cliente en la base de datos."
)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    nuevo_cliente = models.Cliente(
        nombre=cliente.nombre,
        email=cliente.email
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


@cliente_router.get(
    "/",
    response_model=List[schemas.ClienteResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los clientes",
    description="Devuelve la lista completa de clientes registrados."
)
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()


@cliente_router.get(
    "/{id}",
    response_model=schemas.ClienteResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener un cliente por ID",
    description="Busca y devuelve un cliente específico según su identificador único."
)
def obtener_cliente_por_id(id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {id} no encontrado"
        )
    return cliente
