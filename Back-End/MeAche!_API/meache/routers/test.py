# -----------------------
# BIBLIOTECAS
# -----------------------
from fastapi import APIRouter, Response, status
from schemas import TestSchema

# -----------------------
# CONSTANTES
# -----------------------
router = APIRouter(prefix='/test', tags=['Test'])
# -----------------------
# CLASSES
# -----------------------
# -----------------------
# FUNÇÕES()
# -----------------------
@router.get('/', status_code=status.HTTP_200_OK, tags=['Test'])
async def index():

    return TestSchema(mensagem='Olá')


# -----------------------
# Main()
# -----------------------
# -----------------------
