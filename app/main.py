from fastapi import FastAPI
from app.api import posts

app = FastAPI()
app.include_router(posts.router)
