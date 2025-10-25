"""Core implementation compiled with Cython for distribution."""


def hello() -> str:
    """Return a friendly greeting to verify the compiled package works."""
    return "Hello from libc"
