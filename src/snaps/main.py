import fastapi

from snaps.router import item

app = fastapi.FastAPI()
app.include_router(item.router)
