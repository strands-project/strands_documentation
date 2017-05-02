Long-term person activity datasets
----------------------------------

This dataset contains information about a given person activity over several weeks. It was used to evaluate which type of spatio-temporal models improve the accuracy of activity classification over time. The dataset contains information about human activity in two different environments:

-   **Aruba** dataset contains person activity collected at a smart apartment by the Center for Advanced Studies in Adaptive Systems, [CASAS](http://ailab.wsu.edu/casas/),
-   **Witham Wharf** dataset shows activity at the Lincoln Centre for Autonomous System, [LCAS](http://robots.lincoln.ac.uk/).

* * * * *

### Dataset structure

#### Aruba

![](images/person_activity/aruba-flat.png)

![](images/person_activity/aruba-scheme.jpg)

Aruba apartment visualisation

Aruba sensor layout (see [CASAS](http://ailab.wsu.edu/casas/))

The **Aruba** folder contains *activity.min*, which indicates the activity performed by a home-bound person in a small apartment every minute for 16 weeks. In addition *locations.min* contains the person location (room) minute-by-minute as well. The *location.names* and *activity.names* indicate which rooms and activities correspond to which number in the *activity.min* and *location.min* files. Example: number 0 on line 10 of the *location.min* and number 2 on 10th line of *activity.min* indicate that in the 10th minute after midnight of the first day, the person was *Eating* in the *Master bedroom*. The **Aruba** dataset was extracted from the [CASAS](http://ailab.wsu.edu/casas/) datasets.

#### Witham Wharf

![](images/person_activity/witham-cam.jpg)

![](images/person_activity/witham-topo.png)

Witham office overview

Witham office topological layout

The **Witham Wharf** directory contains activity of a particular student in an open-plan office for three weeks. Again, *locations.names* and *activity.names* files describe the locations and activities, which are stored in *location.min* and *activity.min* files.

These contain the student's activity and location on a minute-by-minute basis.

### Download

All of these datasets are available for download in a single archive [file](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/activity/activity.zip). After you unzip the file, you get two folders which correspond to the individual datasets.

* * * * *

### Condition of use

If you use the dataset for your research, please cite our [paper](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/activity/paper.pdf) that describes it. We attached a [bibtex](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/activity/paper.bib) record for your convenience. If you use the **Aruba** subset, you must also acknowledge the original [CASAS](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/presence/aruba.bib) paper.

* * * * *

This dataset is part of the larger [LCAS-STRANDS long-term dataset collection](https://lcas.lincoln.ac.uk/owncloud/shared/datasets/index.html).
