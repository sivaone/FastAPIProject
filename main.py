from fastapi import FastAPI
import json
from pathlib import Path
from contextlib import asynccontextmanager


# Read weather.json from the same directory
data: dict = {}


def load_weather_data() -> dict:
    weather_file = Path(__file__).parent / "weather.json"
    if not weather_file.exists():
        raise FileNotFoundError(f"weather.json not found at {weather_file}")
    with weather_file.open() as f:
        return json.load(f)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global data
    data = load_weather_data()
    yield
    # optional shutdown cleanup here


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/cities/{country}")
async def get_cities(country: str):
    cities = data.get(country, [])
    return {"country": country, "cities": cities}


@app.get("/countries")
async def get_countries():
    countries = list(data.keys())
    return {"countries": countries}


@app.get("/weather/{city}")
async def get_weather(city: str):
    for country, cities in data.items():
        if city in cities:
            return {"city": city, "weather": cities[city]}
    return {"error": "City not found"}


# Get the weather for a country and city and month combination
@app.get("/weather/{country}/{city}/{month}")
async def get_weather_by_month(country: str, city: str, month: str):
    cities = data.get(country, {})
    weather = cities.get(city, {})
    month_weather = weather.get(month)
    if month_weather:
        return {"country": country, "city": city, "month": month, "weather": month_weather}
    return {"error": "Weather data not found for the specified country, city, and month"}