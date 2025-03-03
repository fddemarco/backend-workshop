import typing

import fastapi

from snaps import schemas

ITEMS_ENDPOINT = "/items"

app = fastapi.FastAPI()


@app.get(ITEMS_ENDPOINT, status_code=201)
def read_item(
    item: typing.Annotated[schemas.ItemSchema, fastapi.Query()],
) -> schemas.ItemSchema:
    return item
