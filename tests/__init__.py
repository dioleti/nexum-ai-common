import os
import sys

_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SRC_DIR = os.path.join(_ROOT_DIR, "src")

if _ROOT_DIR not in sys.path:
    sys.path.append(_ROOT_DIR)
if _SRC_DIR not in sys.path:
    sys.path.append(_SRC_DIR)
