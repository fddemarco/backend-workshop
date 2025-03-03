import pytest
from fastapi import testclient

import snaps.database.inmemory
from snaps import main
from snaps.models import schemas
from snaps.router import item as item_router


@pytest.fixture(name="setup_database", scope="function")
def fixture_setup_database() -> None:
    snaps.database.inmemory.DATABASE.clear()


@pytest.fixture(name="app_client", scope="function")
def fixture_app_client(setup_database: None) -> testclient.TestClient:
    return testclient.TestClient(main.app)


@pytest.fixture(name="item")
def fixture_item() -> schemas.ItemSchema:
    return schemas.ItemSchema(name="name", id="id", price=123)


def test_items_should_be_unique(
    app_client: testclient.TestClient, item: schemas.ItemSchema
) -> None:
    app_client.post(item_router.ITEMS_ENDPOINT, json=item.model_dump())
    response = app_client.post(item_router.ITEMS_ENDPOINT, json=item.model_dump())

    assert response.status_code == 409


def test_create_item(
    app_client: testclient.TestClient, item: schemas.ItemSchema
) -> None:
    response = app_client.post(item_router.ITEMS_ENDPOINT, json=item.model_dump())
    actual_item = schemas.ItemSchema.model_validate(response.json())

    assert response.status_code == 201
    assert actual_item == item
