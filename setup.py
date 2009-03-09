try:
    from setuptools import setup, find_packages
except:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import thrifty

author, email = thrifty.__author__[:-1].split(' <')

setup(
    name='Thrifty',
    version=thrifty.__version__,
    description=thrifty.__doc__,
    long_description=open('README.rst').read(),
    keywords='thrift parser generator serialization rpc',
    license='Apache Software License',
    author=author,
    author_email=email,
    url=thrifty.__url__,
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
        [pygments.lexers]
        thrift = thrifty.ext.pygments:ThriftLexer

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
