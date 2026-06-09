
from sqlalchemy.orm import Session
from .models import Producto
from .schemas import ProductoCreate

# Obtener todos los productos
def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

# crear un nuevo producto
def crear_producto(
    db: Session,
    producto: ProductoCreate
):
    nuevo_producto = Producto(**producto.model_dump())

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


# eliminar un producto por su ID
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

# actualizar un producto por su ID
def actualizar_producto(
    db: Session,
    producto_id: int,
    producto_data: ProductoCreate
):
    producto = db.query(Producto).filter(
        Producto.id == producto_id
    ).first()

    if producto is None:
        return None

    producto.nombre = producto_data.nombre
    producto.categoria = producto_data.categoria
    producto.precio = producto_data.precio
    producto.stock = producto_data.stock

    db.commit()
    db.refresh(producto)

    return producto