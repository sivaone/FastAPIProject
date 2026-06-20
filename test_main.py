import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_cities_spain():
    response = client.get("/cities/Spain")
    assert response.status_code == 200
    assert response.json()["country"] == "Spain"
    assert isinstance(response.json()["cities"], dict)
    assert "Seville" in response.json()["cities"]


def test_get_weather_valid_city():
    response = client.get("/weather/London")
    assert response.status_code == 200
    assert response.json()["city"] == "London"
    assert "weather" in response.json()
    weather = response.json()["weather"]
    assert isinstance(weather, dict)
    assert "January" in weather
    assert "high" in weather["January"]
    assert "low" in weather["January"]


def test_get_weather_different_city():
    response = client.get("/weather/Paris")
    assert response.status_code == 200
    assert response.json()["city"] == "Paris"
    assert "weather" in response.json()
    weather = response.json()["weather"]
    assert isinstance(weather, dict)
    assert weather["January"]["high"] == 45


def test_get_weather_city_not_found():
    response = client.get("/weather/NonexistentCity")
    assert response.status_code == 200
    assert "error" in response.json()
    assert response.json()["error"] == "City not found"


def test_get_weather_multiple_cities():
    cities = ["London", "Paris", "Berlin", "Lima", "Lisbon", "Porto", "Montepulciano", "Seville"]
    for city in cities:
        response = client.get(f"/weather/{city}")
        assert response.status_code == 200
        assert response.json()["city"] == city
        assert "weather" in response.json()


def test_get_weather_case_sensitive():
    response = client.get("/weather/london")
    assert response.status_code == 200
    assert "error" in response.json()
