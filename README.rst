==================
thrifty README
==================

thrifty is a Python-based generator for `Apache Thrift`_ source files.

You can get thrifty via ``git``::

    git clone git://github.com/euphoria/thrifty

And install it via::

    python setup.py install

thrifty can also be easily installed from PyPI_ using ``easy_install``::

    easy_install -U thrifty

.. _`Apache Thrift`: http://incubator.apache.org/thrift/
.. _PyPI: http://pypi.python.org/pypi

Usage
=====

``thriftyc``, the command-line compiler, is invoked using similar commands as
the original Apache Thrift compiler.

An example generating Python and C# output from the Thrift tutorial::

    thriftyc --gen python --gen csharp tutorial.thrift

License
=======

thrifty is licensed under the `Apache Software License`_, which is
distributed with the source in the ``LICENSE.txt`` file.

.. _`Apache Software License`: http://www.apache.org/licenses/LICENSE-2.0.html
