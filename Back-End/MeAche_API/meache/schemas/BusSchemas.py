from typing import Optional

from pydantic import BaseModel, Field


class BusSchema(BaseModel):
    id: Optional[int] = Field(
        1,
        title='ID',
        description='ID do ônibus',
        gt=0,
    )
    nome: str = Field(
        'Nome do ônibus', title='Nome', description='Nome do ônibus', len=60
    )
    placa: str = Field(
        title='Placa',
        description='Placa do ônibus',
        len=7,
        regex='[a-zA-Z]{3}[0-9]{4}|[a-zA-Z]{3}[0-9]{1}[a-zA-Z]{1}[0-9]{2}',
    )
    capacidade: int = Field(
        10,
        title='Capacidade',
        description='Capacidade de pessoas no ônibus',
        gt=9,
        lt=80,
    )

    class Config:
        orm_mode = True
