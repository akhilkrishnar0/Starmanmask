from setuptools import setup, find_packages

setup(
    name="starcleaner",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'astroquery',
        'astropy',
        'requests'
    ],
    description="A package mask stars",
    author="Akhil Krishna R",
    author_email="akhil.r@res.christuniversity.in",
    url="https://github.com/akhilkrishnar0/starcleaner",
)
