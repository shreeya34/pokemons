from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import httpx
from . import models, schemas, database
from .database import SessionLocal
from .config import settings

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await database.init_db()
    await fetch_and_store_pokemon_data()

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
                    image=details['sprites']['front_default'],
                    type=details['types'][0]['type']['name']
                )
                session.add(pokemon)
            await session.commit()

@app.get("/api/v1/pokemons", response_model="list[schemas.Pokemon]")
async def read_pokemons(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(select(models.Pokemon).offset(skip).limit(limit))
    return result.scalars().all()

@app.get("/api/v1/pokemons/search", response_model="list[schemas.Pokemon]")
async def search_pokemons(name: str = None, type: str = None, db: AsyncSession = Depends(SessionLocal)):
    query = select(models.Pokemon)
    if name:
        query = query.filter(models.Pokemon.name.ilike(f"%{name}%"))
    if type:
        query = query.filter(models.Pokemon.type.ilike(f"%{type}%"))
    result = await db.execute(query)
    return result.scalars().all()
