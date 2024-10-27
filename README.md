# API de Búsqueda de Películas

API REST desarrollada en Python que permite buscar películas por palabra clave y filtrar aquellas con calificación IMDb superior a 7.

## Características

- Búsqueda de películas por palabra clave
- Filtrado automático de películas con calificación IMDb > 7
- Información detallada incluyendo título, año, póster y calificación
- Manejo robusto de errores
- Documentación automática con Swagger/OpenAPI

## Requisitos

- Python 3.8+
- FastAPI
- HTTPX
- Python-dotenv
- Pydantic

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Gerion9/movie-search-api.git
cd movie-search-api
```

2. Crear y activar el entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Unix o MacOS:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Crear archivo `.env` con tu clave API de OMDB:
```env
OMDB_API_KEY=tu_clave_api_aqui
API_HOST=0.0.0.0
API_PORT=8000
```

## Configuración de la API OMDB

1. Registrarse en [OMDB API](http://www.omdbapi.com/apikey.aspx)
2. Solicitar una API key gratuita
3. Agregar la API key al archivo `.env`

## Ejecutar la API

1. Iniciar el servidor:
```bash
uvicorn app.main:app --reload
```

2. Acceder a:
- API Documentation (Swagger): http://localhost:8000/docs


## Uso de la API

### Buscar Películas
- Localiza el endpoint `GET /api/v1/search/`

**Endpoint:** `GET /api/v1/search/`

- Haz click en el botón "Try it out"
4. Ingresa el término de búsqueda en el campo `keyword`

**Parámetros:**
- `keyword` (string): Término de búsqueda

- Presiona "Execute" para realizar la búsqueda

**Ejemplo de solicitud:**
```bash
curl "http://localhost:8000/api/v1/search/?keyword=inception"
```

**Ejemplo de respuesta:**
```json
{
    "Busqueda": [
        {
            "Titulo": "Inception",
            "Anio": "2010",
            "imdbID": "tt1375666",
            "Tipo": "movie",
            "Poster": "https://m.media-amazon.com/...",
            "CalificacionIMDB": "8.8"
        }
    ]
}
```

## Estructura del Proyecto

```
movie-search-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada de FastAPI
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── movies.py      # Endpoints de películas
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py         # Configuraciones
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── omdb.py          # Servicio OMDB
│   │
│   └── schemas/
│       ├── __init__.py
│       └── movies.py        # Modelos Pydantic
│
├── tests/
│   ├── __init__.py
│   └── test_api.py         # Pruebas
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Manejo de Errores

La API incluye manejo de errores para:
- Películas no encontradas (404)
- Errores de conexión con OMDB
- Errores de validación de datos
- Errores internos del servidor (500)

## Pruebas

Para ejecutar las pruebas:
```bash
pytest
```

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu función (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Gairo Yostin Peralta - [@gairoperalta](https://www.linkedin.com/in/gairoperalta/) - gairo@strtgy.ai

Link del Proyecto: [https://github.com/Gerion9/movie-search-api](https://github.com/Gerion9/movie-search-api)
