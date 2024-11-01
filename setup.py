from setuptools import setup, find_packages

setup(
    name="swaig-cli",
    version="0.1.4",
    author="Brian West",
    author_email="brian@signalwire.com",
    description="A command-line tool for testing SignalWire AI Gateway functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/briankwest/swaig-cli",
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "swaig_cli=swaig_cli.cli:main",  # Define CLI entry point
        ],
    },
    data_files=[('/usr/local/share/man/man1', ['man/swaig_cli.1'])],  # Install man page
    install_requires=[
        "requests",
        "wheel"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
