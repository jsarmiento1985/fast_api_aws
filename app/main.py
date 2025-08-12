from fastapi import FastAPI, Request
from fastapi import Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.routers.product import router as product_router
from app.routers.endpoint import router as endpoint_router
from app.middleware.error_handler import manejar_excepciones
from sqlalchemy import text
from .db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="JSSP (Rest API)",
    description="Servicios REST API de JSSP project",
    summary="JSSPproject",
    version="0.0.3",
    terms_of_service="#",
    contact={
        "name": "JSSP projects",
        "url": "https://www.jsspproject.com.co/",
        "email": "contacto@sjsspproyect.com.co",
    },
)




# Define los orígenes permitidos
origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://127.0.0.1:5500",
    "https://tu-dominio.com"
]

# Aplica el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # O usa ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],              # Permite todos los métodos HTTP
    allow_headers=["*"],              # Permite todos los encabezados
)

# Registrar middleware
app.middleware("http")(manejar_excepciones)

# Manejador de errores de validación de FastAPI (NO entra al middleware), errores de pydantic
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "mensaje": "Error de validación",
            "detalle": exc.errors(),
            "valor": None
        }
    )

@app.get("/", tags=["home"])
async def root(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"message": "Connected to PostgreSQL", "result": result.scalar()}


prefijo = "/api/v1"
app.include_router(product_router, prefix=prefijo)
app.include_router(endpoint_router, prefix=prefijo)
