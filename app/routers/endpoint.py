from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.schemas.endpoint import Enpoint
import httpx

router = APIRouter(prefix="/api", tags=["Api Tercero"])

@router.post("/call_api")
async def call_api(item: Enpoint):
    codigo = item.CODIGO

    # URL de la API externa de prueba
    url = f"https://jsonplaceholder.typicode.com/posts/{codigo}"

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()  # Lanza error si no es 200
            data = response.json()  # JSON de la API externa
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al llamar API externa: {str(e)}")

    return {
        "error": False,
        "mensaje": "Llamado al API fue exitoso.",
        "valor": data,  # Devuelve el JSON recibido de la API
    }



  