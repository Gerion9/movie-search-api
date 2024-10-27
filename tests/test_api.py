import pytest
from fastapi.testclient import TestClient
from app.main import app

# Creamos el cliente de pruebas
client = TestClient(app)

def test_leer_raiz():
    """Prueba el endpoint raíz de la API"""
    # Hacemos una petición GET a la raíz
    respuesta = client.get("/")
    # Verificamos que el código de estado sea 200 (éxito)
    assert respuesta.status_code == 200
    # Verificamos que el mensaje de bienvenida sea correcto
    assert respuesta.json() == {"mensaje": "Bienvenido a la API de Búsqueda de Películas. Usa /docs para ver la documentación."}

def test_buscar_peliculas():
    """Prueba la búsqueda de películas con calificación alta"""
    # Realizamos búsqueda con la palabra clave 'inception'
    respuesta = client.get("/api/v1/search/?keyword=inception")
    # Verificamos código 200 de éxito
    assert respuesta.status_code == 200
    # Obtenemos los datos de la respuesta
    datos = respuesta.json()
    # Verificamos que exista la clave 'Busqueda' en la respuesta
    assert "Busqueda" in datos
    # Verificamos que todas las películas tengan calificación mayor a 7
    for pelicula in datos["Busqueda"]:
        assert float(pelicula["imdbRating"]) > 7
        print(f"Película encontrada: {pelicula['Title']} - Calificación: {pelicula['imdbRating']}")

def test_buscar_peliculas_no_encontradas():
    """Prueba el caso cuando no se encuentran películas"""
    # Búsqueda con término que no debería encontrar resultados
    respuesta = client.get("/api/v1/search/?keyword=xxxxxxxxxxx")
    # Verificamos código 404 de no encontrado
    assert respuesta.status_code == 404
    # Verificamos mensaje de error
    assert respuesta.json() == {"detail": "No se encontraron películas con calificación mayor a 7"}