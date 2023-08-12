from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
MAIN_DIR = PACKAGE_DIR.parent
RESOURCES_DIR = MAIN_DIR / 'resources'
DATA_DIR = RESOURCES_DIR / 'data'
