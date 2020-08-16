from fastapi import FastAPI
from app.api.mountains import mountains

app = FastAPI()

app.include_router(mountains)
