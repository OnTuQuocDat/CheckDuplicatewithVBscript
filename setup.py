import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {
#     "excludes": ["tkinter", "unittest"],
#     "zip_include_packages": ["encodings", "PySide6"],
# }
build_exe_options = {"packages": ["os"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name="GammaSU",
    version="2.0.2",
    description="GammaSU application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("new_main.py", base=base)]
)