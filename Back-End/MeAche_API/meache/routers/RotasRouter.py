from controllers import RotasController
from fastapi import APIRouter, status
from schemas import RotasGetSchema, RotasInsertSchema, RotasSchema

router = APIRouter(
    prefix='/rotas',
    tags=['Rotas'],
)


@router.post(
    '/store',
    status_code=status.HTTP_201_CREATED,
    # response_model=RotasGetSchema,
    tags=['store'],
)
async def store(rota_completa: RotasInsertSchema):
    return await RotasController.store(rota_completa)


@router.get(
    '/show/{id}',
    status_code=status.HTTP_200_OK,
    response_model=RotasGetSchema,
    tags=['show'],
)
async def show(id: int):
    return await RotasController.show(id=id)


@router.get(
    '/show/placa/{placa}',
    status_code=status.HTTP_200_OK,
    response_model=list,
    tags=['show'],
)
async def show(placa: str):
    return await RotasController.showPlaca(placa=placa)


@router.post(
    '/passageiro/{id}',
    status_code=status.HTTP_201_CREATED,
    tags=['add'],
)
async def add(id: int):
    return await RotasController.addPassageiro(id=id)


@router.post(
    '/interesse/{id}',
    status_code=status.HTTP_201_CREATED,
    tags=['add'],
)
async def add(id: int):
    return await RotasController.addinteresse(id=id)


@router.delete(
    '/passageiro/{id}',
    status_code=status.HTTP_202_ACCEPTED,
    tags=['remove'],
)
async def remove(id: int):
    return await RotasController.rmPassageiro(id=id)


@router.delete(
    '/interesse/{id}',
    status_code=status.HTTP_202_ACCEPTED,
    tags=['remove'],
)
async def remove(id: int):
    return await RotasController.rminteresse(id=id)
