==================
``thrifty`` README
==================

``thrifty`` is a Python-based generator for Apache Thrift source files.

You can get ``thrifty`` via ``git``::

    git clone git://github.com/euphoria/thrifty

And install it via::

    python setup.py install

``thrifty`` can also be conveniently installed from PyPI_ using ``easy_install``::

    easy_install -U thrifty

.. _PyPI: http://pypi.python.org

Usage
=====

``thrifty`` is invoked from the command-line and accepts similar commands as
the original Apache Thrift compiler.

An example generating Python and C# output from the Thrift tutorial::

    thrifty --gen python --gen csharp tutorial.thrift
