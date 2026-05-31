import os
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_theme/__init__.py
from custom_theme import __version__ as version

setup(
	name="custom_theme",
	version=version,
	description="A beautiful, vibrant modern UI theme for Frappe",
	author="Developer",
	author_email="hello@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
