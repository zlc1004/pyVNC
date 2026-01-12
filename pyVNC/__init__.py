"""
pyVNC core modules
"""

# Safe imports for core modules
__all__ = []

try:
    from .Client import Client
    __all__.append('Client')
except ImportError as e:
    print(f"Warning: Could not import Client: {e}")
    Client = None

try:
    from .Buffer import DisplayBuffer, ArrayBuffer
    __all__.extend(['DisplayBuffer', 'ArrayBuffer'])
except ImportError as e:
    print(f"Warning: Could not import Buffer classes: {e}")
    DisplayBuffer = ArrayBuffer = None

try:
    from .VNCFactory import VNCFactory
    __all__.append('VNCFactory')
except ImportError as e:
    print(f"Warning: Could not import VNCFactory: {e}")
    VNCFactory = None

try:
    from .RFBToGUI import RFBToGUI
    __all__.append('RFBToGUI')
except ImportError as e:
    print(f"Warning: Could not import RFBToGUI: {e}")
    RFBToGUI = None

try:
    from .constants import *
except ImportError as e:
    print(f"Warning: Could not import constants: {e}")

try:
    from .rfb import *
except ImportError as e:
    print(f"Warning: Could not import rfb: {e}")
