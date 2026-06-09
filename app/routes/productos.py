
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Listar todos los productos
@router.get("/")
def listar_productos(
    db: Session = Depends(get_db)
):
    return crud.obtener_productos(db)

# Obtener un producto por su ID
@router.get("/{producto_id}")
def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    return crud.obtener_producto(db, producto_id)

# crear un nuevo producto
@router.post("/")
def crear_producto(
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db, producto)

# eliminar un producto por su ID
@router.delete("/{producto_id}")
def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    producto = crud.eliminar_producto(
        db,
        producto_id
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {
        "mensaje": "Producto eliminado correctamente"
    }

# actualizar un producto por su ID
@router.put("/{producto_id}")
def actualizar_producto(
    producto_id: int,
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    producto_actualizado = crud.actualizar_producto(
        db,
        producto_id,
        producto
    )

    if producto_actualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto_actualizado
