import struct
from .config import MAGIC, VERSION

# Container: MAGIC | version(1) | payload length(8) | payload
HEADER_FMT = ">8sBQ"
HEADER_SIZE = struct.calcsize(HEADER_FMT)

def pack(payload: bytes) -> bytes:
    return struct.pack(HEADER_FMT, MAGIC, VERSION, len(payload)) + payload

def unpack(data: bytes, offset=0):
    if len(data) < offset + HEADER_SIZE:
        raise ValueError("Stego header is missing or truncated.")
    magic, version, length = struct.unpack_from(HEADER_FMT, data, offset)
    if magic != MAGIC or version != VERSION:
        raise ValueError("Not a StegApp-generated payload.")
    start = offset + HEADER_SIZE
    end = start + length
    if end > len(data):
        raise ValueError("Stego payload is truncated or corrupted.")
    return data[start:end], end
