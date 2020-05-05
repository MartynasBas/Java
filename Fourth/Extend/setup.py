from distutils.core import setup, Extension

module = Extension("shortString", sources = ["shortString.c"])

setup(name="shortString",
		ext_modules = [module])