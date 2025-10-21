from setuptools import setup, find_packages

setup(
    name="parqclean",
    version="0.1.0",
    author="Stanley Honkpehedji",
    description="Pipeline simple de nettoyage CSV → Parquet",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pyarrow",
    ],
    entry_points={
        "console_scripts": [
            "parqclean=parqclean.cli:run",
        ],
    },
)
