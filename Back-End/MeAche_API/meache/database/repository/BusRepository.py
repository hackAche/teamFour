from database.config import session as connection
from database.models import BusModel
from schemas import BusSchema
from sqlalchemy import delete, insert, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class BusRepository:
    async def store(bus: BusSchema) -> BusModel | None:
        async with connection() as session:
            session: Session

            stmt = insert(BusModel).values(
                nome=bus.nome,
                placa=bus.placa.upper(),
                capacidade=bus.capacidade,
            )

            await session.execute(stmt)
            await session.commit()

            return await BusRepository.show(bus.placa)

    async def show(placa: str) -> BusModel | None:
        async with connection() as session:
            session: Session

            stmt = select(BusModel).where(BusModel.placa == placa.upper())

            bus = await session.execute(stmt)
            return bus.scalars().first()
    
    async def showId(id:int) -> BusModel | None:
        async with connection() as session:
            session: Session

            stmt = select(BusModel).where(BusModel.id == id)

            bus = await session.execute(stmt)
            return bus.scalars().first()

    async def index() -> list[BusModel]:
        async with connection() as session:
            session: Session

            stmt = select(BusModel)
            buses = await session.execute(stmt)
            buses = buses.scalars().all()

            return buses

    async def edit(bus: BusSchema) -> BusModel | None:
        async with connection() as session:
            session: Session

            stmt = (
                update(BusModel)
                .where(BusModel.placa == bus.placa)
                .values(nome=bus.nome, capacidade=bus.capacidade)
            )

            await session.execute(stmt)
            await session.commit()

            return await BusRepository.show(bus.placa)

    async def delete(placa: str) -> None:
        async with connection() as session:
            session: Session

            stmt = delete(BusModel).where(BusModel.placa == placa)

            await session.execute(stmt)
            await session.commit()
