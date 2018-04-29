from setuptools import setup, find_packages
from h.version import version

setup(name='h',
      version=version,
      description='Custom help text aggregator & navigator',
      author='Ben Whittle',
      author_email='benwhittle31@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
        'click'
      ],
      entry_points='''
        [console_scripts]
        h=h.main:cli
      ''')