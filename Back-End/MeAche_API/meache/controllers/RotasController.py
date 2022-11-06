from database import (BusRepository, LocalizacaoRepository,
                      PassageirosRepository, RotasModel, RotasRepository)
from fastapi import HTTPException, status
from schemas import RotasGetSchema, RotasInsertSchema, RotasSchema


class RotasController:
    async def store(rota_completa: RotasInsertSchema) -> RotasGetSchema:

        bus = await BusRepository.show(rota_completa.placa_bus)

        if not bus:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Ônibus com a placa ({rota_completa.placa_bus}) não está cadastrado',
            )
        try:
            if rota_completa.passageiros.qtd_pessoas > bus.capacidade:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'Quantidade de Passageiros maior que a capacidade',
                )
            localizacao = await LocalizacaoRepository.store(
                localizacao=rota_completa.localizacao
            )
            passageiros = await PassageirosRepository.store(
                passageiro=rota_completa.passageiros
            )
            rota = RotasSchema(
                nome=rota_completa.rota,
                bus_id=bus.id,
                localizacao_id=localizacao.id,
                passageiros_id=passageiros.id,
            )
            rotas = await RotasRepository.store(rota=rota)
            return {
                'bus': bus,
                'rota': rotas,
                'localizacao': localizacao,
                'passageiros': passageiros,
            }
        except Exception as Erro:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{Erro}',
            )

    async def show(id: int) -> RotasModel:
        try:
            rota = await RotasRepository.show(id=id)
            if rota:
                return rota
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Esta rota não está cadastrada!',
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Rota não existente!',
            )

    async def showPlaca(placa: str) -> RotasModel:
        try:
            bus = await BusRepository.show(placa)
            if bus:
                return await RotasRepository.showPlaca(placa=placa)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Ônibus com a placa ({placa}) não cadastrado!',
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Placa ({placa}) não existente!',
            )

    async def index() -> list[RotasModel]:
        return await RotasRepository.index()

    async def addPassageiro(id: int):
        rota = await RotasRepository.show(id)
        if not rota:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Rota não existente!',
            )
        passageiros = await PassageirosRepository.show(id=rota.passageiros_id)
        passageiros.qtd_pessoas += 1
        print(passageiros.qtd_pessoas)
        bus = await BusRepository.showId(rota.bus_id)
        if bus.capacidade >= passageiros.qtd_pessoas:
            await PassageirosRepository.edit(passageiros=passageiros)
            raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail=f'Adicionado mais pessoas',
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Quantidade de pessoas maior que a capacidade do ônibus!',
        )

    async def addinteresse(id:int):
        rota = await RotasRepository.show(id)
        if not rota:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Rota não existente!',
            )
        passageiros = await PassageirosRepository.show(id=rota.passageiros_id)
        passageiros.qtd_interesse += 1
        await PassageirosRepository.edit(passageiros=passageiros)
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail=f'Adicionado mais pessoas',
        )

    async def rmPassageiro(id:int):
        rota = await RotasRepository.show(id)
        if not rota:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Rota não existente!',
            )
        passageiros = await PassageirosRepository.show(id=rota.passageiros_id)
        passageiros.qtd_pessoas -= 1
        if 0 <= passageiros.qtd_pessoas:
            await PassageirosRepository.edit(passageiros=passageiros)
            raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail=f'Removido mais pessoas',
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Quantidade de pessoas menor que zero!',
        )

    async def rminteresse(id:int):
        rota = await RotasRepository.show(id)
        if not rota:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Rota não existente!',
            )
        passageiros = await PassageirosRepository.show(id=rota.passageiros_id)
        passageiros.qtd_interesse -= 1
        if 0 <= passageiros.qtd_interesse:
            await PassageirosRepository.edit(passageiros=passageiros)
            raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail=f'Removido mais pessoas',
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Quantidade de pessoas menor que zero!',
        )
