from snaps.models import schemas


class Database:
    def __init__(self) -> None:
        self.data: dict[str, schemas.ItemSchema] = {}

    def clear(self) -> None:
        self.data.clear()

    def includes(self, item: schemas.ItemSchema) -> bool:
        return item.id in self.data

    def add(self, item: schemas.ItemSchema) -> None:
        self.data[item.id] = item


DATABASE = Database()


def get_database() -> Database:
    return DATABASE
