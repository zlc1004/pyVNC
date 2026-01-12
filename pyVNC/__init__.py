"""
pyVNC core modules

To avoid circular import issues, only import what's absolutely necessary.
For specific modules, import them directly:
  from pyVNC.pyVNC.Client import Client
  from pyVNC.pyVNC.Buffer import DisplayBuffer
  etc.
"""

# Keep it minimal to avoid circular imports
__version__ = "0.1"
