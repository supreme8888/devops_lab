from setuptools import setup, find_packages

setup(
    name="homework3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = main.snapshot:main",
        ],
    },
    install_requires=[
        "argsparse", "psutil", "datetime"
    ],
    version="0.1",
    author="Viktor Gulinskiy",
    author_email="Viktor_Gulinsliy@epam.com",
    description="Test app",
    license="MIT",
)
