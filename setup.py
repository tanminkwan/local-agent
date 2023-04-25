from setuptools import setup, find_packages

setup(
    name='mini-agent',
    version='0.0.1',
    description='PYPI tutorial package creation written by TeddyNote',
    author='tanminkwan',
    author_email='tanminkwan@gmail.com',
    url='https://github.com/teddylee777/teddynote',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['flask', 'sqlalchemy', 'scheduler'],
    python_requires='>=3.9',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)