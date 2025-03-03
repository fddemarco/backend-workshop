import pydantic


class Item(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")
    name: str
    id: str
    price: int
