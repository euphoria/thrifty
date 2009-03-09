"""
Thrifty is a Python-based parser generator for Apache Thrift source
"""
__version__ = '0.1'
__author__ = 'Michael Greene'

try:
    from setuptools import setup, find_packages
except:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='Thrifty',
    version=__version__,
    description=__doc__,
    long_description=open('README.rst').read(),
    keywords='thrift parser generator serialization rpc',
    license='Apache Software License',
    author=__author__,
    author_email='michael.greene@gmail.com',
    url='http://github.com/euphoria/thrifty/',
    dependency_links=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Code Generators',
    ],
    packages=find_packages(),
    include_package_data=True,
    scripts=['thrifty/bin/thriftyc.py'],
    entry_points="""
        [thrifty.generators]
        csharp = thrifty.generators.csharp:CSharpGenerator
        html = thrifty.generators.html:HTMLGenerator
        py = thrifty.generators.python:PythonGenerator
    """,
    install_requires=[
        'ply',
        'setuptools',
    ],
    zip_safe=False,
)
