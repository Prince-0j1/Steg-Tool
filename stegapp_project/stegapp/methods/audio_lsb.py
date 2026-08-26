import wave, struct
from ..container import pack, unpack, HEADER_SIZE

def encode(src, dst, payload):
    with wave.open(src, "rb") as w:
        params = w.getparams()
        if params.sampwidth != 2:
            raise ValueError("Audio LSB currently supports 16-bit PCM WAV files only.")
        frames = bytearray(w.readframes(w.getnframes()))
    raw = pack(payload)
    capacity = len(frames)
    if len(raw) * 8 > capacity:
        raise ValueError(f"Insufficient WAV capacity. Need {len(raw)*8} samples/bytes, have {capacity}.")
    i = 0
    for byte in raw:
        for bit in range(7, -1, -1):
            frames[i] = (frames[i] & 0xFE) | ((byte >> bit) & 1)
            i += 1
    with wave.open(dst, "wb") as w:
        w.setparams(params)
        w.writeframes(frames)

def decode(src):
    with wave.open(src, "rb") as w:
        if w.getsampwidth() != 2:
            raise ValueError("Audio LSB supports 16-bit PCM WAV files only.")
        frames = bytearray(w.readframes(w.getnframes()))
    bits = [(b & 1) for b in frames[:HEADER_SIZE*8]]
    if len(bits) < HEADER_SIZE*8:
        raise ValueError("WAV file is too small for a StegApp header.")
    def to_bytes(bs):
        out=bytearray()
        for i in range(0,len(bs),8):
            v=0
            for b in bs[i:i+8]: v=(v<<1)|b
            out.append(v)
        return bytes(out)
    import struct
    header=to_bytes(bits)
    magic, version, length=struct.unpack(">8sBQ", header)
    total=(HEADER_SIZE+length)*8
    if len(frames)<total: raise ValueError("WAV payload is truncated.")
    payload,_=unpack(to_bytes([(b&1) for b in frames[:total]]))
    return payload
