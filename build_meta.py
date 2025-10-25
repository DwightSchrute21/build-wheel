# build_meta.py
from setuptools import setup
from setuptools.command.build_py import build_py as _build_py
from setuptools.build_meta import build_wheel as _build_wheel, build_editable as _build_editable
from Cython.Build import cythonize

class build_py_skip_modules(_build_py):
    def get_source_files(self): 
        return []
    def build_module(self, module, module_file, package): 
        return

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):

    ext_modules = cythonize("libc/**/*.py", 
                            language_level="3",
                            compiler_directives={"binding": False, "docstrings": False}
                            )
    setup(
        name="libc",
        packages=["libc"],
        ext_modules=ext_modules,
        cmdclass={"build_py": build_py_skip_modules},
        include_package_data=False,
        zip_safe=False,
    )
    return _build_wheel(wheel_directory, config_settings, metadata_directory)

def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    # editable: skip compiling or leave ext_modules=[]
    setup(name="libc", 
          packages=["libc"], 
          ext_modules=[], 
          zip_safe=False)
    return _build_editable(wheel_directory, config_settings, metadata_directory)
