STRANDS data tools that work with QSRlib
========================================

Trajectory reader
~~~~~~~~~~~~~~~~~

``traj_data_reader.py`` provides the class ``Trajectory_Data_Reader``.
``config.ini`` needs to include qsr options. It can optionally contain
Activity Graph options.

About the ``config.ini``
^^^^^^^^^^^^^^^^^^^^^^^^

Create a ``config.ini`` based on the following template:

.. code:: ini

    [trajectory_data_reader]
    path = <path1>
    ; use load_from_files=True in the constructor to load from the following files
    date = date
    qsr = qtcb
    q = 0_01
    v = False
    n = True

You can add any parameters you like in the config file, but also
initiate them in the data\_reader config `??? <>`__.
