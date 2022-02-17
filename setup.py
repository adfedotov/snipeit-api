import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='snipeit-api',  
    version='0.1',
    author="Andrei Fedotov",
    author_email="Andrei Fedotov",
    description="SnipeIT API controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adfedotov/snipeit-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)