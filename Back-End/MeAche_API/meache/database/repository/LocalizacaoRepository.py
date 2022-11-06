from database.config import session as connection
from database.models import LocalizacaoModel
from schemas import LocalizacaoSchema
from sqlalchemy import delete, insert, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class LocalizacaoRepository:
    async def store(localizacao: LocalizacaoSchema) -> LocalizacaoModel | None:
        async with connection() as session:
            session: Session

            stmt = LocalizacaoModel(
                localizacao=localizacao.localizacao,
            )

            session.add(stmt)
            await session.commit()

            return stmt

    async def show(id: int) -> LocalizacaoModel | None:
        async with connection() as session:
            session: Session

            stmt = select(LocalizacaoModel).where(LocalizacaoModel.id == id)

            localizacao = await session.execute(stmt)
            return localizacao.scalars().first()

    async def index() -> list[LocalizacaoModel]:
        async with connection() as session:
            session: Session

            stmt = select(LocalizacaoModel)
            localizacoes = await session.execute(stmt)
            localizacoes = localizacoes.scalars().all()

            return localizacoes

    async def edit(localizacao: LocalizacaoSchema) -> LocalizacaoModel | None:
        async with connection() as session:
            session: Session

            stmt = (
                update(LocalizacaoModel)
                .where(LocalizacaoModel.id == localizacao.id)
                .values(
                    localizacao=localizacao.localizacao,
                )
            )

            await session.execute(stmt)
            await session.commit()

            return await LocalizacaoRepository.show(localizacao.id)

    async def delete(id: int) -> None:
        async with connection() as session:
            session: Session

            stmt = delete(LocalizacaoModel).where(LocalizacaoModel.id == id)

            await session.execute(stmt)
            await session.commit()
