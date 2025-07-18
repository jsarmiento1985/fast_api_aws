from fastapi import APIRouter, Path, Query, APIRouter, Depends, HTTPException

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models.product import Product
from sqlalchemy.future import select
from app.schemas.producto import Producto


router = APIRouter(prefix="/gestion", tags=["Productos"])

products = [
    {"id": 1, "name": "Product 1", "price": 2200, "stock": 12},
    {"id": 2, "name": "Product 2", "price": 4200, "stock": 1},
]

""" @router.get("/products")
def get_products():
    return products

#parametros de ruta se usa path apra validar
@router.get("/products/{id}")
def get_product(id: int = Path(gt=0)):
    return list (filter( lambda item: item['id'] == id, products ))
 
#parametros query se usa Query para validar   
@router.get("/products/")
def get_products_by_stock(stock: int, price: float = Query(gt=0)):
     return list (filter( lambda item: item['stock'] == stock and item['price'] == price, products ))
    
@router.post("/products")
def create_product(product: Product):
    products.append(product) 
    return products   

@router.put("/products/{id}")
def update_product(id: int, product: Producto):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]['name'] = product.name
            products[index]['stock'] = product.stock
            products[index]['price'] = product.price
    return products

@router.delete("/products/{id}")
def delete_product(id: int):
        for item in products:
            if item['id'] == id:
                products.remove(item)
        return products
     """

""" @router.post("/new_product")
async def crear_producto(producto: Producto, db: AsyncSession = Depends(get_db)):
    try:
        nuevo_producto = Product(
            codigo=producto.CODIGO,
            name=producto.NAME,
            price=producto.PRICE,
            stock=producto.STOCK
        )
        db.add(nuevo_producto)
        await db.commit()
        await db.refresh(nuevo_producto)

        return {
            "error": False,
            "mensaje": "Producto creado exitosamente.",
            "valor": {
                "ID": nuevo_producto.id,
                "CODIGO": nuevo_producto.codigo,
                "NAME": nuevo_producto.name,
                "PRICE": float(nuevo_producto.price),
                "STOCK": nuevo_producto.stock
            }
        }

    except SQLAlchemyError as e:
        await db.rollback()
        return {
            "error": True,
            "mensaje": f"Ocurrió un error al guardar el producto: {str(e)}",
            "valor": None
        }

    except Exception as e:
        await db.rollback()
        return {
            "error": True,
            "mensaje": f"Error inesperado: {str(e)}",
            "valor": None
        } 
     """


@router.post("/new_product")
async def crear_producto(producto: Producto, db: AsyncSession = Depends(get_db)):
    nuevo_producto = Product(
        codigo=producto.CODIGO,
        name=producto.NAME,
        price=producto.PRICE,
        stock=producto.STOCK,
    )
    db.add(nuevo_producto)
    await db.commit()
    await db.refresh(nuevo_producto)

    return {
        "error": False,
        "mensaje": "Producto creado exitosamente.",
        "valor": {
            "ID": nuevo_producto.id,
            "CODIGO": nuevo_producto.codigo,
            "NAME": nuevo_producto.name,
            "PRICE": float(nuevo_producto.price),
            "STOCK": nuevo_producto.stock,
        },
    }
