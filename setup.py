import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitandpip",
    version="0.0.1",
    author="kenneth joohyun han",
    author_email="kenneth.jh.han@snu.ac.kr",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/KennethJHan/pip_test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
