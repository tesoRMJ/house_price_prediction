from setuptools import setup, find_packages

setup(
    name='house_price_prediction',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ejecucion_JMR = house_price_prediction.__main__:main',
        ],
    },
)
