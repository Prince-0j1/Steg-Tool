from ..container import pack, unpack

ZW = {"0":"\u200b", "1":"\u200c"}
REV = {v:k for k,v in ZW.items()}
START = "\u2060\u2060STEGAPP\u2060"
END = "\u2060ENDSTEGAPP\u2060"

def encode(src, dst, payload):
    text = open(src, "r", encoding="utf-8").read()
    bits = "".join(ZW[str((b >> i) & 1)] for b in pack(payload) for i in range(7,-1,-1))
    open(dst, "w", encoding="utf-8").write(text + START + bits + END)

def decode(src):
    text = open(src, "r", encoding="utf-8").read()
    if START not in text or END not in text:
        raise ValueError("No StegApp zero-width payload found.")
    bits_text = text.split(START,1)[1].split(END,1)[0]
    try:
        bits = "".join(REV[c] for c in bits_text)
    except KeyError as exc:
        raise ValueError("Corrupted zero-width payload.") from exc
    if len(bits)%8: raise ValueError("Corrupted zero-width payload.")
    raw=bytes(int(bits[i:i+8],2) for i in range(0,len(bits),8))
    payload,_=unpack(raw)
    return payload
