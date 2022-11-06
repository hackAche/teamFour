from database.config import session as connection
from database.models import (BusModel, LocalizacaoModel, PassageirosModel,
                             RotasModel)
from schemas import RotasSchema
from sqlalchemy import delete, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class RotasRepository:
    async def store(rota: RotasSchema) -> RotasModel | None:
        async with connection() as session:
            session: Session

            stmt = RotasModel(
                nome=rota.nome,
                bus_id=rota.bus_id,
                localizacao_id=rota.localizacao_id,
                passageiros_id=rota.passageiros_id,
            )

            session.add(stmt)
            await session.commit()

            return stmt

    async def show(id: str) -> RotasModel | None:
        async with connection() as session:
            session: Session

            stmt = select(RotasModel).where(RotasModel.id == id)

            bus = await session.execute(stmt)
            return bus.scalars().first()

    async def showPlaca(
        placa: str,
    ) -> list[tuple[RotasModel, BusModel, LocalizacaoModel, PassageirosModel]]:
        async with connection() as session:
            session: Session

            stmt = (
                select(
                    RotasModel, BusModel, LocalizacaoModel, PassageirosModel
                )
                .join(BusModel, RotasModel.bus_id == BusModel.id)
                .join(
                    LocalizacaoModel,
                    RotasModel.localizacao_id == LocalizacaoModel.id,
                )
                .join(
                    PassageirosModel,
                    RotasModel.passageiros_id == PassageirosModel.id,
                )
                .where(BusModel.placa == placa)
            )

            rotas_completas = await session.execute(stmt)
            rotas_completas = rotas_completas.all()

            return rotas_completas

    async def index() -> list[RotasModel]:
        async with connection() as session:
            session: Session

            stmt = (
                select(
                    RotasModel, BusModel, LocalizacaoModel, PassageirosModel
                )
                .join(BusModel, RotasModel.bus_id == BusModel.id)
                .join(
                    LocalizacaoModel,
                    RotasModel.localizacao_id == LocalizacaoModel.id,
                )
                .join(
                    PassageirosModel,
                    RotasModel.passageiros_id == PassageirosModel.id,
                )
            )
            buses = await session.execute(stmt)
            buses = buses.all()

            return buses

    async def edit(rota: RotasSchema) -> RotasModel | None:
        async with connection() as session:
            session: Session

            stmt = (
                update(RotasModel)
                .where(RotasModel.id == rota.id)
                .values(
                    nome=rota.nome,
                    bus_id=rota.bus_id,
                    localizacao_id=rota.localizacao_id,
                    passageiros_id=rota.passageiros_id,
                )
            )

            await session.execute(stmt)
            await session.commit()

            return await RotasRepository.show(rota.id)

    async def delete(id: int) -> None:
        async with connection() as session:
            session: Session

            stmt = delete(RotasModel).where(RotasModel.id == id)

            await session.execute(stmt)
            await session.commit()
