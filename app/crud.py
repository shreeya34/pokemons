

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from . import models, schemas

async def get_pokemons(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[schemas.Pokemon]:
    result = await db.execute(select(models.Pokemon).offset(skip).limit(limit))
    return result.scalars().all()

async def search_pokemons(db: AsyncSession, name: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[schemas.Pokemon]:
    query = select(models.Pokemon).distinct(models.Pokemon.name)
    if name:
        query = query.where(models.Pokemon.name.ilike(f"%{name}%"))
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


