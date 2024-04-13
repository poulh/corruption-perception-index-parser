from setuptools import setup, find_packages

setup(
    name='country-cpi-score-parser', 
    author='Poul Hornsleth',  
    description='A project to parse country scores from HTML https://www.transparency.org/en/cpi/2023/index/dnk',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',  
    ],
)
