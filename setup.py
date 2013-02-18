from distutils.core import setup
from setuptools import find_packages

description = 'Generate HTML output for Python unittest results'

setup(
    name='gadzooks',
    version='0.1.0',
    author=u'Kris Rogers',
    author_email='kris.rogers.01@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    url='https://github.com/krisrogers/gadzooks-python',
    license='LICENCE.txt',
    description=description,
    long_description=description,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    gadzooks = gadzooks.core:main
    """,
)