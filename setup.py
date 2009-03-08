__version__ = '0.1'

try:
    from setuptools import setup, find_packages
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='thrifty',
    version=__version__,
    description='thrifty is a Python-based generator for Apache Thrift source',
    long_description=open('README.rst').read(),
    keywords='thrift parser generator serialization rpc',
    license='Apache Software License',
    author='Michael Greene',
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
        [thrifty.generator]
        csharp = thrifty.gen.csharp:CSharpGenerator
        html = thrifty.gen.html:HTMLGenerator
        py = thrifty.gen.py:PythonGenerator
    """,
    install_requires=[
        'ply',
        'setuptools',
    ],
    zip_safe=False,
)
