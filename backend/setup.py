import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teacheress",
    version="0.0.1",
    author="Tobias Lausch",
    author_email="mail@lauscht.com",
    description="A project for organization of appointments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lauscht/teacheress",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
