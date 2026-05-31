from pathlib import Path
import tomllib

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_FILE = PROJECT_ROOT / "config.toml"


def load_config():
    """ """
    with open(CONFIG_FILE, "rb") as file:
        return tomllib.load(file)
