from collections import Counter
from pathlib import Path


def list_files(root: Path) -> list[Path]:
    """Returns a list of all files in a given path."""
    return [datei for datei in Path(root).rglob("*") if datei.is_file()]


def count_filenames(root: Path) -> Counter:
    """Returns a counter of all filenames contained in a given path."""
    namen = [datei.name for datei in list_files(root)]
    return Counter(namen)


def find_file(root: Path, searched: str) -> list[Path]:
    """e.g. find_file(root, '*merged*')"""
    return sorted(Path(root).rglob(searched))