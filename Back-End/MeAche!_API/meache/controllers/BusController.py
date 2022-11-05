from database import BusModel, BusRepository
from fastapi import HTTPException, status
from schemas import BusSchema


class BusController:
    async def store(bus: BusSchema) -> BusModel:

        bus_exist = await BusRepository.show(bus.placa)

        if bus_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Ônibus com a placa ({bus.placa}) já existe!',
            )

        return await BusRepository.store(bus=bus)

    async def show(placa: str) -> BusModel:
        try:
            bus = await BusRepository.show(placa)
            print(bus)
            if bus:
                return bus
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Ônibus com a placa ({placa}) não cadastrado!',
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Placa ({placa}) não existente!',
            )

    async def index() -> list[BusModel]:
        return await BusRepository.index()
