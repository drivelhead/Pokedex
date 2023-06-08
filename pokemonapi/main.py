from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from routes.anything import router as anythingRouter
from routes.pokemons import router as pokemonRouter
from database.connection import engine
from database import models

from origins import origins

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_origins=origins,
                   allow_methods=["*"],
                   allow_headers=["*"])


app.include_router(anythingRouter)
app.include_router(pokemonRouter)



@app.get("/", status_code=status.HTTP_200_OK)
def printHelloWorld():
    return {"message": "Hello world!"}

