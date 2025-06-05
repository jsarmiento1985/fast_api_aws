from fastapi import APIRouter, Path, Query

from models.product import Product

router = APIRouter(prefix="/gestion",tags=["Productos"])

products = [
    {"id": 1, "name": "Product 1", "price": 2200, "stock": 12},
    {"id": 2, "name": "Product 2", "price": 4200, "stock": 1},
]

@router.get("/products")
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
def update_product(id: int, product: Product):
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