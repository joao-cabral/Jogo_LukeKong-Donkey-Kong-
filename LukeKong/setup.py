import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("LukeKong.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Luke kong",
    version = "1.0",
    description = "Feito por Joao Cabral",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
