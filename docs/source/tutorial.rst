.. image:: _static/images/logo.svg
   :width: 100px
   :alt: phrasebook
   :align: right

.. toctree::
    :glob:

.. _tutorial:

Tutorial
========

`phrasebook` is designed to make it relatively simple for you to place files containing string
templates alongside your python modules.  You have a few different options for doing so: You can
place all your strings in a :ref:`single file <tutorial_single_file>` or you can break them out into
:ref:`multiple files within a directory <tutorial_directory>`.  While we've tried to use simple
naming conventions to minimize the boiler plate for creating a
:ref:`single phrasebook for a module <tutorial_single_file>`, you can also create as many
phrasebooks as you need by :ref:`specifying the path <tutorial_specify_path>` for each one.

.. _tutorial_single_file:

Single File Phrasebook
----------------------

If you have just a few simple strings, you can place them all in a single
`toml <https://pypi.org/project/toml/>`_ file.

.. code-block:: ini
    :caption: my_module.phr

    txt1 = "Hello, $NAME."
    txt2 = "Hello, $YOURNAME.  My name is $MYNAME."

    [sub1]
    txt1 = "Hello again, $NAME"
    txt2 = "Hello again, $YOURNAME.  My name is still $MYNAME."

You can then access it from a python module with the same base name.

.. note::

    If you don't supply the `path` constructor argument, the
    :py:class:`Phrasebook <phrasebook.phrasebook.Phrasebook>` class will attempt to
    find a file or directory with the same name as the current module with the `.phr` suffix.

.. code-block:: python
    :caption: my_module.py

    from phrasebook import Phrasebook

    phrasebook = Phrasebook().load()

    print(phrasebook.substitute('txt1', NAME='Eric'))
    print(phrasebook.substitute('txt2', YOURNAME='Eric', MYNAME='Terry'))

    print(phrasebook.substitute('sub1.txt1', NAME='Eric'))
    print(phrasebook.substitute('sub1.txt2', YOURNAME='Eric', MYNAME='Terry'))


.. code-block:: sh
    :caption: output

    Hello, Eric.
    Hello, Eric.  My name is Terry.
    Hello again, Eric
    Hello again, Eric.  My name is still Terry.


.. _tutorial_directory:

Phrasebook Directory
--------------------

.. code-block:: ini
    :caption: my_module.phr/query1.sql

    SELECT $COLUMN FROM $TABLE


.. code-block:: ini
    :caption: my_module.phr/sub1/query2.sql

    SELECT $COLUMN1, $COLUMN2 FROM $TABLE

.. code-block:: python
    :caption: my_module.py

    from phrasebook import Phrasebook

    phrasebook = Phrasebook().load()

    print(phrasebook.substitute('query1', COLUMN='first', TABLE='names'))
    print(
        phrasebook.substitute(
            'sub1.query2',
            COLUMN1='first',
            COLUMN2='last',
            TABLE='names'
        )
    )


.. code-block:: sh
    :caption: output

    SELECT first FROM names
    SELECT first, last FROM names

.. _tutorial_specify_path:

Specifying the Path
-------------------

TODO

