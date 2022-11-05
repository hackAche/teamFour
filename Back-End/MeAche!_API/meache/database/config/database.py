from database.models import Base

from .connection import engine


async def create_database() -> bool:
    """Create DataBase.

    Nesta função nós fazemos a criação do banco de dados.

    Returns:
        bool: Retornamos se foi efetuado o
        serviço de forma correta.
    """
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        return True
    except Exception as erro:
        print(f'Erro:{erro}')
        return False


async def delete_database() -> bool:
    """Delete DataBase.

    Nesta função nós fazemos a exclusão do banco de dados.

    Returns:
        bool: Retornamos se foi efetuado o
        serviço de forma correta.
    """
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
        return True
    except Exception as erro:
        print(f'Erro:{erro}')
        return False


async def reset_database() -> bool:
    """Reset DataBase.

    Nesta função nós fazemos a exclusão e criação do banco de dados.

    Returns:
        bool: Retornamos se foi efetuado o
        serviço de forma correta.
    """
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)
        return True
    except Exception as erro:
        print(f'Erro:{erro}')
        return False
