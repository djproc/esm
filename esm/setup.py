from setuptools import setup, find_packages

setup(
    name='esm_djp',
    version='0.1.0',
    packages=find_packages(),
    author='Dean Procter',
    author_email='',
    description='A vendored, self-contained version of the ESM library for local analysis.',
    install_requires=[
        # Add any direct dependencies of the esm_djp library itself here
        # For now, we will assume they are covered by the main requirements.txt
    ],
)
