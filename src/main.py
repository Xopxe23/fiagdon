import uvicorn
from fastapi import FastAPI

from src.api.routers import routers

app = FastAPI(title="Fiagdon")

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
