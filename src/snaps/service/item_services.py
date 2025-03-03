from snaps.database import inmemory
from snaps.models import schemas


class ItemService:
    def __init__(self, db: inmemory.Database) -> None:
        self.db = db

    def create_item(self, item: schemas.ItemSchema) -> None:
        if self.db.includes(item):
            raise ConflictError
        self.db.add(item.id, item)


class ConflictError(BaseException): ...
