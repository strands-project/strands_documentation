Object/people presence aka where is Waldo? datasets
---------------------------------------------------

This dataset contains information about people and object presence gathered in three different environments. The dataset is divided in three smaller ones according to the environment these were gathered in:

-  **Aruba** dataset of person presence collected at a smart apartment by the Center for Advanced Studies in Adaptive Systems, `CASAS <http://ailab.wsu.edu/casas/>`__,
-  **Brayford** dataset of person presence created at the premised of the Lincoln Centre for Autonomous System, `LCAS <http://robots.lincoln.ac.uk/>`__),
-  **KTH** dataset of object presence created by the Centre of Autonomous Systems of the Royal Institute of Technology in Stockholm, `CAS/KTH <http://www.cas.kth.se/>`__.

--------------

Dataset structure
~~~~~~~~~~~~~~~~~

Aruba
^^^^^

|image0|

|image1|

Aruba apartment visualisation

Aruba sensor layout (see `CASAS <http://ailab.wsu.edu/casas/>`__)

The **Aruba** folder contains *locations.min*, which contains the location (room) of a person in a small apartment every minute for 16 weeks. The *locations.names* indicate which rooms corresponds to which number. Example: number 0 on line 10 of the locations.min means that in 10th minute after midnight of the first day, the person was in the *Master bedroom*. **Aruba** was extracted from the `CASAS <http://ailab.wsu.edu/casas/>`__ datasets.

Brayford
^^^^^^^^

|image2|

Brayford office locations and topological structure

The **Brayford** directory contains presence of people every 10 minutes on eight different areas in an open-plan office. Again, *locations.names* file describes the locations. Example: Having '0' on line 6 of file 'learning\_06.txt' means that there was no-one at 1:00AM in the kitchenette.

KTH
^^^

|image3|

KTH dataset: object retrieval from point cloud data

The **KTH** data containe presence of objects observed by a mobile robot at different rooms of the `CAS/KTH <http://www.cas.kth.se/>`__. The observations are stored in \*.occ files that have 'epoch time' + presence of a given object at that time. Description of the individual objects is also provided in the *clusters\_meaning* file. Example: line 50 of the *test/31.occ* file indicates that 'Johan's laptop' was present at time 1411317123 (which is Sunday September 21, 2014 18:32:03).

--------------

Download
~~~~~~~~

All of these datasets are available for download in a single archive `file <presence/strands.zip>`__. After you unzip the file, you get three folders which correspond to the individual datasets.

--------------

Condition of use
~~~~~~~~~~~~~~~~

If you use the dataset for your research, please cite our `paper <presence/paper.pdf>`__ that describes it. We attached a `bibtex <presence/paper.bib>`__ record for your convenience. If you use the **Aruba** subset, you must also acknowledge the original `CASAS <presence/aruba.bib>`__ paper.

--------------

This dataset is part of the larger `LCAS-STRANDS long-term dataset collection <index.html>`__.

.. |image0| image:: images/object_presence/aruba-flat.png
.. |image1| image:: images/object_presence/aruba-scheme.jpg
.. |image2| image:: images/object_presence/brayford_top.png
.. |image3| image:: images/object_presence/observation.png
