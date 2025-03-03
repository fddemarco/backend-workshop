from fastapi import responses

from snaps.models import schemas
from snaps.service import item_services


class ItemController:
    def __init__(self, service: item_services.ItemService) -> None:
        self.service = service

    def create_item(self, item: schemas.ItemSchema) -> responses.JSONResponse:
        try:
            self.service.create_item(item)
        except item_services.ConflictError:
            return responses.JSONResponse(
                status_code=409,
                content=schemas.Message(message="Item already exists!").model_dump(),
            )
        return responses.JSONResponse(status_code=201, content=item.model_dump())
