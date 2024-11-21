from cryptography.fernet import Fernet

from src.config import settings

fernet = Fernet(settings.ENCRYPTION_KEY)


def encrypt_password(password: str) -> str:
    """Cifra una contraseña."""
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password: str) -> str:
    """Descifra una contraseña cifrada."""
    return fernet.decrypt(encrypted_password.encode()).decode()
