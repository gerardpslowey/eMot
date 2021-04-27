import platform
import subprocess
import os

script = f"{os.getcwd()}\src\scripts" # noqa
os.chdir(script)

system = platform.system()
if system == "Windows":
    print("Windows Machine")
    subprocess.call([r'start.bat'])

elif system == "Darwin":
    print("Mac OS Machine")

elif system == "Linux":
    print("Linux Machine")
    subprocess.call([r'start.sh'])

else:
    print("Unsupported Machine")
