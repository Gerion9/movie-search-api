# Importamos las librerías necesarias
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import movies

# Creamos la aplicación FastAPI con la configuración inicial
app = FastAPI(
    title="API de Búsqueda de Películas",
    description="API para buscar películas con calificación IMDb mayor a 7",
    version="1.0.0"
)

# Configuración del middleware CORS para permitir peticiones de otros dominios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,  # Permite credenciales
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todas las cabeceras
)

# Incluimos los routers de la aplicación
app.include_router(movies.router, prefix="/api/v1", tags=["peliculas"])

# Ruta raíz que muestra un mensaje de bienvenida
@app.get("/")
async def raiz():
    return {"mensaje": "Bienvenido a la API de Búsqueda de Películas. Usa /docs para ver la documentación."}