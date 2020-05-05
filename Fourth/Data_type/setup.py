from distutils.core import setup, Extension

module = Extension("Volume", sources = ["Volume.c"])

setup(name="Volumes",
		ext_modules = [module])