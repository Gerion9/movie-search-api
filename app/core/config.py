# Importamos las clases y funciones necesarias
from pydantic_settings import BaseSettings
from functools import lru_cache

class Configuracion(BaseSettings):
    """
    Clase para manejar la configuración de la aplicación
    Hereda de BaseSettings para cargar variables de entorno
    """
    # Variables requeridas para la API de OMDB
    OMDB_API_KEY: str  # Clave de API requerida
    OMDB_BASE_URL: str = "http://www.omdbapi.com"  # URL base de la API
    
    # Configuración del servidor
    API_HOST: str = "0.0.0.0"  # Host por defecto
    API_PORT: int = 8000  # Puerto por defecto

    class Config:
        # Archivo de donde se cargarán las variables de entorno
        env_file = ".env"

    def __str__(self):
        """Método para imprimir la configuración de forma legible"""
        return f"""
        Configuración actual:
        - URL Base OMDB: {self.OMDB_BASE_URL}
        - Host API: {self.API_HOST}
        - Puerto API: {self.API_PORT}
        """

@lru_cache()
def obtener_configuracion():
    """
    Función que devuelve una instancia única de la configuración
    Utiliza lru_cache para mantener en caché la configuración
    """
    config = Configuracion()
    print("Configuración cargada:", config)  # Imprime la configuración al cargarla
    return config