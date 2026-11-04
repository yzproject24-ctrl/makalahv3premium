#!/usr/bin/env python3
# YZMakalah V3 Premium - pembuka kit. BY YZ PROJECT @yzproject24
import hashlib, io, os, sys, tarfile, lzma
TK = "MAAF, FILE TERKUNCI. MASUKKAN KODE UNTUK MENGUBAH. BY YZ PROJECT"
def main():
    kode = (sys.argv[1] if len(sys.argv) > 1 else "").strip()
    d0 = os.path.dirname(os.path.abspath(__file__))
    tuju = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/yz3"
    try:
        d = open(os.path.join(d0, "kit.enc"), "rb").read()
        g, n, h, c = d[:16], d[16:32], d[32:64], d[64:]
        k = hashlib.pbkdf2_hmac("sha256", kode.encode("utf8"), g, 400000, 64)
        if not kode or hashlib.sha256(k[32:] + c).digest() != h: raise ValueError
        a = bytearray(); i = 0
        while len(a) < len(c):
            a += hashlib.sha256(k[:32] + n + i.to_bytes(8, "big")).digest(); i += 1
        p = bytes(x ^ y for x, y in zip(c, a))
        os.makedirs(tuju, exist_ok=True)
        tarfile.open(fileobj=io.BytesIO(p), mode="r:xz").extractall(tuju)
        open(os.path.join(tuju, ".kunci"), "w", encoding="utf8").write(kode)
    except Exception:
        print(TK); print("STATUS: TERKUNCI"); sys.exit(0)
    print("STATUS: TERBUKA")
main()
