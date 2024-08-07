from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='char_charm',
    version='0.1.0',
    description='char-charm, charm of ASCII art',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sbartoszuk/char-charm',
    author='Szymon Bartoszuk',
    author_email='s.bartoszuk@proton.me',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='ASCII art',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.6, <4',
    install_requires=[
        'Pillow',
    ],
    package_data={
        'char_charm': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'char-charm=char_charm:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/sbartoszuk/char-charm',
    },
)
