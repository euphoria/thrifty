# Makefile for Thrifty parser/generator
#
#   This serves no purpose day-to-day, but is used each time someone
#   would like to smash this file into the Apache Thrift source tree.
#   Normally, you would run:
#
#     python setup.py develop

all: dist

dist:
	python setup.py bdist_egg
	python setup.py sdist

install:
	python setup.py install

clean:
	python setup.py clean
	rm -rf dist/*

.PHONY: all clean dist install
