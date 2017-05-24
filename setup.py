import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-utphy-richdocument',
    version='0.6',
    url='https://github.com/jcuotpc/wagtail-utphy-richdocument',
    packages=find_packages(),
    include_package_data=True,
    keywords = ['wagtail', 'richdocument'],
    license='BSD License',
    description='A Wagtail richdocument content type built with wagtail straemfield.',
    long_description=README,
    author='Julian Comanean',
    author_email='icom@physics.utoronto.ca',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
