import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

<<<<<<< HEAD
setup(name='Prj',
      version='0.0',
      description='Prj',
=======
setup(name='Prjt',
      version='0.0',
      description='Prjt',
>>>>>>> 285f6f0ed29be16f453d4ccfab0b974c0fb1db6a
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
<<<<<<< HEAD
      main = prj:main
      [console_scripts]
      initialize_Prj_db = prj.scripts.initializedb:main
=======
      main = prjt:main
      [console_scripts]
      initialize_Prjt_db = prjt.scripts.initializedb:main
>>>>>>> 285f6f0ed29be16f453d4ccfab0b974c0fb1db6a
      """,
      )
