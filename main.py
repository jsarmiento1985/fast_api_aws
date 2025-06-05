from fastapi import FastAPI

from routers.product import router as product_router
app = FastAPI()


@app.get("/", tags = ["home"])
def message():
    return "hello mundo "

prefijo = "/api/v1"
app.include_router(product_router, prefix=prefijo)