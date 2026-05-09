from setuptools import setup, find_packages

setup(
    name="PyKeyeasy", # You can use a unique name here
    version="1.0.1",
    author="Emiliano",
    description="Ultra-simple keyboard detection with automatic variables",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/emicics/PyKeys",
    packages=find_packages(),
    install_requires=[
        "keyboard",
        "threading",
		"time"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires='>=3.6',
)
