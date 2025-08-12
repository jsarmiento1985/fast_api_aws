from pydantic import BaseModel, Field, Extra
from typing import Optional

class Enpoint(BaseModel):
    CODIGO: int
    
    model_config = {
        "extra": "forbid"  # ❌ No se permiten campos no definidos como 'RACK'
    }
    