from pathlib import Path

PIANO_DIR = Path(__file__) / "tones/piano/"

PIANO_TONE_MAP = {f.name.split("_")[1]: str(f) for f in PIANO_DIR.iterdir()}
