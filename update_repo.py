#!/usr/bin/env python3
from pathlib import Path
import subprocess, hashlib, gzip, bz2
from email.utils import formatdate

root = Path(__file__).resolve().parent
base_url = "https://dldkdkd.github.io/LivingIcons"

depictions = {
    "com.adam.livingicons": "livingicons",
    "com.adam.dockpages": "dockpages",
    "com.adam.livingiconsdumper": "dumper",
    "com.adam.livingrespring": "livingrespring",
    "com.adam.atriaenglishpatch": "atriaenglish",
}

def field(deb, key):
    try:
        return subprocess.check_output(
            ["dpkg-deb", "-f", str(deb), key],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
    except subprocess.CalledProcessError:
        return ""

parts = []
for deb in sorted((root / "debs").glob("*.deb")):
    pkg = field(deb, "Package")
    desc = field(deb, "Description") or pkg
    data = deb.read_bytes()

    stanza = [
        f"Package: {pkg}",
        f"Name: {field(deb, 'Name') or pkg}",
        f"Version: {field(deb, 'Version')}",
        f"Architecture: {field(deb, 'Architecture')}",
    ]

    dlines = desc.splitlines()
    stanza.append(f"Description: {dlines[0] if dlines else pkg}")
    stanza.extend(" " + (x if x else ".") for x in dlines[1:])

    for key in ["Section", "Author", "Maintainer", "Depends"]:
        value = field(deb, key)
        if value:
            stanza.append(f"{key}: {value}")

    stanza += [
        f"Filename: debs/{deb.name}",
        f"Size: {len(data)}",
        f"SHA256: {hashlib.sha256(data).hexdigest()}",
    ]

    slug = depictions.get(pkg)
    if slug:
        stanza.append(f"Depiction: {base_url}/depictions/{slug}/")

    stanza += [
        f"Icon: {base_url}/CydiaIcon.png",
        "Tag: role::enduser",
    ]

    parts.append("\n".join(stanza))

text = "\n\n".join(parts) + "\n"
(root / "Packages").write_text(text, encoding="utf-8")
(root / "Packages.gz").write_bytes(gzip.compress(text.encode("utf-8"), 9))
(root / "Packages.bz2").write_bytes(bz2.compress(text.encode("utf-8"), 9))

release = [
    "Origin: Adam's Repo",
    "Label: Adam's Repo",
    "Suite: stable",
    "Version: 1.0",
    "Codename: ios",
    "Architectures: iphoneos-arm64 iphoneos-arm64e",
    "Components: main",
    "Description: LivingIcons, DockPages, and jailbreak utilities by Adam.",
    "Icon: https://dldkdkd.github.io/LivingIcons/CydiaIcon.png",
    f"Date: {formatdate(usegmt=True)}",
]

indexes = ["Packages", "Packages.gz", "Packages.bz2"]

for title, func in [
    ("MD5Sum", hashlib.md5),
    ("SHA1", hashlib.sha1),
    ("SHA256", hashlib.sha256),
]:
    release.append(title + ":")
    for n in indexes:
        data = (root / n).read_bytes()
        release.append(f" {func(data).hexdigest()} {len(data):16d} {n}")

(root / "Release").write_text("\n".join(release) + "\n", encoding="utf-8")
print(f"Updated {len(parts)} packages, compressed indexes, and Release.")
