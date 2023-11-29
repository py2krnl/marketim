from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in stok_takip/__init__.py
from stok_takip import __version__ as version

setup(
	name="stok_takip",
	version=version,
	description="Stok Takibi Uygulaması",
	author="py2krnl",
	author_email="admin@admin.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
