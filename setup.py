from setuptools import setup, find_packages

setup(name='MediaTracker',
      version='0.1',
      description='Tracker for Media',
      author='Sarah Melanie Laura Beharry-Goss',
      install_requires=[
          'flask',
          'flask-sqlalchemy',
          'flask-wtf',
      ],
      author_email='sarahbeharry@hotmail.com',
      license='MIT',
      packages=find_packages(),
      )
