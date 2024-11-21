from dotenv import load_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

load_dotenv(override=True)


class Settings(BaseSettings):
    """
    Configuración de la aplicación utilizando Pydantic
    para validar y cargar variables de entorno.
    """

    # Configuración general de entorno
    ENV: str
    DEBUG: bool

    # Configuración de la base de datos
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ENCRYPTION_KEY: str

    # Configuración de CORS
    ALLOWED_ORIGINS: str = [
        "*",
    ]
    ALLOWED_METHODS: str = [
        "*",
    ]
    ALLOWED_HEADERS: str = [
        "*",
    ]
    ALLOW_CREDENTIALS: bool = True

    model_config = ConfigDict(case_sensitive=True)


# Crear una instancia de configuración que puedas utilizar en toda la app.
settings = Settings()
