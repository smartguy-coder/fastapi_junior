from pydantic import BaseModel, Field


class Coin(BaseModel):
    title: str = Field(..., max_length=25)
    price: float = Field(..., ge=10)
    notes: str = None
