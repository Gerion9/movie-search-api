import httpx
from typing import List, Dict, Any
from app.core.config import obtener_configuracion
from app.schemas.movies import Pelicula

settings = obtener_configuracion()

async def search_movies(keyword: str) -> List[Pelicula]:
    """Buscar películas y filtrar aquellas con calificación > 7"""
    async with httpx.AsyncClient() as client:
        # Primero buscamos películas con la palabra clave
        parametros_busqueda = {
            "s": keyword,
            "apikey": settings.OMDB_API_KEY
        }
        respuesta = await client.get(settings.OMDB_BASE_URL, params=parametros_busqueda)
        respuesta.raise_for_status()
        datos_busqueda = respuesta.json()

        if "Search" not in datos_busqueda:
            print("No se encontraron películas")
            return []

        # Obtener información detallada de cada película para verificar calificación
        peliculas_calificadas = []
        total_peliculas = len(datos_busqueda['Search'])
        print(f"Se encontró {total_peliculas} película" if total_peliculas == 1 else f"Se encontraron {total_peliculas} películas en total")
        
        for pelicula in datos_busqueda["Search"]:
            parametros_detalle = {
                "i": pelicula["imdbID"],
                "apikey": settings.OMDB_API_KEY
            }
            respuesta_detalle = await client.get(settings.OMDB_BASE_URL, params=parametros_detalle)
            respuesta_detalle.raise_for_status()
            detalle_pelicula = respuesta_detalle.json()
            
            try:
                calificacion = float(detalle_pelicula.get("imdbRating", "0"))
                if calificacion > 7:
                    print(f"Película encontrada con calificación alta: {detalle_pelicula['Title']} - {calificacion}")
                    peliculas_calificadas.append({
                        "Title": detalle_pelicula["Title"],
                        "Year": detalle_pelicula["Year"],
                        "imdbID": detalle_pelicula["imdbID"], 
                        "Type": detalle_pelicula["Type"],
                        "Poster": detalle_pelicula["Poster"],
                        "imdbRating": str(calificacion)
                    })
            except ValueError:
                print(f"Error al procesar la calificación de: {detalle_pelicula.get('Title', 'Película desconocida')}")
                continue

        peliculas_encontradas = len(peliculas_calificadas)
        print(f"Se encontró {peliculas_encontradas} película con calificación mayor a 7" if peliculas_encontradas == 1 
              else f"Se encontraron {peliculas_encontradas} películas con calificación mayor a 7")
        return peliculas_calificadas