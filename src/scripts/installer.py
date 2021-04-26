import platform
import subprocess
import os

script = os.getcwd() + "\src\scripts"
os.chdir(script)

system = platform.system()
if system == "Windows":
    print("Windows Machine")
    subprocess.call([r'install.bat'])

elif system == "Darwin":
    print("Mac OS Machine")

elif system == "Linux":
    print("Linux Machine")
    subprocess.call([r'install.sh'])

else:
    print("unsupported machine")