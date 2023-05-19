from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='miniagent',
    version='0.0.7',
    long_description = long_description,
    long_description_content_type='text/markdown',
    description='Multi-adaptable and lightweight server framework based on Flask',
    author='tanminkwan',
    author_email='tanminkwan@gmail.com',
    license= 'MIT',
    url='https://github.com/tanminkwan/local-agent',
    packages=find_packages(exclude=[]),
    keywords=['flask', 'sqlalchemy', 'scheduler', 'zipkin', 'kafka'],
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
    install_requires=[
        'aniso8601>=9.0.1',
        'APScheduler>=3.10.1',
        'blinker>=1.6.2',
        'certifi>=2022.12.7',
        'charset-normalizer>=3.1.0',
        'click>=8.1.3',
        'Flask>=2.3.1',
        'Flask-API>=3.0.post1',
        'Flask-APScheduler>=1.12.4',
        'Flask-Cors>=3.0.10',
        'Flask-RESTful>=0.3.9',
        'Flask-SQLAlchemy>=3.0.3',
        'greenlet>=2.0.2',
        'idna>=3.4',
        'itsdangerous>=2.1.2',
        'Jinja2>=3.1.2',
        'kafka-python>=2.0.2',
        'MarkupSafe>=2.1.2',
        'polling2>=0.5.0',
        'python-dateutil>=2.8.2',
        'pytz>=2023.3',
        'pytz-deprecation-shim>=0.1.0.post0',
        'requests>=2.29.0',
        'six>=1.16.0',
        'SQLAlchemy>=2.0.11',
        'typing_extensions>=4.5.0',
        'tzdata>=2023.3',
        'tzlocal>=4.3',
        'urllib3>=1.26.15',
        'Werkzeug>=2.3.2',
        'PyGithub>=1.58.1',
        'py-zipkin>=1.2.8',
    ]
)