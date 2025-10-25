from setuptools import setup
from Cython.Build import cythonize
from setuptools.command.build_py import build_py as _build_py

ext_modules = cythonize("libc/**/*.py", language_level="3")
# ext_modules = []

class build_py_skip_modules(_build_py):
    """Override build_py to skip copying .py modules into build/lib."""
    def get_source_files(self):
        # return empty: setuptools won't try to copy Python sources
        return []

    def build_module(self, module, module_file, package):
        # no-op: don't build/copy python sources
        return
    
setup(
    ext_modules=ext_modules,
    cmdclass={"build_py": build_py_skip_modules},
    zip_safe=False,
    compiler_directives={"binding": False, "docstrings": False, "emit_code_comments": False}
)
