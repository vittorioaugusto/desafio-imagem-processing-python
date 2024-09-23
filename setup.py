from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Rafael Rodrigo",
    email="raf_rodrigo@gmail.com",
    description="Package image processing",
    long_description=page_description,
    long_description_content_tupe="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.4",
)