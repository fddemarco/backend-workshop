import fastapi

from snaps.router import item_router

app = fastapi.FastAPI()
app.include_router(item_router.router)
