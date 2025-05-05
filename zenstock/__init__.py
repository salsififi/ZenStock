"""ZenStock Project central package, with settings and urls"""

from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Link to environment variables
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")
