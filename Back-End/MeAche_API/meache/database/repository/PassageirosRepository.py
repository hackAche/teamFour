from database.config import session as connection
from database.models import PassageirosModel
from schemas import PassageirosSchema
from sqlalchemy import delete, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class PassageirosRepository:
    async def store(passageiro: PassageirosSchema) -> PassageirosModel | None:
        async with connection() as session:
            session: Session

            stmt = PassageirosModel(
                qtd_interesse=passageiro.qtd_interesse,
                qtd_pessoas=passageiro.qtd_pessoas,
            )

            session.add(stmt)
            await session.commit()

            return stmt

    async def show(id: int) -> PassageirosModel | None:
        async with connection() as session:
            session: Session

            stmt = select(PassageirosModel).where(PassageirosModel.id == id)

            passageiros = await session.execute(stmt)
            return passageiros.scalars().first()

    async def index() -> list[PassageirosModel]:
        async with connection() as session:
            session: Session

            stmt = select(PassageirosModel)
            passageiros = await session.execute(stmt)
            passageiros = passageiros.scalars().all()

            return passageiros

    async def edit(passageiros: PassageirosSchema) -> PassageirosModel | None:
        async with connection() as session:
            session: Session

            stmt = (
                update(PassageirosModel)
                .where(PassageirosModel.id == passageiros.id)
                .values(
                    qtd_interesse=passageiros.qtd_interesse,
                    qtd_pessoas=passageiros.qtd_pessoas,
                )
            )

            await session.execute(stmt)
            await session.commit()

            return await PassageirosRepository.show(passageiros.id)

    async def delete(id: int) -> None:
        async with connection() as session:
            session: Session

            stmt = delete(PassageirosModel).where(PassageirosModel.id == id)

            await session.execute(stmt)
            await session.commit()
