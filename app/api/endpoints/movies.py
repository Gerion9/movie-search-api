from fastapi import APIRouter, HTTPException
from app.services.omdb import search_movies
from app.schemas.movies import RespuestaPeliculas, RespuestaError

router = APIRouter()

@router.get("/search/", response_model=RespuestaPeliculas, responses={404: {"model": RespuestaError}})
async def buscar_peliculas_por_palabra_clave(keyword: str):
    """
    Busca películas por palabra clave y retorna aquellas con calificación IMDb > 7
    """
    try:
        # Obtener las películas usando el servicio OMDB
        peliculas = await search_movies(keyword)
        
        # Imprimir las películas encontradas para debugging
        cantidad = len(peliculas) if peliculas else 0
        print(f"Película{'s' if cantidad != 1 else ''} encontrada{'s' if cantidad != 1 else ''} para '{keyword}': {cantidad}")
        # Verificar si se encontraron películas
        if not peliculas:
            raise HTTPException(
                status_code=404, 
                detail="No se encontraron películas con calificación mayor a 7"
            )
            
        # Retornar las películas encontradas con el campo correcto "Busqueda"
        return {"Busqueda": peliculas}  # Changed from "Search" to "Busqueda"
        
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir
        print(f"Error al buscar películas: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error del servidor: {str(e)}"
        )