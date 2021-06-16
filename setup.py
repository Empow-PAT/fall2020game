import cx_Freeze

executables = [cx_Freeze.Executable("run.py")]

cx_Freeze.setup(
    name="Astral Run",
    options={"build_exe": {"namespace_packages": ["pygame_menu"],
                           "includes": ["pygame", "pygame_menu"],
                           "include_files": ["apis/", "Images/", "players/", "sprites/", "terrrain/", "__init__.py"]}},
    executables=executables
    )