import fastapi
from fastapi import FastAPI
from repositories.database import Base, engine
from routers import authRouter, songRouter
from fastapi.middleware.cors import CORSMiddleware
from models.user import User
from models.song import Song

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
                   allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])
Base.metadata.create_all(bind=engine)

@app.get("/api/data")
async def root():
    return {"message": "Hello World"}

app.include_router(authRouter.router)
app.include_router(songRouter.router)





