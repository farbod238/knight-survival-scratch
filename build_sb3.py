import json
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Knight-Survival.sb3"


def ensure_files():
    required = [
        ROOT / "project.json",
        ROOT / "assets" / "background.svg",
        ROOT / "assets" / "player.svg",
        ROOT / "assets" / "enemy.svg",
        ROOT / "assets" / "attack.svg",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required files: {missing}")


def build_sb3():
    ensure_files()

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(ROOT / "project.json", arcname="project.json")

        for rel in [
            "assets/background.svg",
            "assets/player.svg",
            "assets/enemy.svg",
            "assets/attack.svg",
        ]:
            zf.write(ROOT / rel, arcname=rel)

    print(f"Created: {OUT}")


if __name__ == "__main__":
    build_sb3()
