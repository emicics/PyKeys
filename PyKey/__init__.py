"""
PyKeys - The simplest keyboard detection library for humans.
Developed by: Emiliano
Version: 1.0.0
"""

from .core import PyKey

__docs__ = """
PyKeys is a library designed to simplify keyboard detection using a background monitor.
It provides three main variables that update automatically:
- PyKey.key: For regular letters and numbers.
- PyKey.F: For function keys (F1-F12).
- PyKey.hotkey: For key combinations (Ctrl, Alt, etc.) or special keys.

Basic Usage:
from PyKeys import PyKey
while True:
    if PyKey.key == 'a, s':
        print("A and S keys are pressed in order")
"""