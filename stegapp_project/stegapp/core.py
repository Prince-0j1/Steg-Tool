from pathlib import Path
from .crypto import pack_message, unpack_message
from .methods import image_lsb, audio_lsb, text_zero_width, file_append

METHODS = {
    "Image LSB": image_lsb,
    "Audio LSB": audio_lsb,
    "Text Zero-Width": text_zero_width,
    "File Append": file_append,
}

EXTENSIONS = {
    "Image LSB": {".png", ".bmp"},
    "Audio LSB": {".wav"},
    "Text Zero-Width": {".txt", ".md", ".html", ".htm"},
    "File Append": None,
}

def supported_methods(path):
    ext=Path(path).suffix.lower()
    return [m for m in METHODS if EXTENSIONS[m] is None or ext in EXTENSIONS[m]]

def encode(path, output, text, method, password=None):
    if not text.strip(): raise ValueError("Secret text cannot be empty.")
    if method not in METHODS: raise ValueError("Unknown steganography method.")
    ext=Path(path).suffix.lower()
    allowed=EXTENSIONS[method]
    if allowed is not None and ext not in allowed:
        raise ValueError(f"{method} is incompatible with {ext or 'this file type'}.")
    payload=pack_message(text,password)
    METHODS[method].encode(path, output, payload)

def decode(path, method, password=None):
    if method not in METHODS: raise ValueError("Unknown steganography method.")
    payload=METHODS[method].decode(path)
    return unpack_message(payload,password)
