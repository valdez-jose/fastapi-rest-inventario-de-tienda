
from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    categoria: str
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int

    class Config:
        from_attributes = True