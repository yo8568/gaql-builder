from setuptools import setup, find_packages
from codecs import open

tests_require = [
    'pytest >= 4.4'
]

setup(
    name="gaql-builder",
    version="1.0.1",
    author="Shao-Tung Change",
    author_email="yo8568@gmail.com",
    description="Generating GAQL tool",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yo8568/gaql-builder",
    packages=find_packages(exclude=['tests', 'test_*']),
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'gaql_builder=gaql_builder:main'
        ],
    },
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
