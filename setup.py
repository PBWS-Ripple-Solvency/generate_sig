import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("ring_proof_verifier.py", base=base)]

setup(name="ring_proof_verifier",
      version="0.1",
      description="My Ring Proof app",
      options={"build_exe": build_exe_options},
      executables=executables,
      data_files=[("bitcoin", ["bitcoin/english.txt"]), (".", ["definitions.json"])])
