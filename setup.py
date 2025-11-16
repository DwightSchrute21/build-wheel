from setuptools import setup
from Cython.Build import cythonize
from setuptools.command.build_py import build_py as _build_py
import sys

#prevent compilation when pip install -e
if any( arg in [ 'sdist', 'bdist_wheel'] for arg in sys.argv ):
    ext_modules = cythonize("libc/**/*.py", language_level="3", compiler_directives={"binding": False, "emit_code_comments": False})
else:
    ext_modules = []

#prevent pushing .py in the wheel
class build_py_skip_modules(_build_py):
    """Override build_py to skip copying .py modules into build/lib."""
    def get_source_files(self):
        # return empty: setuptools won't try to copy Python sources
        return []

    def build_module(self, module, module_file, package):
        # no-op: don't build/copy python sources
        return


setup(
    name = "libc",
    version = "0.1.0",
    packages = ["libc"],
    ext_modules = ext_modules,
    cmdclass={"build_py": build_py_skip_modules},
    zip_safe=False,
)