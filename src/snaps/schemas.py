import pydantic


class ItemSchema(pydantic.BaseModel):
    name: str
    id: str
    price: int


class Message(pydantic.BaseModel):
    message: str
