# Importamos las clases y tipos necesarios
from pydantic import BaseModel
from typing import List, Optional

# Modelo Pydantic para representar una película
# Contiene los campos básicos que devuelve la API de OMDB
class Pelicula(BaseModel):
    Title: str  # Título de la película
    Year: str   # Año de lanzamiento
    imdbID: str # ID único de IMDB
    Type: str   # Tipo de contenido (película, serie, etc)
    Poster: str # URL del póster
    imdbRating: str # Calificación en IMDB

# Modelo para la respuesta que contiene una lista de películas
class RespuestaPeliculas(BaseModel):
    Busqueda: List[Pelicula]
    
    def __str__(self):
        # Método para imprimir la cantidad de películas encontradas
        cantidad = len(self.Busqueda)
        if cantidad == 1:
            return f"Se encontró 1 película"
        return f"Se encontraron {cantidad} películas"

# Modelo para manejar respuestas de error
class RespuestaError(BaseModel):
    detalle: str # Mensaje detallado del error