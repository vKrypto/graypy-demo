import logging
import logging.config
import json
from pathlib import Path
import graypy   # :noqa
import os


cur_dir = Path(__file__).parent
log_dir = cur_dir.parent.joinpath("logs")

if not log_dir.exists():
    os.makedirs(log_dir)

config_file = cur_dir.joinpath("./config.json")
if not config_file.exists():
    raise FileNotFoundError(f"Configuration file not found: {config_file}")
with config_file.open("r") as f:
    config = json.load(f)
    
    
config["handlers"]["file_handler"]["filename"] = log_dir.joinpath("logs.log")
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)