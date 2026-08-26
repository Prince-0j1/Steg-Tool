# StegApp

A modular Python desktop steganography application with a Tkinter GUI. It can hide and later extract text using methods that are appropriate for different carrier types.

## Features

- Image LSB for PNG/BMP carriers (output is PNG).
- 16-bit PCM WAV LSB.
- Text zero-width Unicode embedding for TXT/MD/HTML.
- General binary append container for arbitrary files.
- Optional password protection using `cryptography` + PBKDF2-HMAC-SHA256 + Fernet.
- Capacity/type validation and clear extraction errors.
- Never overwrites the source by default.
- Automated encode/decode tests.

## Installation

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Test

```bash
pytest -q
```

## Method notes

**Image LSB:** embeds one bit in each RGB channel and writes a PNG. This is lossless and deterministic for StegApp-generated files.

**Audio LSB:** supports 16-bit PCM WAV only. It embeds one bit per audio byte.

**Text Zero-Width:** appends invisible Unicode characters containing the payload. It is intended for ordinary text-like files and should not be passed through editors that strip zero-width characters.

**File Append:** appends a clearly identifiable StegApp container to the carrier. This is a general-purpose hiding mechanism, but it does not guarantee that every file format remains semantically valid after modification. Use it when preservation of the original format is not a requirement.

## Security

The password option encrypts the secret message before embedding. The application does not implement custom cryptographic algorithms. Keep passwords private; a wrong password is indistinguishable from a corrupted encrypted payload.

## Limitations

- Image LSB capacity depends on image dimensions.
- WAV LSB currently requires 16-bit PCM.
- Text zero-width steganography can be destroyed by applications that normalize/remove invisible Unicode.
- The File Append method is not appropriate when a file must remain byte-for-byte or format-valid after modification.
