STRANDS data tools that work with QSRlib
========================================

This package aims to provide easy parsing of various datasets mainly
keeping them in QSRlib format.

It might end up being part of the QSRlib given its functionality and
strong dependency to it.

There are usually two types of files: \* ``readers``: responsible for
reading from the raw data or from saved files and keeping the raw data
(and other info as needed) in some QSRlib friendly format. \*
``keepers``: responsible for taking a reader and making QSRs via QSRlib.
They usually have the option to load the QSRs directly from some file.

Available tools for the following datasets
------------------------------------------

-  CAD120 (`info <http://pr.cs.cornell.edu/humanactivities/data.php>`__)

Usage and Help
--------------

Installation
~~~~~~~~~~~~

You do need to have
`QSRlib <https://github.com/strands-project/strands_qsr_lib>`__
somewhere installed where it can be found by the ``readers`` and the
``keepers``. Easiest way is probably to modify your ``PYTHONPATH`` or if
you are using an IDE then check its documentation on how to resolve
dependencies.

CAD120 reader
~~~~~~~~~~~~~

``cad120_data_reader.py`` provides the class ``CAD120_Data_Reader``. In
most cases it is enough to just call the constructor without any of the
optional arguments, and if you have a suitable ``config.ini`` then
things should go smoothly.

About the ``config.ini``
^^^^^^^^^^^^^^^^^^^^^^^^

Create a ``config.ini`` base on the following template that tells where
the CAD120 folder is. If the notion of corrected ``labeling.txt`` files
makes no sense then just use the same path for both ``<path1>`` and
``<path2>``.

.. code:: ini

    [cad120_data_reader]
    path = <path1>/CAD_120
    corrected_labeling_path = <path2>/CAD_120
    ; use load_from_files=True in the constructor to load from the following files
    sub_sequences_filename = <pickle_file.p>
    sub_time_segmentation_filename = <pickle_file.p>
    ground_truth_tracks_filename = <pickle_file.p>

Just make sure that your program can find your ``config.ini``. If you
are not familiar how to do this then an easy way is to pass the
directory of ``config.ini`` in the constructor, e.g.:

.. code:: python

    reader = CAD120_Data_Reader(config_path=<path string to config.ini>)

CAD120 keeper
~~~~~~~~~~~~~

``cad120_qsr_keeper.py`` provides the class ``CAD120_QSR_Keeper``. If
you want to make QSRs from the reader then you need to pass some
parameters. See the main part for an example and you will need a
``local.ini`` file. If you want to load the QSRs from a file simply call
with argument \`-l .

Running ``cad120_qsr_keeper.py -h`` will give sufficient help also.

About the ``local.ini``
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: ini

    [local]
    reader_ini = <reader config.ini file>
    reader_load = true

``reader_load`` true if you want the ``reader`` to load the data from
the files in the ``config.ini``


Original page: https://github.com/strands-project/strands_data_to_qsrlib/blob/master/README.md