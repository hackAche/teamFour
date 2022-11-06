from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class LocalizacaoSchema(BaseModel):
    id: Optional[int] = Field(
        1,
        title='ID',
        description='ID da localização',
        gt=0,
    )
    localizacao: str = Field(
        title='Localização',
        description='Localização do ônibus em tempo real',
        len=17,
        regex='[0-9]{2}\.[0-9]{5}\, [0-9]{1}\.[0-9]{5}',
    )
    updated_at: Optional[datetime] = Field(
        datetime.now(),
        title='Ultima atualização do ônibus',
        description='Placa do ônibus',
    )

    class Config:
        orm_mode = True
