
from sqlalchemy.orm import Session
from .models import Producto
from .schemas import ProductoCreate

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

def crear_producto(
    db: Session,
    producto: ProductoCreate
):
    nuevo_producto = Producto(**producto.model_dump())

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto

def eliminar_producto(
    db: Session,
    producto_id: int
):
    producto = db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

    if producto is None:
        return None

    db.delete(producto)
    db.commit()

    return producto