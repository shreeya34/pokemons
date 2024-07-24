from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Pokemon
from .schemas import PokemonCreate

async def get_pokemons(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Pokemon).offset(skip).limit(limit))
    return result.scalars().all()

async def search_pokemons(db: AsyncSession, name: str = None, type: str = None):
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    if type:
        query = query.filter(Pokemon.type.ilike(f"%{type}%"))
    result = await db.execute(query)
    return result.scalars().all()

async def create_pokemon(db: AsyncSession, pokemon: PokemonCreate):
    db_pokemon = Pokemon(name=pokemon.name, image_url=pokemon.image_url, type=pokemon.type)
    db.add(db_pokemon)
    await db.commit()
    await db.refresh(db_pokemon)
    return db_pokemon
