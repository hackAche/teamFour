from pydantic import BaseModel


class Test(BaseModel):
    mensagem: str

    class Config:
        orm_mode = True
