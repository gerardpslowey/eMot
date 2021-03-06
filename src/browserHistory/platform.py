import enum
import platform


class Platform(enum.Enum):
    """
    An enum used to indicate the system's platform.
    A value of 0 is reserved for unknown platforms.
    """

    OTHER = 0
    LINUX = 1
    MAC = 2
    WINDOWS = 3


# Returns the current platform
def getPlatform():
    system = platform.system()
    if system == "Linux":
        return Platform.LINUX
    if system == "Darwin":
        return Platform.MAC
    if system == "Windows":
        return Platform.WINDOWS
    raise NotImplementedError(f"Platform {system} is not supported yet")
