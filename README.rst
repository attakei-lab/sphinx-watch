============
sphinx-watch
============

This is CLI tool for Documentation eXperimence with Sphinx.

Overview
========

``sphinx-watch`` provides these features for user local environment.

* Build document of Sphinx when source files are changed by users
* HTTP server to publish built documentation using ``http.server``

Installation
============

Uploaded PyPI

.. code-block::

   pip install sphinx-watch

Usage
=====

Build only

.. code-block:: console

   sphinx-watch source build html

Run HTTP server

.. code-block:: console

   sphinx-watch source build html --http

Specify port by running HTTP server

.. code-block:: console

   sphinx-watch source build html --http --port 8080

Development
===========

This uses ``poetry`` and ``pre-commit``

.. code-block:: console

   git clone
   cd sphinx-watch
   poetry install
   pre-commit install

License
=======

Apache License 2.0
