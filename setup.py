from setuptools import setup, find_packages
import sdscli

setup(
    name='sdscli',
    version=sdscli.__version__,
    long_description=sdscli.__description__,
    url=sdscli.__url__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'boto3', 'hysds', 'hysds_commons', 'osaka', 
        'prov_es', 'requests', 'backoff'
    ],
    entry_points={
        'console_scripts': [
            'sds=sdscli.command_line:main'
        ]
    }
)
