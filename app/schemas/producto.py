from pydantic import BaseModel, Field, Extra
from typing import Optional
"""
class Producto(BaseModel):
    #ID: Optional[int] = None
    CODIGO: int = Field(default=0, gt= 0)
    NAME: str = Field(default="New Product",min_length=5, max_length=50)
    PRICE: float = Field(default=0, ge= 100, le=10000)
    STOCK: int = Field(default=0, gt= 0)
"""    
class Producto(BaseModel):
    CODIGO: int
    NAME: str
    PRICE: float
    STOCK: int
    
    model_config = {
        "extra": "forbid"  # ❌ No se permiten campos no definidos como 'RACK'
    }
    