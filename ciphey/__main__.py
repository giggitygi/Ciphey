#! /usr/bin/env python3

"""
Ciphey: https://github.com/Ciphey/Ciphey
"""

import platform
import sys

if __name__ == "__main__":
    major = sys.version_info[0]
    minor = sys.version_info[1]

    python_version = (
        str(sys.version_info[0])
        + "."
        + str(sys.version_info[1])
        + "."
        + str(sys.version_info[2])
    )

    if major != 3 or minor < 8:
        print(
            f"Ciphey requires Python 3.8+, you are using {python_version}. Please install a higher Python version. https://www.python.org/downloads/"
        )
        print(
            "Alternatively, visit our Discord and use the Ciphey bot in #bots http://discord.skerritt.blog"
        )
        sys.exit(1)

    if platform.system() == "Windows" and sys.maxsize <= 2 ** 32:
        print(
            "You are using Python 32 bit on Windows. Ciphey requires Python 64-bit. Please upgrade here: https://www.python.org/downloads/"
        )
        sys.exit(1)
        
    from .ciphey import main

    main()
