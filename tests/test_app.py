import pytest
from fastapi import testclient

from snaps import main, schemas


@pytest.fixture(name="app_client")
def fixture_app_client() -> testclient.TestClient:
    return testclient.TestClient(main.app)


@pytest.fixture(name="item")
def fixture_item() -> schemas.ItemSchema:
    return schemas.ItemSchema(name="name", id="id", price=123)


def test_get_item(app_client: testclient.TestClient, item: schemas.ItemSchema) -> None:
    response = app_client.get(main.ITEMS_ENDPOINT, params=item.model_dump())
    actual_item = schemas.ItemSchema.model_validate(response.json())

    assert response.status_code == 200
    assert actual_item == item
