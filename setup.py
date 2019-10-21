import os
from setuptools import setup
from setuptools import find_packages

NAME = 'CJKSplitter'

here = os.path.abspath(os.path.dirname(__file__))
package = os.path.join(here, 'Products', NAME)

def _package_doc(name):
    f = open(os.path.join(package, name))
    return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'
README = ( _package_doc('README.txt')
         + _boundary
         + _package_doc('HISTORY.txt')
         )

setup(name='Products.%s' % NAME,
      version=_package_doc('version.txt').strip(),
      description='%s product' % NAME,
      long_description=README,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Indexing",
        ],
      keywords='zope2 cmf plone text index chinese japanese korean',
      author="Zopen",
      author_email="panjy@zopen.cn",
      url="http://pypi.python.org/pypi/Products.%s" % NAME,
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      install_requires=['setuptools',
                        'Zope2',
                       ],
      tests_require=[],
      test_suite="Products.%s.tests" % NAME,
      entry_points="""
      """,
)
