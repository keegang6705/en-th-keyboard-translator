import setuptools
from os import path

def ReadFile(fname):
    return open(path.join(path.dirname(__file__), fname), "r").read()

setuptools.setup(
    name="key-changer",
    version="0.0.1",
    description="Translate characters caused by typos because you forgot to change the keyboard language layout",
    long_description=ReadFile("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/keegang6705/en-th-keyboard-translator",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
