"""
pyVNC - Python VNC Client Library
"""

__version__ = "0.1"

# Import only the essential modules to avoid circular dependencies
# The Client module is the main interface that users need

try:
    from .pyVNC.Client import Client
    print("✓ pyVNC.Client imported successfully")
    _client_available = True
except ImportError as e:
    print(f"Warning: Could not import pyVNC.Client: {e}")
    Client = None
    _client_available = False

# Export the main Client class
__all__ = ['Client'] if _client_available else []

def is_available():
    """Check if pyVNC Client is available."""
    return _client_available

def get_client():
    """Get the Client class if available."""
    return Client if _client_available else None

# For users who need other modules, they can import them directly:
# from pyVNC.pyVNC.Buffer import DisplayBuffer, ArrayBuffer
# from pyVNC.pyVNC.constants import *
# from pyVNC.pyVNC.VNCFactory import VNCFactory
