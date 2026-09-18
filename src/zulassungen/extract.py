from pathlib import Path
 
import py7zr
 
def extract_folder(folder_path: Path, output_dir: Path) -> Path:
    """Extracts a .7z-folder, returns output path."""
    with py7zr.SevenZipFile(folder_path, mode="r") as folder:
        folder.extractall(path=output_dir)
    return Path(output_dir)