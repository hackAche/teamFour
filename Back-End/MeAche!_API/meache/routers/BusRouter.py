from controllers import BusController
from fastapi import APIRouter, HTTPException, Query, status
from schemas import BusSchema

router = APIRouter(
    prefix='/bus',
    tags=['Bus'],
)


@router.post(
    '/store',
    status_code=status.HTTP_201_CREATED,
    response_model=BusSchema,
    tags=['store'],
)
async def store(bus: BusSchema):
    return await BusController.store(bus=bus)


@router.get(
    '/show/{placa}',
    status_code=status.HTTP_200_OK,
    response_model=BusSchema,
    tags=['show'],
)
async def show(placa: str):
    return await BusController.show(placa=placa)


@router.get(
    '/index',
    status_code=status.HTTP_200_OK,
    response_model=list[BusSchema],
    tags=['index'],
)
async def show():
    return await BusController.index()
