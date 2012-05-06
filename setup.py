from setuptools import setup, find_packages
import os

version = '0.0.0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_colorpicker', 'test_jquery_colorpicker.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_colorpicker',
    version=version,
    description="fanstatic jQuery color picker",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Misato Takahashi',
    author_email='misato@takahashi.name',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'jquery.colorpicker = js.jquery_colorpicker:library',
            ],
        },
    )
