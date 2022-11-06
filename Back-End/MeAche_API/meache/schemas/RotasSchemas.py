from typing import Optional

from pydantic import BaseModel, Field

from .BusSchemas import BusSchema
from .LocalizacaoSchemas import LocalizacaoSchema
from .PassageirosSchemas import PassageirosSchema


class RotasSchema(BaseModel):
    id: Optional[int] = Field(
        1,
        title='ID',
        description='ID do ônibus',
        gt=0,
    )
    nome: str = Field(
        'Nome da rota do ônibus',
        title='Nome da rota do ônibus',
        description='Nome da rota que o ônibus irá percorrer',
        len=60,
    )
    bus_id: int = Field(
        15,
        title='ID do ônibus',
        description='ID ta tabela que contem as informações do ônibus',
        gt=0,
    )
    localizacao_id: int = Field(
        15,
        title='ID da Localização',
        description='ID ta tabela que contem as informações de localização',
        gt=0,
    )
    passageiros_id: int = Field(
        15,
        title='ID dos dados dos Passageiros',
        description='ID ta tabela que contem os  dados dos Passageiros',
        gt=0,
    )

    class Config:
        orm_mode = True


class RotasInsertSchema(BaseModel):
    placa_bus: str = Field(
        title='Placa',
        description='Placa do ônibus',
        len=7,
        regex='[a-zA-Z]{3}[0-9]{4}|[a-zA-Z]{3}[0-9]{1}[a-zA-Z]{1}[0-9]{2}',
    )

    rota: str = Field(
        title='Nome da Rota',
        description='Nome da rota que irá percorrer',
    )

    localizacao: LocalizacaoSchema = Field(
        title='Dados da localização do ônibus',
        description='Dados específicos da localização do ônibus',
    )

    passageiros: PassageirosSchema = Field(
        title='Dados dos passageiros do ônibus',
        description='Dados específicos dos passageiros do ônibus',
    )

    class Config:
        orm_mode = True


class RotasGetSchema(BaseModel):
    bus: BusSchema = Field(
        title='Ônibus',
        description='Dados do ônibus',
    )

    rota: RotasSchema = Field(
        title='Dados da rota',
        description='Dados específicos da rota',
    )

    localizacao: LocalizacaoSchema = Field(
        title='Dados da localização do ônibus',
        description='Dados específicos da localização do ônibus',
    )

    passageiros: PassageirosSchema = Field(
        title='Dados dos passageiros do ônibus',
        description='Dados específicos dos passageiros do ônibus',
    )

    class Config:
        orm_mode = True
