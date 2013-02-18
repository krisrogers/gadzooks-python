from distutils.core import setup
from setuptools import find_packages

setup(
    name='gadzooks',
    version='0.1.0',
    author=u'Kris Rogers',
    author_email='kris.rogers.01@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    url='https://github.com/krisrogers/gadzooks-python',
    license='LICENCE.txt',
    description='Generate HTML output for Python unittest results',
    long_description='TODO',
    zip_safe=False,
)