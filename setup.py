from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='miniagent',
    version='0.0.4',
    long_description = long_description,
    long_description_content_type='text/markdown',
    description='Multi-adaptable and lightweight application framework based on Flask',
    author='tanminkwan',
    author_email='tanminkwan@gmail.com',
    license= 'MIT',
    url='https://github.com/tanminkwan/local-agent',
    packages=find_packages(exclude=[]),
    keywords=['flask', 'sqlalchemy', 'scheduler'],
    entry_points={
        'console_scripts': [
            'mini-project = miniadmin.admin:example_code_download',
        ],
    },
    python_requires='>=3.9',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)