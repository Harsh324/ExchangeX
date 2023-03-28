from setuptools import find_packages, setup

setup(
    name = 'payment',
    packages = find_packages(include = ['payment']),
    version = '0.1.0',
    description = 'payment package',
    author = 'Harsh Tripathi',
    license = '',
    install_requires = [],
    setup_requires = ['pytest-runner'],
    test_require = ['pytest'],
    test_suite = 'tests',
)