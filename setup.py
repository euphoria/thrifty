try:
    from setuptools import setup, find_packages
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='thrifty',
    version='0.1',
    description='thrifty is a Python-based generator for Apache Thrift source',
    long_description=open('README.rst').read(),
    keywords='thrift parser generator',
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
    install_requires=[
        'ply',
    ],
    zip_safe=False,
)
