from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

async def manejar_excepciones(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    
    except RequestValidationError as ve:
        return JSONResponse(
            status_code=422,
            content={
                "error": True,
                "mensaje": "Error de validación",
                "detalle": ve.errors(),
                "valor": None
            }
        )
    except StarletteHTTPException as he:
        return JSONResponse(
            status_code=he.status_code,
            content={
                "error": True,
                "mensaje": he.detail,
                "valor": None
            }
        )
    except SQLAlchemyError as se:
        return JSONResponse(
            status_code=500,
            content={
                "error": True,
                "mensaje": f"Error de base de datos: {str(se)}",
                "valor": None
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": True,
                "mensaje": f"Error inesperado: {str(e)}",
                "valor": None
            }
        )