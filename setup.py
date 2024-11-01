from setuptools import setup, find_packages

setup(
    name="swaig-cli",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "swaig_cli=swaig_cli.cli:main",  # Define CLI entry point
        ],
    },
    data_files=[('/usr/local/share/man/man1', ['man/swaig_cli.1'])],  # Install man page
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
