from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import httpx
from . import models, schemas, database, crud
from .database import SessionLocal, init_db
from typing import List
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    await init_db()
    await fetch_and_store_pokemon_data()

@app.get("/", response_class=FileResponse)
async def read_index():
    return "static/index.html"



async def fetch_and_store_pokemon_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://pokeapi.co/api/v2/pokemon?limit=100')
        pokemons = response.json().get('results', [])
        async with SessionLocal() as session:
            for poke in pokemons:
                poke_details = await client.get(poke['url'])
                details = poke_details.json()
                pokemon = models.Pokemon(
                    name=details['name'],
                    image_url=details['sprites']['front_default'],
                    type=details['types'][0]['type']['name']
                )
                session.add(pokemon)
            await session.commit()

@app.get("/api/v1/pokemons", response_model=List[schemas.Pokemon])
async def read_pokemons(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)):
    return await crud.get_pokemons(db, skip, limit)

@app.get("/api/v1/pokemons/search", response_model=List[schemas.Pokemon])
async def search_pokemons(name: str = None, type: str = None, db: AsyncSession = Depends(database.get_db)):
    return await crud.search_pokemons(db, name, type)

@app.get("/api/v1/store", response_model=List[schemas.Pokemon])
async def store_and_get_pokemons(db: AsyncSession = Depends(database.get_db)):
    await fetch_and_store_pokemon_data()
    return await crud.get_pokemons(db, skip=0, limit=100)