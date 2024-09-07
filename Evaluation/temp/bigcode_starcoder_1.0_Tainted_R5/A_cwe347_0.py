'''


The ``halo`` command displays the details of a specific halo, and provides a
quick way to get started interacting with a simulation's halo(s).

By default all subcommands are executed via MPI; see
:ref:`Running Simulations<running-label>` for important information about
how to modify this behavior.

Usage:

.. code-block:: bash

  halomod halo [FLAGS]

.. todo::

  Need to fill this out.

Flags:

.. list-table::
  :widths: 10 10 80
  :header-rows: 1


  * - Flag
    - Short Flag
    - Description
  * - ``--header``
    - ``-H``
    - Provides information about the columns in the halo catalog.
  * - ``--help``
    - ``-h``
    - Prints the help text and quits.

Subcommands:

.. list-table::
  :widths: 10 80
  :header-rows: 1

  * - Subcommand
    - Description
  * - :ref:`halomod-halo-get <get>`
    - Gets