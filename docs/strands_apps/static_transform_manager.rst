static\_transform\_manager
==========================

This provides a transformation manager node that broadcasts static
transformations at 30Hz, in the same way that static transformations can
be created using static\_tf\_broadcaster. Using this node static
transformations can be easier setup and removed than managing a
static\_tf\_broadcasters as sub processes.

Usage
~~~~~

::

    rosrun static_transform_manager static_tf_services.py

will start the manager node. This provides two services:

-  /static\_transforms\_manager/set\_tf
-  /static\_transforms\_manager/stop\_tf

``set_tf`` takes a single argument
``geometry_msgs/TransformStamped transform``, and returns a debug string
``response`` and a bool ``success``. The supplied transform is broadcast
at 30Hz.

``stop_tf`` takes a single argument ``string child_frame_id`` which is
the child frame to stop broadcasting.

Example
~~~~~~~

``rosrun static_transform_manager rviz_click_to_tf.py`` will listen to
points clicked in rviz and turn them into a transformation in the TF
tree.
