from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import numpy


try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    bdist_wheel = None

# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
ext = '.pyx' if USE_CYTHON else '.c'
extensions = [
    Extension(
        name="ctc_segmentation.ctc_segmentation_dyn",
        sources=["ctc_segmentation/ctc_segmentation_dyn"+ext],
        include_dirs=[numpy.get_include()],
    )
]
if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

package_information = """
# CTC segmentation

CTC segmentation is used to align utterances within audio files.
It can be combined with CTC-based ASR models.
This package includes the core functions.

https://github.com/lumaku/ctc-segmentation
"""

cmdclass={'build_ext': build_ext}


if bdist_wheel:
    cmdclass['bdist_wheel'] = bdist_wheel

setup(
    name="ctc_segmentation",
    version="1.7.4",
    python_requires='>=3.6',
    packages=['ctc_segmentation'],
    include_package_data=True,
    setup_requires=["numpy"],
    install_requires=["setuptools", "numpy", "Cython"],
    zip_safe=False,
    ext_modules=extensions,
    cmdclass=cmdclass,

    author="Ludwig Kuerzinger <ludwig.kuerzinger@tum.de>, "
           "Dominik Winkelbauer <dominik.winkelbauer@tum.de>",
    description="CTC segmentation to align utterances within "
                "large audio files.",

    long_description_content_type="text/markdown",
    long_description=package_information,
)
