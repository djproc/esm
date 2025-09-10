from setuptools import setup, find_packages

with open("esm/version.py", "r") as f:
    version = f.read().strip().split("=")[-1].strip("'\"")

setup(
    name="fair-esm",
    version=version,
    description="Evolutionary Scale Modeling (ESM) from FAIR",
    author="Meta AI",
    url="https://github.com/facebookresearch/esm",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
