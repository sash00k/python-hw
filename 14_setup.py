from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension('extension_module',  ['14_my_extension.py']),
]

setup(
    name = 'My Extension',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)