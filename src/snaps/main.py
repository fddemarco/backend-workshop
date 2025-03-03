import typing

import fastapi
from fastapi import responses

from snaps.database import inmemory
from snaps.models import schemas

ITEMS_ENDPOINT = "/items"
app = fastapi.FastAPI()


@app.post(
    ITEMS_ENDPOINT,
    response_model=schemas.ItemSchema,
    responses={409: {"model": schemas.Message}, 201: {"model": schemas.ItemSchema}},
)
def read_item(
    item: schemas.ItemSchema,
    database: typing.Annotated[
        inmemory.Database, fastapi.Depends(inmemory.get_database)
    ],
) -> responses.JSONResponse:
    if database.includes(item):
        return responses.JSONResponse(
            status_code=409,
            content=schemas.Message(message="Item already exists!").model_dump(),
        )
    database.add(item)
    return responses.JSONResponse(status_code=201, content=item.model_dump())
