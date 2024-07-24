# Pokémon API Project

This project is a FastAPI application that fetches Pokémon data from the PokeAPI and stores it in a PostgreSQL database. The API provides endpoints to retrieve and search for Pokémon data.

## Features

- Fetch and store Pokémon data from the PokeAPI.
- Retrieve all Pokémon data.
- Search for Pokémon by name and type.
- Display Pokémon details including name, type, and image.
- Pagination for browsing through Pokémon.
- Hide pagination buttons when performing a search.

## Technologies Used

- FastAPI
- SQLAlchemy (with async support)
- PostgreSQL
- Pydantic
- HTTPX (for async HTTP requests)
- pydantic-settings
- HTML
- CSS
- JavaScript

## Requirements

- Python 3.8+
- PostgreSQL

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/shreeya34/pokemons.git
   

2. **Create a virtual environment:**
    
    python3 -m venv venv
    source venv/bin/activate

3. **Install the required dependencies:**

    pip install -r requirements.txt

4. **Set up the PostgreSQL database:**

    Create a new PostgreSQL database and user.
    Update the DATABASE_URL in the .env file with your database connection string.

## Start the FastAPI application:

    uvicorn app.main:app --reload

