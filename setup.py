import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pandas"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "test",
        version = "0.1",
        options = {"build_exe": build_exe_options},
        executables = [Executable("note pad.py", base=base)])