from setuptools import setup, find_packages
import os


def package_files(directory):
    """see https://stackoverflow.com/questions/27664504/how-to-add-package-data-recursively-in-python-setup-py"""
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


static_files = package_files('MediaTracker/static')
template_files = package_files('MediaTracker/templates')


setup(name='MediaTracker',
      version='1.10',
      description='Tracker for Media',
      author='Sarah Melanie Laura Beharry-Goss',
      setup_requires=[
          'setuptools>=27.3',  # unstated requirement for pytest-runner
          'pytest-runner',
      ],
      install_requires=[
          'flask',
          'mysqlclient',
          'flask-sqlalchemy',
          'sqlalchemy-migrate',
          'flask-wtf',
      ],
      tests_require=[
          'pytest',
          'pytest-cov',
      ],
      package_data={'': static_files + template_files},
      author_email='sarahbeharry@hotmail.com',
      license='MIT',
      packages=find_packages(),
      )
