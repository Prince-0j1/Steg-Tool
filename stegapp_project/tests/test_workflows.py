from pathlib import Path
from PIL import Image
from stegapp.core import encode, decode

def test_image_roundtrip(tmp_path):
    src=tmp_path/"carrier.png"; out=tmp_path/"stego.png"
    Image.new("RGB",(200,200),"white").save(src)
    encode(src,out,"Hello World","Image LSB")
    assert decode(out,"Image LSB")=="Hello World"

def test_image_password_roundtrip(tmp_path):
    src=tmp_path/"carrier.png"; out=tmp_path/"stego.png"
    Image.new("RGB",(200,200),"white").save(src)
    encode(src,out,"Secret","Image LSB","correct")
    assert decode(out,"Image LSB","correct")=="Secret"

def test_text_roundtrip(tmp_path):
    src=tmp_path/"carrier.txt"; out=tmp_path/"stego.txt"
    src.write_text("This is ordinary text.",encoding="utf-8")
    encode(src,out,"Hidden message","Text Zero-Width")
    assert decode(out,"Text Zero-Width")=="Hidden message"

def test_append_roundtrip(tmp_path):
    src=tmp_path/"carrier.bin"; out=tmp_path/"stego.bin"
    src.write_bytes(b"example data")
    encode(src,out,"Hidden","File Append")
    assert decode(out,"File Append")=="Hidden"
