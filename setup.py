from setuptools import setup, find_packages

# Read the version in a robust way
version_dict = {}
with open("esm/version.py") as f:
    exec(f.read(), version_dict)
version = version_dict["__version__"]

setup(
    name="fair-esm",
    version=version,
    description="Evolutionary Scale Modeling (ESM) from FAIR - djp fork",
    author="Meta AI & Dean Procter",
    url="https://github.com/djproc/esm",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)