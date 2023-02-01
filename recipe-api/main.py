
from decouple import config

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn

from routers.menu import router as menu_router
from routers.menu import router as dish_router
from fastapi.middleware.cors import CORSMiddleware


DB_URL = config('DB_URL', cast=str)
DB_NAME = config('DB_NAME', cast=str)

app = FastAPI()
app.include_router(menu_router, prefix="/menu", tags=["menus"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )
