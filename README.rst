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

   sphinx-watch source build html --httpd

Specify port by running HTTP server

.. code-block:: console

   sphinx-watch source build html --httpd --port 8080

Development
===========

This uses ``flit`` and ``pre-commit``

.. code-block:: console

   git clone
   cd sphinx-watch
   flit build
   pre-commit install

Or install `tox <https://tox.wiki/en/latest/installation.html>`_ and use the `./Makefile
<./Makefile>`_:

.. code-block:: console

   make

License
=======

Apache License 2.0
