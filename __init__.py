"""
pyVNC - Python VNC Client Library
"""

__version__ = "0.1"

# Safe imports - handle potential numpy/dependency issues gracefully
try:
    from .pyVNC.Client import Client
    _client_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.Client: {e}")
    Client = None
    _client_available = False

try:
    from .pyVNC.Buffer import DisplayBuffer, ArrayBuffer
    _buffer_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.Buffer: {e}")
    DisplayBuffer = ArrayBuffer = None
    _buffer_available = False

try:
    from .pyVNC.VNCFactory import VNCFactory
    _factory_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.VNCFactory: {e}")
    VNCFactory = None
    _factory_available = False

try:
    from .pyVNC.RFBToGUI import RFBToGUI
    _gui_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.RFBToGUI: {e}")
    RFBToGUI = None
    _gui_available = False

# Import constants and rfb safely
try:
    from .pyVNC.constants import *
    _constants_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.constants: {e}")
    _constants_available = False

try:
    from .pyVNC.rfb import *
    _rfb_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.rfb: {e}")
    _rfb_available = False

# Export available modules
__all__ = []
if _client_available:
    __all__.append('Client')
if _buffer_available:
    __all__.extend(['DisplayBuffer', 'ArrayBuffer'])
if _factory_available:
    __all__.append('VNCFactory')
if _gui_available:
    __all__.append('RFBToGUI')

# Availability check function
def is_fully_available():
    """Check if all pyVNC modules are available."""
    return all([_client_available, _buffer_available, _factory_available, _gui_available, _constants_available, _rfb_available])

def get_available_modules():
    """Get list of successfully imported modules."""
    available = []
    if _client_available:
        available.append('Client')
    if _buffer_available:
        available.extend(['DisplayBuffer', 'ArrayBuffer'])
    if _factory_available:
        available.append('VNCFactory')
    if _gui_available:
        available.append('RFBToGUI')
    return available
