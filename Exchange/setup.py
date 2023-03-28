from setuptools import find_packages, setup

setup(
    name = 'exchange',
    packages = find_packages(include = ['exchange']),
    version = '0.1.0',
    description = 'Exchange package',
    author = 'Harsh Tripathi',
    license = '',
    install_requires = [],
    setup_requires = ['pytest-runner'],
    test_require = ['pytest'],
    test_suite = 'tests',
)