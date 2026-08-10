#!/usr/bin/env python3
from pathlib import Path
import subprocess, hashlib, gzip, bz2

root = Path(__file__).resolve().parent
base_url = "https://dldkdkd.github.io/LivingIcons"

def field(deb, key):
    return subprocess.check_output(["dpkg-deb", "-f", str(deb), key], text=True).strip()

parts = []
for deb in sorted((root / "debs").glob("*.deb")):
    package = field(deb, "Package")
    if not package and "com.adam.livingicons_0.5.7" in deb.name:
        package = "com.adam.livingicons"
    desc = field(deb, "Description")
    if package == "com.adam.livingicons" and not desc:
        desc = "Bring your Home Screen to life with animated app icons."
    lines = desc.splitlines()
    stanza = [
        f"Package: {package}",
        f"Name: {field(deb, 'Name') or ('LivingIcons - Animated Home Screen Icons' if package == 'com.adam.livingicons' else package)}",
        f"Version: {field(deb, 'Version') or ('0.5.7' if package == 'com.adam.livingicons' else '')}",
        f"Architecture: {field(deb, 'Architecture') or ('iphoneos-arm64e' if package == 'com.adam.livingicons' else '')}",
        f"Description: {lines[0] if lines else package}",
    ]
    stanza.extend(" " + line if line else " ." for line in lines[1:])
    for key in ["Section", "Author", "Maintainer", "Depends"]:
        value = field(deb, key)
        if value:
            stanza.append(f"{key}: {value}")
    depiction = {
        "com.adam.livingicons": "livingicons",
        "com.adam.dockpages": "dockpages",
        "com.adam.livingiconsdumper": "dumper",
        "com.adam.livingrespring": "livingrespring",
        "com.adam.atriaenglishpatch": "atriaenglish",
    }.get(package, "")
    stanza += [
        f"Filename: debs/{deb.name}",
        f"Size: {deb.stat().st_size}",
        f"SHA256: {hashlib.sha256(deb.read_bytes()).hexdigest()}",
        f"Depiction: {base_url}/depictions/{depiction}/" if depiction else f"Depiction: {base_url}/",
        f"Icon: {base_url}/CydiaIcon.png",
        "Tag: role::enduser",
    ]
    parts.append("\n".join(stanza))

text = "\n\n".join(parts) + "\n"
(root / "Packages").write_text(text)
(root / "Packages.gz").write_bytes(gzip.compress(text.encode(), 9))
(root / "Packages.bz2").write_bytes(bz2.compress(text.encode(), 9))
print("Updated Packages, Packages.gz, and Packages.bz2")
