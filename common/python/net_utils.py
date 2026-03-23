"""
net_utils.py

versatile project only changing when i work on this with other operating systems
current supported os include linux
planning for all operating systems supported by sys
"""

from os import *
from sys import platform


def ipchange(newip: str, os: str=="linux"):
    if os == "win32":
        print("windows will be supported soon")
    elif os == "darwin":
        print("mac will be supported soon")
    elif os == "linux":
        con = popen("nmcli con show").readlines()[1].split(" ")[0]
        system(f"nmcli con mod {con} ipv4.method manual ipv4.address {newip}")
        print("ipv4 address changed to " + newip)
    else:
        print("operating system " + platform + " not supported")


if __name__ == "__main__":
    ipchange("192.168.0.222/24", platform)