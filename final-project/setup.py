import cx_Freeze
import glob

executables = [cx_Freeze.Executable("main.py")] + [cx_Freeze.Executable(f) for f in glob.glob('scenes/*')]
files_to_include = glob.glob('assets/*.*', recursive=True) + glob.glob(
    'sound/*.*', recursive=True) + glob.glob('dialogue/*.*', recursive=True)

cx_Freeze.setup(
    name="Comfort Cafe",
    options={"build_exe": {"packages":["pygame", "ast", "sys", 'os', 'random', 'numpy'],
                           "include_files": files_to_include}},
    executables = executables

    )