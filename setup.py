import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logfly",
    version="0.8",
    author="Yuan Sui",
    author_email="orisui@icloud.com",
    description="Aa simple log tool by python  ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://about.guki.me",
    project_urls={
        "Github": "https://github.com/tinqlo/logfly",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "srcc"},
    packages=setuptools.find_packages(where="srcc"),
    python_requires=">=3.6",
)