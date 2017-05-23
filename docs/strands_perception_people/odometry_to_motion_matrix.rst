Odometry to motion\_matrix package
----------------------------------

This packge contains a tool for the conversion of the robots odometry to
a motion matrix to substitude the visual odometry.

All the information given on how to run the nodes should only be used if
you need to run them seperately. In normal cases please refer to the
``perception_people_launch`` package to start the whole perception
pipeline.

odom2visual
~~~~~~~~~~~

This node creates a motion matrix from the robots odometry using the
Eigen library to substitude the visual odometry.

Run with:

``roslaunch odometry_to_motion_matrix odom2visual.launch``

Parameters: \* ``odom``: *Default: /odom* The topic on which the robots
odometry is published \* ``motion_parameters``: *Default:
/visual*\ odometry/motion\_matrix\_ The topic on which the resulting
motion matrix is published


Original page: https://github.com/strands-project/strands_perception_people/blob/indigo-devel/odometry_to_motion_matrix/README.md