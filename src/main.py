import typing

import fastapi

from snaps import schemas

app = fastapi.FastAPI()


@app.get("/items")
def read_item(item: typing.Annotated[schemas.Item, fastapi.Query()]):
    return {"name": item.name, "id": item.id, "price": item.price}
