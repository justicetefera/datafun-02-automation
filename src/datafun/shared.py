import logging
from pathlib import Path


def setup_logging():
    """Configure basic logging for the project."""
    log_file = Path("project.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
