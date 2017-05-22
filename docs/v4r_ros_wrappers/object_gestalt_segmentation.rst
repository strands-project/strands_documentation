 # object\_gestalt\_segmentation

The current segmentation is based on the work of Ekaterina Popatova and
Andreas Richtsfeld. Segmented objects are discarded if they are too tall
or too far away from the robot. A service is provided that returns the
segmented object in the current scene. A more sophisticated solution
based on attention cues will be provided in the near future.

Technical Maintainer: [markus](https://github.com/edith-langer (Edith Langer, TU Wien) - langer@acin.tuwien.ac.at
-----------------------------------------------------------------------------------------------------------------

Contents
--------

1. Installation Requirements
2. Execution
3. Software architecture

1. Installation Requirements: 
------------------------------

ROS packages
^^^^^^^^^^^^

The ROS packages dependencies can be installed with the command:

::

    rosdep install --from-path object_gestalt_segmentation -i -y

2. Execution: 
--------------

::

    roslaunch object_gestalt_segmentation startup.launch

top
