from setuptools import setup, find_packages


tests_require = [

]

install_requires = [
    'icalendar == 3.9.0',
]

packages = find_packages(
    '.', exclude=('tests', 'tests.*')
)

setup(
    name='ical2org',
    version='0.0.1',
    author='Marc Sherry',
    author_email='msherry@gmail.com',
    packages=packages,
    tests_require=tests_require,
    install_requires=install_requires,
    extras_require={'test': tests_require},
)
