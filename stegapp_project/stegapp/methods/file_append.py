from ..config import MAGIC
from ..container import pack, unpack

TRAILER = b"\nSTEGAPP-APPEND-TRAILER\n"

def encode(src, dst, payload):
    with open(src,"rb") as f: original=f.read()
    with open(dst,"wb") as f: f.write(original + TRAILER + pack(payload))

def decode(src):
    with open(src,"rb") as f: data=f.read()
    marker = data.rfind(TRAILER)
    if marker < 0: raise ValueError("No StegApp appended payload found.")
    payload,_=unpack(data, marker+len(TRAILER))
    return payload
