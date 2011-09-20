from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='SilverSync',
      version=version,
      description="A firefox sync client library for python, for the SilverLining browser",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python firefox sync api',
      author='Ivo van der Wijk',
      author_email='silversync@in.m3r.nl',
      url='http://vanderwijk.info/',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "requests",
          "M2Crypto"
      ],
      entry_points={
        "console_scripts":[
            "synctest=silversync.client:main",
            "normalize=silversync.normalize:main"
        ]
      },
      )
