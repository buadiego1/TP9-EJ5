# pyrefly: ignore [missing-import]
from pydantic import BaseModel, ConfigDict


# =========================
# LUGAR
# =========================

class LugarCreate(BaseModel):
    nombre: str
    direccion: str


class LugarResponse(BaseModel):
    id: int
    nombre: str
    direccion: str

    model_config = ConfigDict(from_attributes=True)


# =========================
# SECTOR
# =========================

class SectorCreate(BaseModel):
    nombre: str
    descripcion: str | None = None


class SectorResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

    model_config = ConfigDict(from_attributes=True)


# =========================
# EVENTO
# =========================

class EventoCreate(BaseModel):
    nombre: str
    fecha: str
    descripcion: str | None = None


class EventoResponse(BaseModel):
    id: int
    nombre: str
    fecha: str
    descripcion: str | None = None

    model_config = ConfigDict(from_attributes=True)


# =========================
# CLIENTE
# =========================

class ClienteCreate(BaseModel):
    nombre: str
    email: str


class ClienteResponse(BaseModel):
    id: int
    nombre: str
    email: str

    model_config = ConfigDict(from_attributes=True)