from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

extras_require = {}

setup(
    name="mask2former",
    version="0.0.1",
    packages=find_packages(),
    author="Facebook Research",
    install_requires=requirements,
    extras_require=extras_require,
    long_description=open("README.md").read(),
)
