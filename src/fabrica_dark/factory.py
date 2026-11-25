"""
Factory configuration for the Fabrica Dark platform.

This module contains the basic factory information.
"""

FACTORY_NAME: str = "Fabrica Dark"
NUMBER_OF_MACHINES: int = 5
NUMBER_OF_PRODUCTS: int = 30
TARGET_CYCLE_TIME_SECONDS: float = 50.0

def get_factory_info() -> str:
    """Return a short description of the factory"""
    return (
        f"{FACTORY_NAME}: "
        f"{NUMBER_OF_MACHINES} machines, "
        f"{NUMBER_OF_PRODUCTS} products, "
        f"target cycle time {TARGET_CYCLE_TIME_SECONDS} seconds. "
    )