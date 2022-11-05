from os import getenv

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DRIVER_DATABASE = getenv('DRIVER_DATABASE')
USER_DATABASE = getenv('USER_DATABASE')
PASSWORD_DATABASE = getenv('PASSWORD_DATABASE')
HOSTNAME_DATABASE = getenv('HOSTNAME_DATABASE')
PORT_DATABASE = getenv('PORT_DATABASE')
NAME_DATABASE = getenv('NAME_DATABASE')

URL_DATABASE = (
    f'{DRIVER_DATABASE}://{USER_DATABASE}:{PASSWORD_DATABASE}@'
    f'{HOSTNAME_DATABASE}/{NAME_DATABASE}'
)

engine = create_async_engine(URL_DATABASE)

session = sessionmaker(
    engine, expire_on_commit=False, future=True, class_=AsyncSession
)
