import os, sys
from datetime import datetime

# Add project root to sys.path if not already added
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from core.env_loader import load_env
from core.reflection import reflect

# Load environment variables
load_env()
