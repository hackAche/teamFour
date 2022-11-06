from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PassageirosSchema(BaseModel):
    id: Optional[int] = Field(
        1,
        title='ID',
        description='ID do ônibus',
        gt=0,
    )
    qtd_interesse: Optional[int] = Field(
        15,
        title='Quantidade de interessados',
        description='Quantidade de pessoas interessadas em pegar essa rota',
        gt=0,
    )
    qtd_pessoas: Optional[int] = Field(
        4,
        title='Quantidade de pessoas no ônibus',
        description='Quantidade de pessoas no ônibus dessa rota',
        gt=0,
    )
    updated_at: Optional[datetime] = Field(
        datetime.now(),
        title='Ultima atualização do ônibus',
        description='Placa do ônibus',
    )

    class Config:
        orm_mode = True
