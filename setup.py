from setuptools import setup, find_packages

setup(name='MediaTracker',
      version='1.10',
      description='Tracker for Media',
      author='Sarah Melanie Laura Beharry-Goss',
      install_requires=[
          'flask',
          'mysqlclient',
          'flask-sqlalchemy',
          'sqlalchemy-migrate',
          'flask-wtf',
      ],
      author_email='sarahbeharry@hotmail.com',
      license='MIT',
      packages=find_packages(),
      )
