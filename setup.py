from setuptools import setup, find_packages

setup(
    name="missmat",
    version="0.1.2",
    author="Thijs van der Plas",
    description="Simple functions to complement matplotlib",
    long_description=open("README.md").read(),  # Long description, usually from README
    long_description_content_type="text/markdown",  # Format of long description
    url="https://github.com/vdplasthijs/missmat",
    packages=find_packages(),
    install_requires=[
        "numpy>=2.2.1",
        "matplotlib>=3.10.0"
    ],
    extras_require={
        "dev": [
            "pytest"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        "Framework :: Matplotlib"
    ],
    python_requires='>=3.10',
    zip_safe=False
)