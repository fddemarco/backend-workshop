import typing

import fastapi
from fastapi import responses

from snaps.controller import item_controllers
from snaps.database import inmemory
from snaps.models import schemas
from snaps.service import item_services

ITEMS_ENDPOINT = "/item"
app = fastapi.FastAPI()


@app.post(
    ITEMS_ENDPOINT,
    response_model=schemas.ItemSchema,
    responses={409: {"model": schemas.Message}, 201: {"model": schemas.ItemSchema}},
)
def create_item(
    item: schemas.ItemSchema,
    database: typing.Annotated[
        inmemory.Database, fastapi.Depends(inmemory.get_database)
    ],
) -> responses.JSONResponse:
    service = item_services.ItemService(database)
    controller = item_controllers.ItemController(service)
    return controller.create_item(item)
