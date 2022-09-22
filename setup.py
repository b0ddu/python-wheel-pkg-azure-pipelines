import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ado_wheel_pkg",
    version="0.0.9",
    author="Sankeerth Boddu",
    author_email="mail@san.de",
    description="Python Wheel Package Deployment Using Adobe Pipelines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sankeerthb/python-wheel-pkg-azure-pipelines",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)