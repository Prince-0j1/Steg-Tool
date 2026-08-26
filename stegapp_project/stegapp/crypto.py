from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64, os

ITERATIONS = 600_000
SALT_SIZE = 16

def _key(password: str, salt: bytes) -> bytes:
    if not password:
        raise ValueError("Password cannot be empty.")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))

def encrypt(data: bytes, password: str) -> bytes:
    salt = os.urandom(SALT_SIZE)
    token = Fernet(_key(password, salt)).encrypt(data)
    return b"P" + salt + token

def decrypt(data: bytes, password: str) -> bytes:
    if len(data) < 1 + SALT_SIZE or data[:1] != b"P":
        raise ValueError("Invalid encrypted payload.")
    salt, token = data[1:1+SALT_SIZE], data[1+SALT_SIZE:]
    try:
        return Fernet(_key(password, salt)).decrypt(token)
    except InvalidToken as exc:
        raise ValueError("Incorrect password or corrupted payload.") from exc

def pack_message(text: str, password: str | None) -> bytes:
    raw = text.encode("utf-8")
    return encrypt(raw, password) if password else b"N" + raw

def unpack_message(data: bytes, password: str | None) -> str:
    if not data:
        raise ValueError("Empty payload.")
    if data[:1] == b"P":
        if not password:
            raise ValueError("This payload is password-protected.")
        raw = decrypt(data, password)
    elif data[:1] == b"N":
        raw = data[1:]
    else:
        raise ValueError("Invalid payload format.")
    return raw.decode("utf-8")
