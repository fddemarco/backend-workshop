import typing

import fastapi
from fastapi import responses

from snaps import schemas

Database = dict[str, schemas.ItemSchema]

ITEMS_ENDPOINT = "/items"
DATABASE: Database = {}
app = fastapi.FastAPI()


def get_database() -> Database:
    return DATABASE


@app.post(
    ITEMS_ENDPOINT,
    response_model=schemas.ItemSchema,
    responses={409: {"model": schemas.Message}, 201: {"model": schemas.ItemSchema}},
)
def read_item(
    item: schemas.ItemSchema,
    database: typing.Annotated[Database, fastapi.Depends(get_database)],
) -> responses.JSONResponse:
    if item.id in database:
        return responses.JSONResponse(
            status_code=409,
            content=schemas.Message(message="Item already exists!").model_dump(),
        )
    database[item.id] = item
    return responses.JSONResponse(status_code=201, content=item.model_dump())
