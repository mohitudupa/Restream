"""
Setup file
"""


from setuptools import setup


setup(
    name='restream',
    version='0.0.1',
    description='A python library to parse strings based on tokens and grammar rules',
    url='https://github.com/mohitudupa/restream.git',
    # Entry points provide cross-platform support and allow pip to create the appropriate form of executable for
    # the target platform.
    # http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point

    # If there are any packages in the project that need to be installed, specify them here or use find_packages
    # module to let it do for you
    # http://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
    packages=['restream'],
    install_requires=[],
    # List all the dependencies here. These will be installed by pip when the project is being installed
    # https://packaging.python.org/discussions/install-requires-vs-requirements/#install-requires
)
