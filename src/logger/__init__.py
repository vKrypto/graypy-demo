import logging
import logging.config
import json
from pathlib import Path
import graypy  # noqa



config_file = Path(__file__).parent.joinpath("./config.json")
if not config_file.exists():
    raise FileNotFoundError(f"Configuration file not found: {config_file}")

with config_file.open("r") as f:
    config = json.load(f)

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)