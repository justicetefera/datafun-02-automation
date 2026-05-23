"""
Module: app_justice
Author: Justice Tefera
Email: justfera30@gmail.com
Date: 2026-05-23

Description:
    Custom automation script demonstrating loops, file generation,
    logging, and structured workflow patterns.
"""

import logging
from pathlib import Path
import time

from datafun.shared import setup_logging

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)


# FUNCTION 1 — Numeric loop (e.g., training days)
def function_one():
    logger.info("FUNCTION 1: Daily training logs")
    for day in range(1, 4):
        filename = f"justice_training_day_{day}.txt"
        Path(filename).write_text(f"Training Day {day}: Completed required tasks.")
        logger.info(f"Wrote file: {filename}")


# FUNCTION 2 — Loop over a list (Army tasks)
def function_two():
    logger.info("FUNCTION 2: Army task logs")
    tasks = ["inventory", "training", "maintenance"]
    for task in tasks:
        filename = f"justice_{task}.txt"
        Path(filename).write_text(f"Task completed: {task}")
        logger.info(f"Wrote file: {filename}")


# FUNCTION 3 — List comprehension (completed tasks)
def function_three():
    logger.info("FUNCTION 3: Completed task logs")
    tasks = ["inventory", "training", "maintenance"]
    completed = [f"completed_{t}" for t in tasks]
    for item in completed:
        filename = f"justice_{item}.txt"
        Path(filename).write_text(f"Log entry: {item}")
        logger.info(f"Wrote file: {filename}")


# FUNCTION 4 — While loop with timing (duty cycle logs)
def function_four():
    logger.info("FUNCTION 4: Duty cycle logs")
    count = 1
    while count <= 3:
        filename = f"justice_duty_{count:02}.txt"
        Path(filename).write_text(f"Duty cycle entry {count}")
        logger.info(f"Wrote file: {filename}")
        time.sleep(1)
        count += 1


def main():
    logger.info("=== START JUSTICE ARMY AUTOMATION ===")
    function_one()
    function_two()
    function_three()
    function_four()
    logger.info("=== END JUSTICE ARMY AUTOMATION ===")


if __name__ == "__main__":
    main()
