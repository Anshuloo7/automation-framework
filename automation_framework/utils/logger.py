import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, "behave_run.log")

# File handler (INFO and above)
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.INFO)

# Console handler (WARN and above only)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Unified format
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Configure logger
logger = logging.getLogger("behave-logger")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
