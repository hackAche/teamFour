from sqlalchemy import (BigInteger, Column, DateTime, ForeignKey, SmallInteger,
                        String, func)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class BusModel(Base):
    __tablename__ = 'bus'

    id = Column(
        BigInteger, primary_key=True, autoincrement=True, nullable=False
    )
    nome = Column(String(60), nullable=False)
    placa = Column(String(7), nullable=False, unique=True)
    capacidade = Column(SmallInteger, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=func.current_timestamp(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )

    def __repr__(self):
        return f'[Tabela: {self.__tablename__}(id: {self.id})]'


class RotasModel(Base):
    id = Column(
        BigInteger, primary_key=True, autoincrement=True, nullable=False
    )
    nome = Column(String(60), nullable=False)
    bus_id = Column(BigInteger, ForeignKey('bus.id'), nullable=False)
    
    ultima_parada = Column(String(60), nullable=False)
    proxima_parada = Column(String(60), nullable=False)
    
    qtd_interesse = Column(SmallInteger, nullable=False)
    qtd_pessoas = Column(SmallInteger, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=func.current_timestamp(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )
