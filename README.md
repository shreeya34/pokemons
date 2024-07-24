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

   ```

2. **Create a virtual environment:**
    
    ```sh
    python3 -m venv venv
    source venv/bin/activate

    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt

    ```
4. **Set up the PostgreSQL database:**

    - Create a new PostgreSQL database and user.
    - Update the DATABASE_URL in the .env file with your database connection string.

## Start the FastAPI application:

    uvicorn app.main:app --reload

## API Endpoints:

1. **Get Pokémon Data**

    Endpoint: /api/v1/pokemons

    Method: GET

    Description: Retrieves a list of Pokémon with pagination.

    Parameters:
                skip : The number of Pokémon to skip. Used for pagination. Default is 0.
                limit: The number of Pokémon to return. Used for pagination. Default is 100
                
    **Usage** 
        This endpoint is used to fetch a paginated list of Pokémon. For example, to get the first 10 Pokémon,

2. **Search for Pokémon**

        Endpoint: /api/v1/pokemons/search

        Method: GET

        Description: Searches for Pokémon based on name 

        Parameters:

        name: The name of the Pokémon to search for.

    **Usage**
            This endpoint allows you to search for Pokémon by name or type. If no parameters are provided, it returns an empty list.

3. **Store and Retrieve Pokémon Data**

        Endpoint: /api/v1/store

        Method: GET

        Description: Fetches Pokémon data from the PokeAPI, stores it in the PostgreSQL database, and retrieves the stored Pokémon.

    **Usage**
            This endpoint is used to initially populate or update the Pokémon data in the database by fetching it from the PokeAPI. It stores the data and then retrieves the first 100 Pokémon from the database