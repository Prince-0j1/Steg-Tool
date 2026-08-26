from PIL import Image
from ..container import pack, unpack, HEADER_SIZE

def _bits(data):
    for byte in data:
        for i in range(7, -1, -1):
            yield (byte >> i) & 1

def _bytes(bits):
    out = bytearray()
    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        if len(chunk) < 8: break
        v = 0
        for b in chunk: v = (v << 1) | b
        out.append(v)
    return bytes(out)

def encode(src, dst, payload):
    im = Image.open(src).convert("RGB")
    raw = pack(payload)
    capacity = im.width * im.height * 3
    if len(raw) * 8 > capacity:
        raise ValueError(f"Insufficient image capacity. Need {len(raw)*8} bits, have {capacity}.")
    pix = list(im.getdata())
    bitstream = _bits(raw)
    new = []
    for p in pix:
        q = list(p)
        for c in range(3):
            try: q[c] = (q[c] & 0xFE) | next(bitstream)
            except StopIteration: pass
        new.append(tuple(q))
    im.putdata(new)
    im.save(dst, format="PNG")

def decode(src):
    im = Image.open(src).convert("RGB")
    pixels = list(im.getdata())
    bits = []
    needed = HEADER_SIZE * 8
    for p in pixels:
        for c in range(3):
            bits.append(p[c] & 1)
            if len(bits) >= needed: break
        if len(bits) >= needed: break
    header = _bytes(bits)
    import struct
    magic, version, length = struct.unpack(">8sBQ", header)
    total_bits = (HEADER_SIZE + length) * 8
    bits = []
    for p in pixels:
        for c in range(3):
            bits.append(p[c] & 1)
            if len(bits) >= total_bits: break
        if len(bits) >= total_bits: break
    if len(bits) < total_bits:
        raise ValueError("Image does not contain a complete StegApp payload.")
    packed = _bytes(bits)
    payload, _ = unpack(packed)
    return payload
